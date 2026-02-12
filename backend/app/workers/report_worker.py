"""Background worker for asynchronous report generation jobs."""

from __future__ import annotations

import asyncio
import os
import socket
from uuid import UUID

from pydantic import TypeAdapter

from app.api.dependencies import get_coordinator, get_report_job_repository
from app.core.config import settings
from app.core.logging import logger
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import AnamnesisUnion
from app.services.pdf_service import pdf_service


class ReportWorker:
    """Simple polling worker that processes report jobs from PostgreSQL."""

    def __init__(self):
        self.repository = get_report_job_repository()
        self.coordinator = get_coordinator()
        self.poll_interval = max(settings.REPORT_WORKER_POLL_INTERVAL_SECONDS, 1)
        self.worker_id = os.getenv("REPORT_WORKER_ID", socket.gethostname())
        self._anamnesis_adapter = TypeAdapter(AnamnesisUnion)

    async def run(self) -> None:
        """Continuously poll and process queued jobs."""
        logger.info(
            f"Report worker started (worker_id={self.worker_id}, poll={self.poll_interval}s)"
        )
        while True:
            job_row = self.repository.claim_next_job(worker_id=self.worker_id)
            if not job_row:
                await asyncio.sleep(self.poll_interval)
                continue

            await self._process_job(job_row)

    async def _process_job(self, job_row: dict) -> None:
        job_id = UUID(str(job_row["id"]))
        logger.info(f"Processing report job {job_id}")
        try:
            payload = job_row["request_payload"]
            exam_data = TNMExamData.model_validate(payload["exam_data"])
            anamnesis = self._anamnesis_adapter.validate_python(payload["anamnesis"])
            exam_type = payload.get("exam_type") or job_row["exam_type"]

            markdown_report, _ = await self.coordinator.generate_report(
                exam_data=exam_data,
                anamnesis=anamnesis,
                exam_type=exam_type,
            )

            pdf_bytes = None
            if pdf_service.is_available():
                pdf_bytes = pdf_service.generate_pdf(
                    markdown_content=markdown_report,
                    patient_id=exam_data.patient_id,
                    report_id=str(job_id),
                )
            else:
                logger.warning(
                    "wkhtmltopdf not available in worker container; saving markdown only"
                )

            self.repository.complete_job(
                job_id=job_id,
                markdown=markdown_report,
                pdf_bytes=pdf_bytes,
            )
            logger.info(f"Report job {job_id} completed")
        except Exception as exc:
            logger.exception(f"Report job {job_id} failed")
            self.repository.fail_job(job_id=job_id, error_message=str(exc))


async def main() -> None:
    worker = ReportWorker()
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())

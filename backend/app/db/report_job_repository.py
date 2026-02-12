"""PostgreSQL repository for asynchronous report jobs."""

from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Json

from app.core.config import settings
from app.schemas.report_jobs import ReportJobStatus


class ReportJobRepository:
    """Persistence layer for report job queue and results."""

    def __init__(self, dsn: str):
        self._dsn = dsn
        self._schema_ready = False

    @classmethod
    def from_settings(cls) -> "ReportJobRepository":
        """Build repository from environment settings."""
        dsn = settings.REPORT_JOBS_DATABASE_URL
        if dsn:
            return cls(dsn)

        return cls(
            (
                f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
                f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
            )
        )

    def _connect(self):
        return psycopg.connect(self._dsn, row_factory=dict_row)

    def _ensure_schema(self) -> None:
        if self._schema_ready:
            return
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS report_jobs (
                        id UUID PRIMARY KEY,
                        status VARCHAR(32) NOT NULL,
                        exam_type VARCHAR(64) NOT NULL,
                        request_payload JSONB NOT NULL,
                        result_markdown TEXT,
                        result_pdf BYTEA,
                        error_message TEXT,
                        worker_id TEXT,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        started_at TIMESTAMPTZ,
                        finished_at TIMESTAMPTZ
                    );
                    """
                )
                cur.execute(
                    """
                    CREATE INDEX IF NOT EXISTS idx_report_jobs_status_created
                    ON report_jobs (status, created_at);
                    """
                )
        self._schema_ready = True

    def create_job(self, exam_type: str, payload: dict[str, Any]) -> UUID:
        """Create a queued report job."""
        self._ensure_schema()
        job_id = uuid4()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO report_jobs (id, status, exam_type, request_payload)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (
                        job_id,
                        ReportJobStatus.QUEUED.value,
                        exam_type,
                        Json(payload),
                    ),
                )
        return job_id

    def claim_next_job(self, worker_id: str) -> dict[str, Any] | None:
        """Atomically claim one queued job for processing."""
        self._ensure_schema()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    WITH next_job AS (
                        SELECT id
                        FROM report_jobs
                        WHERE status = %s
                        ORDER BY created_at
                        FOR UPDATE SKIP LOCKED
                        LIMIT 1
                    )
                    UPDATE report_jobs j
                    SET status = %s,
                        worker_id = %s,
                        started_at = NOW(),
                        updated_at = NOW()
                    FROM next_job
                    WHERE j.id = next_job.id
                    RETURNING j.*;
                    """,
                    (
                        ReportJobStatus.QUEUED.value,
                        ReportJobStatus.RUNNING.value,
                        worker_id,
                    ),
                )
                row = cur.fetchone()
                return row if row else None

    def complete_job(
        self,
        job_id: UUID,
        markdown: str,
        pdf_bytes: bytes | None,
    ) -> None:
        """Persist successful report generation result."""
        self._ensure_schema()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE report_jobs
                    SET status = %s,
                        result_markdown = %s,
                        result_pdf = %s,
                        finished_at = NOW(),
                        updated_at = NOW(),
                        error_message = NULL
                    WHERE id = %s;
                    """,
                    (
                        ReportJobStatus.COMPLETED.value,
                        markdown,
                        pdf_bytes,
                        job_id,
                    ),
                )

    def fail_job(self, job_id: UUID, error_message: str) -> None:
        """Persist job failure details."""
        self._ensure_schema()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE report_jobs
                    SET status = %s,
                        error_message = %s,
                        finished_at = NOW(),
                        updated_at = NOW()
                    WHERE id = %s;
                    """,
                    (
                        ReportJobStatus.FAILED.value,
                        error_message[:2000],
                        job_id,
                    ),
                )

    def get_job(self, job_id: UUID) -> dict[str, Any] | None:
        """Retrieve one job by id."""
        self._ensure_schema()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        id, status, exam_type, request_payload, result_markdown,
                        error_message, worker_id, created_at, updated_at,
                        started_at, finished_at, (result_pdf IS NOT NULL) AS has_pdf
                    FROM report_jobs
                    WHERE id = %s;
                    """,
                    (job_id,),
                )
                row = cur.fetchone()
                return row if row else None

    def get_result_pdf(self, job_id: UUID) -> bytes | None:
        """Retrieve stored PDF bytes for a completed job."""
        self._ensure_schema()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT result_pdf
                    FROM report_jobs
                    WHERE id = %s
                    AND status = %s;
                    """,
                    (job_id, ReportJobStatus.COMPLETED.value),
                )
                row = cur.fetchone()
                if not row:
                    return None
                return row["result_pdf"]

    @staticmethod
    def map_job_response(row: dict[str, Any]) -> dict[str, Any]:
        """Normalize DB row for API serialization."""
        return {
            "job_id": str(row["id"]),
            "status": row["status"],
            "exam_type": row["exam_type"],
            "created_at": _as_datetime(row["created_at"]),
            "updated_at": _as_datetime(row["updated_at"]),
            "started_at": _as_datetime(row.get("started_at")),
            "finished_at": _as_datetime(row.get("finished_at")),
            "error_message": row.get("error_message"),
            "report_markdown": row.get("result_markdown"),
            "has_pdf": bool(row.get("has_pdf", False)),
        }


def _as_datetime(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(str(value))

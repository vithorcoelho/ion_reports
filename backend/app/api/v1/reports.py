"""Report API endpoints for generating medical reports.

This module provides REST API endpoints for generating medical reports
using different plugins (IonNutri, VidaNova).
"""

from contextlib import nullcontext
from datetime import datetime
from time import perf_counter
from uuid import UUID

import mlflow
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel

from app.api.dependencies import get_coordinator, get_report_job_repository
from app.core.config import settings
from app.core.logging import logger
from app.db.report_job_repository import ReportJobRepository
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import AnamnesisUnion
from app.schemas.report_jobs import ReportAsyncAccepted, ReportJobResult, ReportJobStatus
from app.schemas.report_out import MarkdownReportOut
from app.services.pdf_service import pdf_service
from app.services.report_coordinator import ReportCoordinator

router = APIRouter()


class PDFGenerationRequest(BaseModel):
    """Request model for PDF generation."""

    markdown_content: str
    patient_id: str
    report_id: str


@router.post("/reports/", response_model=MarkdownReportOut | ReportAsyncAccepted)
async def generate_report(
    exam_data: TNMExamData,
    anamnesis: AnamnesisUnion,
    exam_type: str | None = Query(
        default=None, description="Plugin type: ionnutri, vidanova"
    ),
    async_mode: bool = Query(
        default=False,
        alias="async",
        description="When true, enqueue report generation and return a job id.",
    ),
    coordinator: ReportCoordinator = Depends(get_coordinator),  # noqa: B008
    job_repository: ReportJobRepository = Depends(get_report_job_repository),  # noqa: B008
) -> MarkdownReportOut | ReportAsyncAccepted | None:
    """Gera um relatório TNM em formato markdown com base nos dados do exame e anamnese do paciente."""
    if exam_data.patient_id != anamnesis.patient_id:
        raise HTTPException(400, "IDs de paciente inconsistentes")
    exam_type = exam_type or anamnesis.anamnesis_type

    if async_mode:
        payload = {
            "exam_data": exam_data.model_dump(mode="json"),
            "anamnesis": anamnesis.model_dump(mode="json"),
            "exam_type": exam_type,
        }
        job_id = job_repository.create_job(exam_type=exam_type, payload=payload)
        return ReportAsyncAccepted(
            job_id=str(job_id),
            status=ReportJobStatus.QUEUED,
            message="Relatório enfileirado para processamento assíncrono.",
        )

    run_name = f"TNM_Report_Patient_{exam_data.patient_id}"

    # Use MLflow context only if enabled, otherwise use nullcontext (no-op)
    # Wrap in try/except to handle runtime MLflow unavailability gracefully
    mlflow_context = nullcontext()
    mlflow_active = False
    if settings.MLFLOW_ENABLED:
        try:
            mlflow_context = mlflow.start_run(
                run_name=run_name,
                tags={
                    "patient_id": str(exam_data.patient_id),
                    "stage": "report_generation",
                },
            )
            mlflow_active = True
        except Exception as e:
            logger.warning(
                f"MLflow start_run failed: {e}. Proceeding without tracking."
            )

    with mlflow_context:
        try:
            if mlflow_active:
                mlflow.log_params(
                    {
                        "exam_data": exam_data.model_dump(),
                        "anamnesis": anamnesis.model_dump(),
                    }
                )
            start = perf_counter()
            logger.info(f"Gerando relatório markdown para {exam_data.patient_id}")
            # Generate both markdown and structured report through coordinator
            markdown_report, structured_report = await coordinator.generate_report(
                exam_data, anamnesis, exam_type
            )

            if mlflow_active:
                # Save the final report in mlflow artifacts
                mlflow.log_text(
                    markdown_report, artifact_file="final_reports/report.md"
                )
                mlflow.log_metric("generation_time_sec", perf_counter() - start)

            logger.info("Relatório markdown retornado pela API")

            return MarkdownReportOut(
                report_id=exam_data.patient_id,
                patient_id=exam_data.patient_id,
                anamnesis_id=exam_data.patient_id,
                exam_id=exam_data.patient_id,
                version="1.0",
                timestamp=datetime.now(),
                report=markdown_report,
            )

        except Exception as e:
            logger.error(f"Erro ao gerar relatório: {str(e)}")
            raise HTTPException(500, f"Erro interno: {str(e)}") from e


@router.get("/reports/jobs/{job_id}", response_model=ReportJobResult)
async def get_async_report_status(
    job_id: UUID,
    job_repository: ReportJobRepository = Depends(get_report_job_repository),  # noqa: B008
) -> ReportJobResult:
    """Recupera status e resultado de um job assíncrono de relatório."""
    row = job_repository.get_job(job_id)
    if not row:
        raise HTTPException(status_code=404, detail="Job não encontrado")
    return ReportJobResult.model_validate(ReportJobRepository.map_job_response(row))


@router.get("/reports/jobs/{job_id}/pdf")
async def get_async_report_pdf(
    job_id: UUID,
    job_repository: ReportJobRepository = Depends(get_report_job_repository),  # noqa: B008
) -> Response:
    """Retorna o PDF armazenado para um job assíncrono concluído."""
    row = job_repository.get_job(job_id)
    if not row:
        raise HTTPException(status_code=404, detail="Job não encontrado")
    if row["status"] != ReportJobStatus.COMPLETED.value:
        raise HTTPException(
            status_code=409,
            detail=f"Job ainda não concluído (status atual: {row['status']})",
        )

    pdf_bytes = job_repository.get_result_pdf(job_id)
    if not pdf_bytes:
        raise HTTPException(status_code=404, detail="PDF não disponível para este job")

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="report_{job_id}.pdf"'
        },
    )


@router.post("/reports/pdf")
async def generate_pdf_from_markdown(request: PDFGenerationRequest) -> Response:
    """Gera um PDF a partir de conteúdo markdown.

    Este endpoint converte um relatório markdown em PDF formatado profissionalmente.

    Args:
        request: Dados para geração do PDF (markdown, patient_id, report_id)

    Returns:
        Response com o PDF em bytes

    Raises:
        HTTPException 503: Se wkhtmltopdf não estiver instalado
        HTTPException 500: Se houver erro na geração do PDF

    """
    # Check if PDF service is available
    if not pdf_service.is_available():
        raise HTTPException(
            status_code=503,
            detail=(
                "PDF generation is not available. wkhtmltopdf is not installed. "
                "Install it with: sudo apt-get install wkhtmltopdf (Ubuntu/Debian) "
                "or brew install wkhtmltopdf (macOS)"
            ),
        )

    try:
        logger.info(f"Generating PDF for report {request.report_id}")

        # Generate PDF
        pdf_bytes = pdf_service.generate_pdf(
            markdown_content=request.markdown_content,
            patient_id=request.patient_id,
            report_id=request.report_id,
        )

        logger.info(f"PDF generated successfully for report {request.report_id}")

        # Return PDF as response
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="report_{request.report_id}.pdf"'
            },
        )

    except RuntimeError as e:
        logger.error(f"PDF service error: {str(e)}")
        raise HTTPException(status_code=503, detail=str(e)) from e
    except Exception as e:
        logger.error(f"Error generating PDF: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to generate PDF: {str(e)}"
        ) from e

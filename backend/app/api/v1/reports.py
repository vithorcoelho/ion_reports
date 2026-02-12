"""Report API endpoints for generating medical reports.

This module provides REST API endpoints for generating medical reports
using different plugins (IonNutri, VidaNova).
"""

from contextlib import nullcontext
from datetime import datetime
from time import perf_counter

import mlflow
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel

from app.api.dependencies import get_coordinator
from app.core.config import settings
from app.core.logging import logger
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import AnamnesisUnion
from app.schemas.report_out import MarkdownReportOut
from app.services.pdf_service import pdf_service
from app.services.report_coordinator import ReportCoordinator

router = APIRouter()


class PDFGenerationRequest(BaseModel):
    """Request model for PDF generation."""

    markdown_content: str
    patient_id: str
    report_id: str


@router.post("/reports/", response_model=MarkdownReportOut)
async def generate_report(
    exam_data: TNMExamData,
    anamnesis: AnamnesisUnion,
    exam_type: str | None = Query(
        default=None, description="Plugin type: ionnutri, vidanova"
    ),
    coordinator: ReportCoordinator = Depends(get_coordinator),  # noqa: B008
) -> MarkdownReportOut | None:
    """Gera um relatório TNM em formato markdown com base nos dados do exame e anamnese do paciente."""
    if exam_data.patient_id != anamnesis.patient_id:
        raise HTTPException(400, "IDs de paciente inconsistentes")
    exam_type = exam_type or anamnesis.anamnesis_type

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

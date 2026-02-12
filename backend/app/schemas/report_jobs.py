"""Schemas for asynchronous report job API responses."""

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class ReportJobStatus(StrEnum):
    """Possible states for report generation jobs."""

    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class ReportAsyncAccepted(BaseModel):
    """Response returned when an async report job is accepted."""

    job_id: str = Field(..., description="Unique identifier for the async job")
    status: ReportJobStatus = Field(
        ..., description="Current status for the queued job"
    )
    message: str = Field(..., description="Human-readable processing message")


class ReportJobResult(BaseModel):
    """State and result payload for an async report job."""

    job_id: str
    status: ReportJobStatus
    exam_type: str
    created_at: datetime
    updated_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None
    error_message: str | None = None
    report_markdown: str | None = None
    has_pdf: bool = False

"""Output schemas for medical report API responses.

This module defines the output schemas used for API responses, providing
a clean interface for delivering markdown formatted medical reports to clients
along with essential metadata.

Classes:
    BaseReportOut: Base schema with essential metadata fields.
    MarkdownReportOut: Schema for markdown reports with metadata.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class BaseReportOut(BaseModel):
    """Base output schema containing essential metadata fields for reports.

    This base class provides the core metadata fields for report identification
    and tracking, ensuring consistency across all report responses.

    Attributes:
        report_id (str): Unique identifier for the report.
        patient_id (str): Identifier for the patient.
        anamnesis_id (str): Identifier for the anamnesis data.
        exam_id (str): Identifier for the examination data.
        version (str): Report version identifier.
        timestamp (datetime): Report generation timestamp.

    """

    # Core metadata only
    report_id: str = Field(..., description="Unique identifier for the report")
    patient_id: str = Field(..., description="Identifier for the patient")
    anamnesis_id: str = Field(..., description="Identifier for the anamnesis data")
    exam_id: str = Field(..., description="Identifier for the examination data")
    version: str = Field(..., description="Report version identifier")
    timestamp: datetime = Field(..., description="Report generation timestamp")


class MarkdownReportOut(BaseReportOut):
    """Simplified output schema containing the markdown report and essential metadata.

    This schema provides a clean API response containing the markdown formatted
    report that users receive along with essential tracking metadata inherited
    from BaseReportOut.

    Attributes:
        Inherits all BaseReportOut metadata fields plus:
        report (str): Complete markdown formatted report ready for user display.

    """

    # Main content - metadata inherited from BaseReportOut
    report: str = Field(
        ..., description="Complete markdown formatted report for user display"
    )

"""Exam configuration for VidaNova exams."""

from typing import Any

from pydantic import BaseModel

from app.domain.exam_configs.base_config import BaseExamConfig
from app.domain.report import (
    FindingsSection,
    MarkdownReport,
    SummaryContent,
    SupplementRecommendationSectionWrapper,
    TrainingRecommendation,
    VidaNovaDietSuggestions,
)


class VidaNovaConfig(BaseExamConfig):
    """Schema mappings for different sections."""

    # Placeholder for status mapping. Add actual values as needed.
    STATUS_MAPPING: dict[str, str] = {}

    SECTION_SCHEMAS = {
        "findings": FindingsSection,
        "supplements": SupplementRecommendationSectionWrapper,
        "diet": VidaNovaDietSuggestions,
        "training": TrainingRecommendation,
        "summary": SummaryContent,
        "markdown": MarkdownReport,
    }

    def get_exam_type(self) -> str:
        """Return exam type."""
        return "vidanova"

    def get_status_mapping(self) -> dict:
        """Get status mapping for this exam type."""
        return self.STATUS_MAPPING

    def get_section_schemas(self) -> dict[str, type[BaseModel]]:
        """Get section schemas for this exam type."""
        return self.SECTION_SCHEMAS.copy()

    def get_formatting_config(self) -> dict[str, Any]:
        """Get formatting rules for VidaNova reports."""
        return {
            "style": "Focado em performance com linguagem motivacional",
            "headers": "Use ## para seções principais e ### para subseções",
            "format": "Markdown  e listas numeradas",
        }

    def get_complete_report_schema(self):
        """Get complete report schema for single-pass generation."""
        return MarkdownReport

    def get_status_mapping(self) -> dict[str, Any]:
        """Get status mapping for VidaNova."""
        return {}  # VidaNova doesn't use complex status mapping

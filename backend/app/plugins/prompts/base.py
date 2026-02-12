"""Base interface for prompt management across different plugins.

This module defines the abstract PromptInterface class that all prompt
implementations must follow to ensure consistent behavior.
"""

from abc import ABC, abstractmethod


class PromptInterface(ABC):  # pragma: no cover
    """Interface base para prompts de plugins."""

    @staticmethod
    @abstractmethod
    def _build_context_section(section_name: str, data: dict) -> str:
        pass

    @staticmethod
    @abstractmethod
    def _generate_prompt(
        prompt_type: str, data: dict, context: dict | None = None
    ) -> tuple[str, str]:
        pass

    @abstractmethod
    def _prepare_data(self, exam_data, anamnesis, kg_data) -> dict:
        pass

    @abstractmethod
    def get_findings_prompt(self, exam_data, anamnesis, kg_data):
        """Get findings system role."""
        pass

    @abstractmethod
    def get_supplements_prompt(self, exam_data, anamnesis, kg_data):
        """Get supplements system role."""
        pass

    @abstractmethod
    def get_summary_prompt(self, exam_data, anamnesis, kg_data, all_previous_context):
        """Get summary system role."""
        pass

    @abstractmethod
    def get_markdown_report_prompt(
        self, exam_data, anamnesis, kg_data, final_report_structured_data
    ):
        """Get markdown report system role."""
        pass

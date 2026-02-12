"""Base plugin interface for report generation."""

from abc import ABC, abstractmethod

from app.domain.kg_result import KGResult
from app.domain.report import BaseReport
from app.plugins.prompts.base import PromptInterface
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.llm.llm_service import OpenRouterLLMService


class ReportPlugin[PromptT: PromptInterface](ABC):
    """Generic base class for medical report generation plugins.

    This abstract class defines the interface that all report generation plugins
    must implement. It provides a common structure for plugins that generate
    different types of medical reports based on examination data, patient
    anamnesis, and knowledge graph information.

    Type Parameters:
        PromptT: The specific prompt interface type used by the plugin,
                must be a subclass of PromptInterface.

    Attributes:
        llm_service (OpenRouterLLMService): Service for interacting with language models.
        prompt (PromptT): Plugin-specific prompt management interface.

    """

    def __init__(self, llm_service: OpenRouterLLMService, prompt: PromptT):
        """Initialize the plugin with required services.

        Args:
            llm_service (OpenRouterLLMService): Service for LLM API interactions and
                                    structured response generation.
            prompt (PromptT): Plugin-specific prompt interface that provides
                            templated prompts for different report sections.

        """
        self.llm_service = llm_service
        self.prompt = prompt

    @abstractmethod
    async def build_report(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> BaseReport:
        """Build a medical report using validated data and knowledge graph context.

        This method orchestrates the report generation process by:
        1. Processing the input data (exam results, patient history, KG insights)
        2. Generating prompts for different report sections
        3. Calling the LLM service to generate structured content
        4. Assembling the final report in the appropriate format

        Args:
            exam_data (TNMExamData): Laboratory examination results and
                                   metabolite measurements.
            anamnesis (PatientAnamnesis): Patient medical history, symptoms,
                                        and clinical background information.
            kg_data (KGResult): Knowledge graph query results containing
                              relevant medical knowledge and recommendations.

        Returns:
            BaseReport: Complete structured medical report with common fields
                       (report metadata, summary, findings) plus plugin-specific
                       sections.

        """
        pass

    @abstractmethod
    async def get_markdown_report(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> tuple[str, BaseReport]:
        """Generate a markdown report for user display along with metadata.

        This method should generate a user-friendly markdown report based on the
        examination data, patient anamnesis, and knowledge graph information.
        It returns both the markdown content and the structured report for metadata.

        Args:
            exam_data (TNMExamData): Laboratory examination results and
                                   metabolite measurements.
            anamnesis (PatientAnamnesis): Patient medical history, symptoms,
                                        and clinical background information.
            kg_data (KGResult): Knowledge graph query results containing
                              relevant medical knowledge and recommendations.

        Returns:
            tuple[str, BaseReport]: A tuple containing:
                - Complete markdown-formatted report ready for user display
                - Structured report object containing metadata

        """
        pass

    @abstractmethod
    def get_plugin_name(self) -> str:
        """Return the unique identifier name of the plugin.

        This name is used for plugin registration, routing requests to the
        appropriate plugin, and logging/debugging purposes.

        Returns:
            str: Lowercase string identifier for the plugin (e.g., "ionnutri").
            Should be unique across all plugins in the system.

        """
        pass

"""VidaNova plugin for fitness and performance-focused medical reports.

This module contains the VidaNova plugin implementation for generating medical
reports focused on physical performance and fitness recommendations.
"""

from datetime import datetime
from typing import Any

import mlflow

from app.constants.vidanova_constants import SECTION_SCHEMAS
from app.core.config import settings
from app.core.logging import logger
from app.domain.kg_result import KGResult, MetaboliteInfo
from app.domain.report import (
    FindingItem,
    FindingsSection,
    SummaryContent,
    SupplementItem,
    TrainingRecommendation,
    VidaNovaDietSuggestions,
    VidaNovaReport,
)
from app.plugins.base import ReportPlugin
from app.plugins.prompts.vidanova_prompts import VidaNovaPrompts
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.llm.llm_service import OpenRouterLLMService


class VidaNovaPlugin(ReportPlugin[VidaNovaPrompts]):
    """VidaNova plugin for generating performance and fitness-focused reports.

    This plugin specializes in creating medical reports with emphasis on physical
    performance, fitness recommendations, and lifestyle modifications tailored
    for active individuals and athletes.

    Attributes:
        llm_service (OpenRouterLLMService): Service for LLM interactions.
        prompt (VidaNovaPrompts): Prompt interface for generating section content.

    """

    def __init__(self, llm_service: OpenRouterLLMService, prompt: VidaNovaPrompts):
        """Initialize the VidaNova plugin.

        Args:
            llm_service (OpenRouterLLMService): Service for LLM interactions.
            prompt (VidaNovaPrompts): Prompt interface for content generation.

        """
        super().__init__(llm_service, prompt)
        logger.info("VidaNovaPlugin iniciado.")

    @mlflow.trace(name="build_vidanova_report", span_type="func")
    async def build_report(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
    ) -> VidaNovaReport:
        """Build a VidaNova medical report using structured section generation.

        Args:
            exam_data (TNMExamData): The examination data.
            anamnesis (PatientAnamnesis): The patient anamnesis data.
            kg_data (KGResult): Knowledge graph query results.

        Returns:
            VidaNovaReport: The generated VidaNova report.

        """
        logger.info(f"Building VidaNova report for patient {exam_data.patient_id}")

        timestamp = datetime.now()
        report_id = f"vida_{exam_data.patient_id}_{timestamp.strftime('%Y%m%d_%H%M%S')}"
        anamnesis_id = f"anam_{exam_data.patient_id}_{timestamp.strftime('%Y%m%d')}"
        exam_id = (
            f"exam_{exam_data.patient_id}_{exam_data.exam_date.strftime('%Y%m%d')}"
        )

        # Generate all section contents using structured approach
        section_contents = await self._generate_section_contents(
            exam_data, anamnesis, kg_data
        )

        # Build the report using generated sections
        report = VidaNovaReport(
            report_id=report_id,
            patient_id=exam_data.patient_id,
            anamnesis_id=anamnesis_id,
            exam_id=exam_id,
            version="1.0",
            timestamp=timestamp,
            summary=self._build_summary_section(section_contents.get("summary")),
            findings=self._build_findings_section(
                kg_data.metabolite_info, section_contents.get("findings")
            ),
            diet_suggestions=self._build_diet_suggestions_section(section_contents),
            supplements=self._build_supplements_section(
                section_contents.get("supplements")
            ),
            training=self._build_training_section(section_contents.get("training")),
        )

        logger.info(f"VidaNova report built successfully: {report.report_id}")
        return report

    def get_plugin_name(self) -> str:
        """Return the plugin name identifier.

        Returns:
            str: The string "vidanova" identifying this plugin.

        """
        return "vidanova"

    @mlflow.trace(name="get_vidanova_markdown_report", span_type="func")
    async def get_markdown_report(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> tuple[str, VidaNovaReport]:
        """Generate a markdown report for user display along with metadata.

        Args:
            exam_data: Laboratory examination results and metabolite measurements
            anamnesis: Patient medical history, symptoms, and clinical background information
            kg_data: Knowledge graph query results containing relevant medical knowledge

        Returns:
            tuple[str, VidaNovaReport]: Markdown report and structured report with metadata

        """
        try:
            # First generate the structured report
            structured_report = await self.build_report(exam_data, anamnesis, kg_data)

            # Then generate markdown based on the structured report
            system_prompt, user_prompt = self.prompt.get_markdown_report_prompt(
                exam_data, anamnesis, kg_data, structured_report.model_dump(mode="json")
            )

            markdown_response = await self.llm_service.call_llm(
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                schema=None,  # No structured output needed for markdown
                temperature=settings.OPENROUTER_TEMPERATURE,
                max_tokens=settings.OPENROUTER_MAX_TOKENS,
            )

            # Extract text from response
            if hasattr(markdown_response, "content"):
                markdown_content = markdown_response.content
            elif isinstance(markdown_response, str):
                markdown_content = markdown_response
            else:
                markdown_content = str(markdown_response)

            return markdown_content, structured_report

        except Exception as e:
            logger.error(f"Error generating markdown report: {str(e)}")
            # Return error markdown and a basic report structure
            error_report = await self.build_report(exam_data, anamnesis, kg_data)
            return (
                "# Relatório VidaNova\n\nErro na geração do relatório em markdown.",
                error_report,
            )

    @mlflow.trace(name="generate_section_contents", span_type="func")
    async def _generate_section_contents(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> dict[str, Any]:
        """Generate content for all report sections using structured approach.

        Args:
            exam_data: Examination data
            anamnesis: Patient anamnesis data
            kg_data: Knowledge graph data

        Returns:
            Dict[str, Any]: Dictionary with content for all generated sections

        """
        section_contents: dict[str, Any] = {}

        # Configuration for VidaNova sections with execution order
        SECTION_CONFIG = {
            # Basic sections (no context required)
            "findings": {
                "prompt_func": self.prompt.get_findings_prompt,
                "schema": SECTION_SCHEMAS["findings"],
                "requires_context": False,
            },
            # Diet section (unified)
            "diet_suggestions": {
                "prompt_func": self.prompt.get_diet_suggestions_prompt,
                "schema": SECTION_SCHEMAS["diet_suggestions"],
                "requires_context": True,
            },
            # Other sections
            "supplements": {
                "prompt_func": self.prompt.get_supplements_prompt,
                "schema": SECTION_SCHEMAS["supplements"],
                "requires_context": True,
            },
            "training": {
                "prompt_func": self.prompt.get_training_prompt,
                "schema": SECTION_SCHEMAS["training"],
                "requires_context": True,
            },
            # Summary generated last with all context
            "summary": {
                "prompt_func": self.prompt.get_summary_prompt,
                "schema": SECTION_SCHEMAS["summary"],
                "requires_context": True,
            },
        }

        # 1. Generate sections without context first
        for section_name, config in SECTION_CONFIG.items():
            if not config["requires_context"]:
                await self._generate_section(
                    section_name,
                    config,
                    exam_data,
                    anamnesis,
                    kg_data,
                    section_contents,
                )

        # 2. Generate sections with context (summary)
        for section_name, config in SECTION_CONFIG.items():
            if config["requires_context"]:
                await self._generate_section(
                    section_name,
                    config,
                    exam_data,
                    anamnesis,
                    kg_data,
                    section_contents,
                )

        return section_contents

    @mlflow.trace(name="generate_vidanova_section", span_type="llm")
    async def _generate_section(
        self,
        section_name: str,
        config: dict,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        section_contents: dict,
    ):
        """Generate a specific section using standardized configuration.

        Args:
            section_name: Name of the section to generate
            config: Section configuration (prompt_func, schema, etc.)
            exam_data: Examination data
            anamnesis: Patient anamnesis data
            kg_data: Knowledge graph data
            section_contents: Dictionary to be modified in-place with generated content

        """
        try:
            prompt_func = config["prompt_func"]
            target_schema = config["schema"]

            # Generate prompt
            if config["requires_context"]:
                # Summary needs context from all other sections
                system_prompt_content, user_prompt_content = prompt_func(
                    exam_data, anamnesis, kg_data, section_contents
                )
            else:
                # Basic sections without context
                system_prompt_content, user_prompt_content = prompt_func(
                    exam_data, anamnesis, kg_data
                )

            # Call LLM
            llm_response = await self.llm_service.call_llm(
                user_prompt=user_prompt_content,
                system_prompt=system_prompt_content,
                schema=target_schema,
                temperature=settings.OPENROUTER_TEMPERATURE,
                max_tokens=settings.OPENROUTER_MAX_TOKENS,
            )

            logger.debug(f"LLM response for section '{section_name}': {llm_response}")

            # Store the result
            section_contents[section_name] = (
                llm_response.model_dump()
                if hasattr(llm_response, "model_dump")
                else llm_response
            )

        except Exception as e:
            logger.error(f"Error generating section '{section_name}': {str(e)}")
            # Store empty section on error
            section_contents[section_name] = {}

    def _build_summary_section(self, summary_data: dict | None) -> SummaryContent:
        """Build the summary section from LLM-generated data."""
        if summary_data and summary_data.get("content"):
            content = summary_data.get("content")
            return SummaryContent(
                content=content
                if isinstance(content, str)
                else "Resumo não disponível."
            )
        else:
            return SummaryContent(content="Resumo não disponível.")

    def _build_findings_section(
        self,
        metabolite_info: list[MetaboliteInfo],
        findings_section_data: dict | None,
    ) -> FindingsSection:
        """Build the findings section from knowledge graph and LLM data."""
        findings = []
        for metabolite in metabolite_info:
            try:
                finding = FindingItem(
                    status=metabolite.status,
                    description=metabolite.description,
                    metabolite=metabolite.name,
                    implications=[],  # VidaNova focuses more on performance implications
                )
                findings.append(finding)
            except Exception as e:
                logger.warning(
                    f"Error processing metabolite {metabolite.name}: {str(e)}"
                )

        conclusion_text = (
            findings_section_data.get("conclusion")
            if findings_section_data
            else "Conclusão focada em performance não disponível."
        )
        if not isinstance(conclusion_text, str):
            conclusion_text = "Conclusão focada em performance não disponível."

        items = (
            findings_section_data.get("items") if findings_section_data else findings
        )
        if not isinstance(items, list):
            items = findings

        return FindingsSection(items=items, conclusion=conclusion_text)

    def _build_diet_suggestions_section(
        self, section_contents: dict[str, dict]
    ) -> VidaNovaDietSuggestions:
        """Build the diet suggestions section from unified diet data."""
        diet_data = section_contents.get("diet_suggestions")

        if diet_data:
            return VidaNovaDietSuggestions(
                carnivoro_onivoro=diet_data.get("carnivoro_onivoro", []),
                vegetariano=diet_data.get("vegetariano", []),
                vegano=diet_data.get("vegano", []),
            )
        else:
            return VidaNovaDietSuggestions(
                carnivoro_onivoro=["Sugestões não disponíveis"],
                vegetariano=["Sugestões não disponíveis"],
                vegano=["Sugestões não disponíveis"],
            )

    def _build_supplements_section(
        self, supplements_data: dict | None
    ) -> list[SupplementItem]:
        """Build the supplements section from LLM-generated data."""
        if not supplements_data:
            return []

        # Handle if it's a wrapper with items list
        items = supplements_data.get("items", [])
        if isinstance(items, list) and items:
            if isinstance(items[0], dict):
                return [SupplementItem(**item) for item in items]
            else:
                return items
        return []

    def _build_training_section(
        self, training_data: dict | None
    ) -> TrainingRecommendation:
        """Build the training section from LLM-generated data."""
        if training_data:
            return TrainingRecommendation(
                recommendations=training_data.get("recommendations", []),
                avoid=training_data.get("avoid", []),
                focus=training_data.get(
                    "focus", "Treino de força com descanso adequado"
                ),
            )
        else:
            return TrainingRecommendation(
                recommendations=["Treino de força com carga leve/moderada"],
                avoid=["Exercícios aeróbicos muito longos"],
                focus="Treino de força com descanso adequado para ganho de massa magra",
            )

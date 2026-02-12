"""IonNutri plugin for comprehensive nutritional medical reports.

This module contains the IonNutri plugin implementation for generating detailed
medical reports focused on nutritional analysis, metabolite findings, and
comprehensive dietary recommendations based on knowledge graph data.
"""

from datetime import datetime
from typing import Any, TypeVar

import mlflow
from pydantic import BaseModel

from app.constants.metabolite_constants import (
    METABOLITE_STATUS_CONFIG,
    SECTION_SCHEMAS,
    STATUS_MAPPING,
)
from app.core.config import settings
from app.core.logging import logger
from app.domain.kg_result import KGResult, MetaboliteInfo
from app.domain.report import (
    DeficiencyItem,
    ExamItem,
    FindingItem,
    FindingsSection,
    IonNutriReport,
    NutritionalRecs,
    RecommendationsSection,
    SummaryContent,
)
from app.domain.status import MetaboliteStatusEnum
from app.plugins.base import ReportPlugin
from app.plugins.prompts.ionnutri_prompts import IonNutriPrompts
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.llm.llm_service import OpenRouterLLMService

T = TypeVar("T", bound=BaseModel)


class IonNutriPlugin(ReportPlugin[IonNutriPrompts]):
    """IonNutri plugin for comprehensive nutritional medical reports.

    This plugin generates detailed medical reports with focus on metabolite
    analysis, nutritional deficiencies, dietary recommendations, and lifestyle
    interventions based on knowledge graph data and patient information.

    Attributes:
        llm_service (OpenRouterLLMService): Service for LLM interactions.
        prompt (IonNutriPrompts): Specialized prompts for IonNutri reports.

    """

    def __init__(self, llm_service: OpenRouterLLMService, prompt: IonNutriPrompts):
        """Initialize the IonNutri plugin.

        Args:
            llm_service (OpenRouterLLMService): Service for LLM interactions.
            prompt (IonNutriPrompts): IonNutri-specific prompt templates.

        """
        super().__init__(llm_service, prompt)
        logger.info("IonNutriPlugin initialized.")

    @mlflow.trace(name="build_ionnutri_report", span_type="func")
    async def build_report(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> IonNutriReport:
        """Build a comprehensive IonNutri medical report.

        Args:
            exam_data (TNMExamData): The examination data.
            anamnesis (PatientAnamnesis): The patient anamnesis data.
            kg_data (KGResult): Knowledge graph query results.

        Returns:
            IonNutriReport: The generated comprehensive medical report.

        """
        logger.info(f"Building IonNutri report for patient {exam_data.patient_id}")

        timestamp = datetime.now()
        report_id = f"TNM_{exam_data.patient_id}_{timestamp.strftime('%Y%m%d_%H%M%S')}"
        anamnesis_id = f"anam_{exam_data.patient_id}_{timestamp.strftime('%Y%m%d')}"
        exam_id = (
            f"exam_{exam_data.patient_id}_{exam_data.exam_date.strftime('%Y%m%d')}"
        )

        section_contents = await self._generate_section_contents(
            exam_data, anamnesis, kg_data
        )

        report = IonNutriReport(
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
            recommendations=self._build_recommendations_section(section_contents),
            deficiencies=self._build_deficiencies_section(
                section_contents.get("deficiencies")
            ),
            general_guidelines=self._build_guidelines_section(
                section_contents.get("guidelines")
            ),
            additional_exams=self._build_additional_exams_section(
                section_contents.get("exams")
            ),
        )
        logger.info(f"IonNutri report built successfully: {report.report_id}")
        return report

    def get_plugin_name(self) -> str:
        """Return the plugin name identifier.

        Returns:
            str: The string "ionnutri" identifying this plugin.

        """
        return "ionnutri"

    @mlflow.trace(name="get_ionnutri_markdown_report", span_type="func")
    async def get_markdown_report(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> tuple[str, IonNutriReport]:
        """Generate a markdown report for user display along with metadata.

        Args:
            exam_data: Laboratory examination results and metabolite measurements
            anamnesis: Patient medical history, symptoms, and clinical background information
            kg_data: Knowledge graph query results containing relevant medical knowledge

        Returns:
            tuple[str, IonNutriReport]: Markdown report and structured report with metadata

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
                "# Relatório IonNutri\n\nErro na geração do relatório em markdown.",
                error_report,
            )

    @mlflow.trace(name="generate_section_contents", span_type="func")
    async def _generate_section_contents(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> dict[str, Any]:
        """Gera o conteúdo de todas as seções do relatório usando prompts padronizados.

        Refatorado para eliminar condicionais desnecessários.

        Args:
            exam_data: Dados do exame
            anamnesis: Dados da anamnese
            kg_data: Dados do knowledge graph

        Returns:
            Dict[str, Any]: Dicionário com o conteúdo de todas as seções geradas

        """
        section_contents: dict[str, Any] = {}

        # Configuração centralizada das seções com ordem de execução
        SECTION_CONFIG = {
            # Seções que não precisam de contexto (executadas primeiro)
            "findings": {
                "prompt_func": self.prompt.get_findings_prompt,
                "schema": SECTION_SCHEMAS["findings"],
                "requires_context": False,
            },
            "deficiencies": {
                "prompt_func": self.prompt.get_deficiencies_prompt,
                "schema": SECTION_SCHEMAS["deficiencies"],
                "requires_context": False,
            },
            # Seções que precisam de contexto (executadas depois)
            "energetics": {
                "prompt_func": self.prompt.get_nutrition_prompt,
                "schema": SECTION_SCHEMAS["energetics"],
                "requires_context": True,
                "section_name": "energetics",
            },
            "constructors": {
                "prompt_func": self.prompt.get_nutrition_prompt,
                "schema": SECTION_SCHEMAS["constructors"],
                "requires_context": True,
                "section_name": "constructors",
            },
            "regulators": {
                "prompt_func": self.prompt.get_nutrition_prompt,
                "schema": SECTION_SCHEMAS["regulators"],
                "requires_context": True,
                "section_name": "regulators",
            },
            "fats": {
                "prompt_func": self.prompt.get_nutrition_prompt,
                "schema": SECTION_SCHEMAS["fats"],
                "requires_context": True,
                "section_name": "fats",
            },
            "foods": {
                "prompt_func": self.prompt.get_nutrition_prompt,
                "schema": SECTION_SCHEMAS["foods"],
                "requires_context": True,
                "section_name": "foods",
            },
            "lifestyle": {
                "prompt_func": self.prompt.get_lifestyle_prompt,
                "schema": SECTION_SCHEMAS["lifestyle"],
                "requires_context": True,
            },
            "supplements": {
                "prompt_func": self.prompt.get_supplements_prompt,
                "schema": SECTION_SCHEMAS["supplements"],
                "requires_context": True,
            },
            "guidelines": {
                "prompt_func": self.prompt.get_guidelines_prompt,
                "schema": SECTION_SCHEMAS["guidelines"],
                "requires_context": True,
            },
            "exams": {
                "prompt_func": self.prompt.get_exams_prompt,
                "schema": SECTION_SCHEMAS["exams"],
                "requires_context": True,
            },
            # Summary será gerado por último
            "summary": {
                "prompt_func": self.prompt.get_summary_prompt,
                "schema": SECTION_SCHEMAS["summary"],
                "requires_context": True,
            },
        }

        # 1. Gera seções sem contexto
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

        # 2. Gera seções com contexto
        for section_name, config in SECTION_CONFIG.items():
            if config["requires_context"] and section_name != "summary":
                await self._generate_section(
                    section_name,
                    config,
                    exam_data,
                    anamnesis,
                    kg_data,
                    section_contents,
                )

        # 3. Gera summary por último com todas as seções já preenchidas
        summary_config = SECTION_CONFIG["summary"]
        await self._generate_section(
            "summary", summary_config, exam_data, anamnesis, kg_data, section_contents
        )

        return section_contents

    @mlflow.trace(name="generate_ionnutri_section", span_type="llm")
    async def _generate_section(
        self,
        section_name: str,
        config: dict,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        section_contents: dict,
    ):
        """Gera uma seção específica usando configuração padronizada.

        Args:
            section_name: Nome da seção a ser gerada
            config: Configuração da seção (prompt_func, schema, etc.)
            exam_data: Dados do exame
            anamnesis: Dados da anamnese
            kg_data: Dados do knowledge graph
            section_contents: Dicionário que será modificado in-place com o conteúdo gerado

        """
        try:
            prompt_func = config["prompt_func"]
            target_schema = config["schema"]

            # Gera prompt com contexto apropriado
            if config["requires_context"]:
                if section_name in [
                    "energetics",
                    "constructors",
                    "regulators",
                    "fats",
                    "foods",
                ]:
                    # Seções nutricionais precisam do contexto e do nome da seção
                    context = {
                        "findings": section_contents.get("findings", {}),
                        "deficiencies": section_contents.get("deficiencies", {}),
                    }
                    system_prompt_content, user_prompt_content = prompt_func(
                        exam_data,
                        anamnesis,
                        kg_data,
                        config.get("section_name", section_name),
                        context,
                    )
                elif section_name == "summary":
                    # Summary precisa de todo o contexto
                    system_prompt_content, user_prompt_content = prompt_func(
                        exam_data, anamnesis, kg_data, section_contents
                    )
                else:
                    # Outras seções precisam do contexto parcial
                    system_prompt_content, user_prompt_content = prompt_func(
                        exam_data, anamnesis, kg_data, section_contents
                    )
            else:
                # Seções sem contexto
                system_prompt_content, user_prompt_content = prompt_func(
                    exam_data, anamnesis, kg_data
                )

            llm_response = await self.llm_service.call_llm(
                user_prompt=user_prompt_content,
                system_prompt=system_prompt_content,
                schema=target_schema,
                temperature=settings.OPENROUTER_TEMPERATURE,
                max_tokens=settings.OPENROUTER_MAX_TOKENS,
            )

            logger.debug(f"LLM response for section '{section_name}': {llm_response}")

            # Armazena como dict usando model_dump() diretamente
            section_contents[section_name] = (
                llm_response.model_dump()
                if hasattr(llm_response, "model_dump")
                else llm_response
            )

        except Exception as e:
            logger.error(f"Error generating section '{section_name}': {str(e)}")
            # Armazena seção vazia em caso de erro
            section_contents[section_name] = {}

    def _build_summary_section(self, summary_data: dict | None) -> SummaryContent:
        """Build the summary section from LLM-generated data.

        Args:
            summary_data (dict | None): Summary data from LLM response.

        Returns:
            SummaryContent: The summary section with content.

        """
        if summary_data and summary_data.get("content"):
            return SummaryContent(content=summary_data.get("content"))
        else:
            return SummaryContent(content="Resumo não disponível.")

    def _build_findings_section(
        self,
        metabolite_info: list[MetaboliteInfo],
        findings_section_data: dict | None,
    ) -> FindingsSection:
        """Constrói a seção de achados a partir dos dados do knowledge graph e do LLM."""
        findings = []
        for metabolite in metabolite_info:
            try:
                normalized_status = self._normalize_status(metabolite.status)
                metabolite_status = self._create_metabolite_status(normalized_status)

                finding = FindingItem(
                    status=normalized_status.name,
                    description=metabolite.description,
                    metabolite=metabolite.name,
                    implications=[],
                    metabolite_status=metabolite_status,
                )
                findings.append(finding)

            except Exception as e:
                logger.warning(
                    f"Error processing metabolite {metabolite.name}: {str(e)}"
                )

        # Trabalha com dict ao invés de objeto Pydantic
        conclusion_text = (
            findings_section_data.get("conclusion")
            if findings_section_data
            else "Conclusão não disponível."
        )
        items = (
            findings_section_data.get("items") if findings_section_data else findings
        )

        return FindingsSection(
            items=items,
            conclusion=conclusion_text,
        )

    def _build_recommendations_section(
        self, section_contents: dict[str, dict]
    ) -> RecommendationsSection:
        """Constrói a seção de recomendações a partir dos dados das seções nutricionais."""
        # Trabalha com dicts ao invés de objetos Pydantic
        energetics_data = section_contents.get("energetics", {})
        constructors_data = section_contents.get("constructors", {})
        regulators_data = section_contents.get("regulators", {})
        fats_data = section_contents.get("fats", {})
        lifestyle_data = section_contents.get("lifestyle", {})
        supplements_data = section_contents.get("supplements", {})
        foods_data = section_contents.get("foods", {})

        energetics_items = energetics_data.get("items", []) if energetics_data else []
        constructors_items = (
            constructors_data.get("items", []) if constructors_data else []
        )
        regulators_items = regulators_data.get("items", []) if regulators_data else []
        fats_items = fats_data.get("items", []) if fats_data else []

        nutritional_recs = NutritionalRecs(
            energetics=energetics_items,
            constructors=constructors_items,
            regulators=regulators_items,
            fats=fats_items,
        )

        return RecommendationsSection(
            nutritional=nutritional_recs,
            lifestyle=lifestyle_data.get("items", []) if lifestyle_data else [],
            supplements=supplements_data.get("items", []) if supplements_data else [],
            foods=foods_data.get("items", []) if foods_data else [],
        )

    def _build_deficiencies_section(
        self, deficiencies_data: dict | None
    ) -> list[DeficiencyItem]:
        """Constrói a lista de deficiências a partir dos dados do LLM."""
        return deficiencies_data.get("items", []) if deficiencies_data else []

    def _build_additional_exams_section(
        self, exams_data: dict | None
    ) -> list[ExamItem]:
        """Constrói a lista de exames adicionais a partir dos dados do LLM."""
        return exams_data.get("items", []) if exams_data else []

    def _build_guidelines_section(self, guidelines_data: dict | None) -> str:
        """Constrói a seção de diretrizes gerais."""
        return (
            guidelines_data.get("content", "Manter acompanhamento nutricional regular.")
            if guidelines_data
            else "Manter acompanhamento nutricional regular."
        )

    def _normalize_status(self, status: str) -> MetaboliteStatusEnum:
        """Normalize metabolite status string to enum value.

        Args:
            status (str): Raw status string from data.

        Returns:
            MetaboliteStatusEnum: Normalized status enum value.

        """
        status_clean = status.lower().strip()
        if status_clean in STATUS_MAPPING:
            return STATUS_MAPPING[status_clean]
        logger.warning(f"Unknown status '{status}', defaulting to 'normal'")
        return MetaboliteStatusEnum.NORMAL

    def _create_metabolite_status(self, status_enum: MetaboliteStatusEnum) -> dict:
        """Create metabolite status dictionary from enum value.

        Args:
            status_enum (MetaboliteStatusEnum): Status enum value.

        Returns:
            dict: Status configuration dictionary with color, classification, etc.

        """
        if status_enum not in METABOLITE_STATUS_CONFIG:
            logger.warning(f"Unknown status enum '{status_enum}', using normal status")
            status_enum = MetaboliteStatusEnum.NORMAL
        config = METABOLITE_STATUS_CONFIG[status_enum]
        return {
            "status": status_enum.name,
            "cor": config["cor"],
            "classificacao": config["classificacao"],
            "score": config["score"],
            "analise": config["analise"],
        }

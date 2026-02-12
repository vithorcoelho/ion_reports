"""OneStage report generation strategy implementation."""

from datetime import datetime

from app.core.logging import logger
from app.services.report.base import BaseReportStrategy


class OneStageReportStrategy(BaseReportStrategy):
    """One-stage report generation strategy."""

    def __init__(self, exam_config, services: dict, alias: str = "production"):
        """Initialize one-stage strategy."""
        super().__init__(exam_config, services)
        self.alias = alias
        logger.debug(f"Initialized OneStageReportStrategy with alias: {alias}")

    async def execute(self, exam_data, anamnesis, kg_data) -> str:
        """Execute one-stage report generation."""
        exam_type = self.exam_config.get_exam_type()
        logger.info(f"Starting one-stage report generation for {exam_type}")

        try:
            # Get knowledge graph data
            logger.debug("Querying knowledge graph for exam data")
            prompt_uri = f"{exam_type}_onestage_complete@{self.alias}"
            prompt_template = self.prompt_registry.load_prompt_by_uri(prompt_uri)

            context = {
                "exam_data": exam_data,
                "anamnesis": anamnesis,
                "kg_data": kg_data,
                "formatting_rules": self.exam_config.get_formatting_config(),
            }

            formatted_prompt = prompt_template.format(**context)

            logger.debug(
                f"Calling LLM for complete report generation with alias: {self.alias}"
            )

            result = await self.llm_service.call_llm(
                user_prompt=formatted_prompt,
                schema=self.exam_config.get_complete_report_schema(),
            )

            markdown_uri = f"{exam_type}_onestage_markdown@{self.alias}"
            markdown_prompt = self.prompt_registry.load_prompt_by_uri(markdown_uri)

            # Calculate birth_date from age
            current_year = datetime.now().year
            birth_year = current_year - anamnesis.personal_data.age
            birth_date = f"{birth_year}-01-01"

            markdown_context = {
                **context,
                "complete_result": result,
                "patient_id": exam_data.patient_id,
                "birth_date": birth_date,
                "weight": anamnesis.personal_data.weight,
                "height": anamnesis.personal_data.height,
            }

            final_report = await self.llm_service.call_llm(
                user_prompt=markdown_prompt.format(**markdown_context), schema=None
            )

            logger.info(
                f"Successfully completed innovative one-stage report generation for {exam_type}"
            )
            return final_report

        except Exception as e:
            logger.error(
                f"Failed to generate one-stage report for {exam_type}: {str(e)}"
            )
            raise

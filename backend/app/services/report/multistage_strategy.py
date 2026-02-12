"""MultiStage report generation strategy implementation."""

from datetime import datetime

from app.core.logging import logger
from app.services.report.base import BaseReportStrategy


class MultiStageReportStrategy(BaseReportStrategy):
    """Multi-stage report generation strategy."""

    def __init__(self, exam_config, services: dict, alias: str = "production"):
        """Initialize multi-stage strategy."""
        super().__init__(exam_config, services)
        self.alias = alias
        logger.debug(f"Initialized MultiStageReportStrategy with alias: {alias}")

    async def execute(self, exam_data, anamnesis, kg_data) -> str:
        """Execute multi-stage report generation."""
        try:
            exam_type = self.exam_config.get_exam_type()
            logger.info(f"Starting multi-stage report generation for {exam_type}")

            sections = self.exam_config.get_section_schemas()
            results: list[str] = []
            context = {
                "exam_data": exam_data,
                "anamnesis": anamnesis,
                "kg_data": kg_data,
            }

            logger.debug(f"Processing {len(sections)} sections for {exam_type}")

            # Sequential processing with context accumulation
            for section_name, schema in sections.items():
                if section_name in ["markdown", "markdown_report"]:
                    continue
                try:
                    logger.debug(f"Processing section: {section_name}")

                    # Using Prompt Registry
                    prompt_uri = f"{exam_type}_multistage_{section_name}@{self.alias}"
                    prompt_template = self.prompt_registry.load_prompt_by_uri(
                        prompt_uri
                    )
                    formatted_prompt = prompt_template.format(
                        **context, previous_sections=results
                    )

                    result = await self.llm_service.call_llm(
                        user_prompt=formatted_prompt, schema=schema
                    )

                    results.append(result)
                    context[f"{section_name}_result"] = result

                    logger.debug(f"Successfully processed section: {section_name}")

                except Exception as e:
                    logger.error(f"Failed to process section {section_name}: {str(e)}")
                    raise

            logger.debug("Generating final markdown report")

            # Calculate birth_date from age
            current_year = datetime.now().year
            birth_year = current_year - anamnesis.personal_data.age
            birth_date = f"{birth_year}-01-01"

            # Using Prompt Registry
            markdown_uri = f"{exam_type}_multistage_markdown@{self.alias}"
            markdown_template = self.prompt_registry.load_prompt_by_uri(markdown_uri)

            # Add patient data for markdown template
            markdown_context = {
                **context,
                "section_results": results,
                "patient_id": exam_data.patient_id,
                "birth_date": birth_date,
                "weight": anamnesis.personal_data.weight,
                "height": anamnesis.personal_data.height,
            }

            markdown_prompt = markdown_template.format(**markdown_context)

            markdown_report = await self.llm_service.call_llm(
                user_prompt=markdown_prompt, schema=None
            )

            logger.info(
                f"Successfully completed multi-stage report generation for {exam_type}"
            )
            return markdown_report

        except Exception as e:
            logger.error(
                f"Failed to generate multi-stage report for {exam_type}: {str(e)}"
            )
            raise

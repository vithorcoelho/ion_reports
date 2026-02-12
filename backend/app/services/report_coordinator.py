"""Report generation coordination service.

This module contains the ReportCoordinator class, which serves as the central
orchestrator for report generation. It manages plugin selection, coordinates
data flow between different layers, and handles error scenarios during the
report generation process.
"""

from pathlib import Path

import mlflow
import yaml

from app.core.config import settings
from app.core.feature_flags import get_feature_flags
from app.core.logging import logger
from app.db.unified_query import Neo4jKnowledgeQuery
from app.domain.report import BaseReport
from app.plugins.base import ReportPlugin
from app.plugins.plugin_registry import get_registered_plugins
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.kg.kg_service import KnowledgeGraphService
from app.services.llm.llm_service import BaseLLMService, OpenRouterLLMService
from app.services.llm.prompt_registry import MLflowPromptRegistry
from app.services.report.strategy_factory import StrategyFactory


class ReportCoordinator:
    """Central orchestrator for report generation with dual implementation support.

    This class supports both plugin-based and strategy pattern implementations
    through feature flags, allowing for easy switching between approaches.
    """

    def __init__(
        self,
        # Plugin-based dependencies
        llm_service: OpenRouterLLMService | None = None,
        knowledge_query: Neo4jKnowledgeQuery | None = None,
        # Strategy pattern dependencies
        strategy_factory: StrategyFactory | None = None,
        kg_service: KnowledgeGraphService | None = None,
        base_llm_service: BaseLLMService | None = None,
        prompt_registry: MLflowPromptRegistry | None = None,
        config_path: str = "strategy_config.yaml",
    ):
        """Initialize the ReportCoordinator."""
        self.config_path = config_path
        flags = get_feature_flags()

        if flags.use_strategy_pattern:
            if (
                strategy_factory is None
                or kg_service is None
                or base_llm_service is None
            ):
                raise ValueError(
                    "StrategyFactory, KnowledgeGraphService, and BaseLLMService are required for strategy mode"
                )
            self._init_strategy_mode(
                strategy_factory, kg_service, base_llm_service, prompt_registry
            )
        else:
            # Default to plugins mode
            if llm_service is None or knowledge_query is None:
                raise ValueError(
                    "OpenRouterLLMService and Neo4jKnowledgeQuery are required for plugin mode"
                )
            self._init_plugin_mode(llm_service, knowledge_query)

    def _init_plugin_mode(
        self, llm_service: OpenRouterLLMService, knowledge_query: Neo4jKnowledgeQuery
    ):
        """Initialize plugin-based implementation."""
        self.llm_service = llm_service
        self.knowledge_query = knowledge_query
        self.plugins: dict[str, ReportPlugin] = get_registered_plugins(llm_service)
        logger.info("ReportCoordinator initialized in PLUGIN mode")

    def _init_strategy_mode(
        self,
        strategy_factory: StrategyFactory,
        kg_service: KnowledgeGraphService,
        base_llm_service: BaseLLMService,
        prompt_registry: MLflowPromptRegistry | None,
    ):
        """Initialize strategy pattern implementation."""
        self.strategy_factory = strategy_factory
        self.kg_service = kg_service
        self.llm_service = base_llm_service
        self.prompt_registry = prompt_registry or MLflowPromptRegistry(
            Path(settings.PROMPT_REGISTRY_PATH)
        )
        self.config = self._load_strategy_config()
        logger.info("ReportCoordinator initialized in STRATEGY mode")

    def _load_strategy_config(self) -> dict:
        """Load the strategy mapping from a YAML configuration file."""
        try:
            with open(self.config_path) as f:
                config = yaml.safe_load(f)
                logger.info(f"Strategy configuration loaded from {self.config_path}")
                return config
        except FileNotFoundError:
            logger.error(f"Strategy config file not found at: {self.config_path}")
            raise
        except yaml.YAMLError as e:
            logger.error(
                f"Error parsing strategy config YAML at {self.config_path}: {e}"
            )
            raise

    @mlflow.trace(name="Report Generator", span_type="workflow")
    async def generate_report(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        exam_type: str = "ionnutri",
    ) -> tuple[str, BaseReport | None]:
        """Generate a medical report using the configured implementation.

        Args:
            exam_data (TNMExamData): The examination data.
            anamnesis (PatientAnamnesis): The patient anamnesis data.
            exam_type (str): The type of exam (e.g., "ionnutri", "vidanova").

        Returns:
            Tuple[str, BaseReport | None]: Returns (markdown_report, structured_report)
                - For plugin mode: (markdown_report, domain_report)
                - For strategy mode: (markdown_report, None)

        Raises:
            ValueError: If the specified plugin is not found (plugin mode).
            KeyError: If the exam_type is not found in the configuration (strategy mode).
            RuntimeError: If any step in the generation process fails.

        """
        flags = get_feature_flags()
        mode = "strategy" if flags.use_strategy_pattern else "plugins"
        logger.info(
            f"Starting report generation for exam type: {exam_type} using {mode} mode"
        )

        if flags.use_strategy_pattern:
            return await self._generate_report_with_strategy(
                exam_data, anamnesis, exam_type
            )
        else:
            # Default to plugins mode
            return await self._generate_report_with_plugins(
                exam_data, anamnesis, exam_type
            )

    async def _generate_report_with_plugins(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, exam_type: str
    ) -> tuple[str, BaseReport]:
        """Generate report using plugin-based implementation."""
        try:
            # 1. Select plugin based on exam_type
            plugin = self.plugins.get(exam_type)
            if not plugin:
                raise ValueError(f"Plugin '{exam_type}' not found.")

            logger.info(f"Executing report generation with plugin: {exam_type}")

            # 2. Query the knowledge graph in a generic way
            try:
                kg_result = await self.knowledge_query.execute_unified_query(
                    exam_data, anamnesis
                )
                logger.info("Knowledge graph query completed")
            except Exception as e:
                logger.exception("Error during knowledge graph query.")
                raise RuntimeError("Knowledge graph query failed.") from e

            if kg_result.error:
                raise RuntimeError(f"Knowledge graph query failed: {kg_result.error}")

            try:
                # Generate both structured report and markdown in one call
                markdown_report, domain_report = await plugin.get_markdown_report(
                    exam_data, anamnesis, kg_result
                )
            except Exception as e:
                logger.exception("Error while building the report with plugin.")
                raise RuntimeError("Report building failed.") from e

            logger.info(f"TNM report generated successfully: {domain_report.report_id}")
            return markdown_report, domain_report

        except Exception as e:
            logger.exception(
                f"Error while building the report with plugin '{exam_type}'."
            )
            raise RuntimeError(f"Error generating report: {e}") from e

    async def _generate_report_with_strategy(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, exam_type: str
    ) -> tuple[str, BaseReport | None]:
        """Generate report using strategy pattern implementation."""
        try:
            kg_data = await self.kg_service.get_knowledge_data(exam_data, anamnesis)
            strategy_type = self.config["strategies"][exam_type]["type"]
            logger.info(
                f"Selected strategy '{strategy_type}' for exam_type '{exam_type}'."
            )

            services = {
                "llm_service": self.llm_service,
                "prompt_registry": self.prompt_registry,
            }
            strategy = self.strategy_factory.create_strategy(
                exam_type, strategy_type, services
            )

            # Execute the strategy to get the final report
            markdown_report = await strategy.execute(exam_data, anamnesis, kg_data)
            logger.info(f"Report for exam_type '{exam_type}' generated successfully.")

            # Return only markdown report for strategy mode (no structured report)
            return markdown_report, None

        except KeyError as err:
            logger.error(
                f"Configuration for exam_type '{exam_type}' not found in strategy_config.yaml."
            )
            raise KeyError(
                f"Invalid exam_type: '{exam_type}'. No configuration found."
            ) from err
        except Exception as e:
            logger.exception(
                f"An unexpected error occurred during report generation for '{exam_type}'."
            )
            raise RuntimeError(f"Failed to generate report for '{exam_type}'.") from e

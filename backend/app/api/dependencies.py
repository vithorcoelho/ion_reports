"""FastAPI dependency injection for service instances.

This module provides cached singleton instances of core services and clients
used throughout the API. It uses functools.lru_cache to ensure that expensive
resources like database connections and service initializations are reused.
"""

from functools import lru_cache
from pathlib import Path

from app.core.config import settings
from app.db.neo4j_client import Neo4jClient
from app.db.report_job_repository import ReportJobRepository
from app.db.unified_query import Neo4jKnowledgeQuery
from app.services.kg.kg_service import KnowledgeGraphService
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.llm.prompt_evaluator import MLflowPromptEvaluator
from app.services.llm.prompt_registry import MLflowPromptRegistry
from app.services.report.strategy_factory import StrategyFactory
from app.services.report_coordinator import ReportCoordinator


# Instâncias cache (singleton) para os serviços e clientes
@lru_cache
def get_neo4j_client():
    """Get singleton Neo4j client instance.

    Returns:
        Neo4jClient: Cached Neo4j client instance.

    """
    return Neo4jClient()


@lru_cache
def get_knowledge_query():
    """Get singleton knowledge query service instance.

    Returns:
        Neo4jKnowledgeQuery: Cached knowledge query service.

    """
    return Neo4jKnowledgeQuery(get_neo4j_client())


@lru_cache
def get_kg_service():
    """Get singleton knowledge graph service instance.

    Returns:
        KnowledgeGraphService: Cached knowledge graph service.

    """
    return KnowledgeGraphService(get_neo4j_client())


@lru_cache
def get_strategy_factory():
    """Get singleton strategy factory instance.

    Returns:
        StrategyFactory: Cached strategy factory.

    """
    return StrategyFactory()


@lru_cache
def get_llm_service():
    """Get singleton LLM service instance.

    Returns:
        OpenRouterLLMService: Cached LLM service configured with OpenRouter settings.

    """
    return OpenRouterLLMService(
        model_name=settings.OPENROUTER_MODEL_NAME,
        model_id=settings.OPENROUTER_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        router_api=settings.OPENROUTER_API_BASE,
    )


@lru_cache
def get_prompt_registry() -> MLflowPromptRegistry:
    """Get singleton prompt registry instance.

    Returns:
        MLflowPromptRegistry: Prompt registry instance for strategy mode.

    """
    return MLflowPromptRegistry(Path(settings.PROMPT_REGISTRY_PATH))


@lru_cache
def get_report_job_repository() -> ReportJobRepository:
    """Get singleton repository for async report jobs."""
    return ReportJobRepository.from_settings()


def get_coordinator() -> ReportCoordinator:
    """Get report coordinator instance based on current feature flags.

    Returns:
        ReportCoordinator: Report coordinator with appropriate dependencies based on current mode.

    """
    return ReportCoordinator(
        # Plugin mode dependencies
        llm_service=get_llm_service(),
        knowledge_query=get_knowledge_query(),
        # Strategy mode dependencies
        strategy_factory=get_strategy_factory(),
        kg_service=get_kg_service(),
        base_llm_service=get_llm_service(),
        prompt_registry=get_prompt_registry(),
        config_path="strategy_config.yaml",
    )


@lru_cache
def get_prompt_evaluator():
    """Get singleton prompt evaluator instance.

    Returns:
        MLflowPromptEvaluator: Cached prompt evaluator instance.

    """
    return MLflowPromptEvaluator(experiment_name="medical-prompts-v1")

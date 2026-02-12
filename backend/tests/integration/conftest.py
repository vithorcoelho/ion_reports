"""Test configuration and fixtures for integration tests.

This module provides specific fixtures and configuration for integration tests,
including real service connections, test data, and integration test setup.
"""

import asyncio

import docker
import pytest
from docker.errors import DockerException
from testcontainers.neo4j import Neo4jContainer

from app.core import config
from app.core.config import settings
from app.db.neo4j_client import Neo4jClient
from app.services.kg.kg_service import KnowledgeGraphService
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report.strategy_factory import StrategyFactory
from app.services.report_coordinator import ReportCoordinator


@pytest.fixture
def neo4j_client(neo4j_container):
    """Use in tests that require a connection to the database."""
    return Neo4jClient()


@pytest.fixture(scope="function")
def neo4j_container(monkeypatch):
    """Create a temporary Neo4j container to be used in tests.

    - Checks if Docker is available; if not, skips the test.
    - Starts a container with the 'neo4j:5.12' image.
    - Sets connection configurations  (URI, user, and password) using monkeypatch.
    - Ensures the container is terminated after the test.
    """
    try:
        docker.from_env().ping()
    except DockerException as e:
        pytest.skip(f"Docker is not available: {str(e)}")

    with Neo4jContainer("neo4j:5.12") as neo4j:
        bolt_url = neo4j.get_connection_url()

        monkeypatch.setattr(config.settings, "NEO4J_URI", bolt_url)
        monkeypatch.setattr(config.settings, "NEO4J_USER", "neo4j")
        monkeypatch.setattr(config.settings, "NEO4J_PASSWORD", "password")

        client = Neo4jClient()
        cypher_query = """
            MERGE (m:METABOLITE {name: "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]"})
            SET m.definition = "O 1-estearoil-lisofosfatidilcolina (1-SLPC) é uma molécula que faz parte dos fosfolipídios...",
                m.reference_range_min = 0.8,
                m.reference_range_max = 1.2
        """
        asyncio.run(client.execute_query(cypher_query))
        yield neo4j


@pytest.fixture
def real_llm_service():
    """Fixture para LLM service real (OpenRouter) para testes de integração."""
    return OpenRouterLLMService(
        model_name=settings.OPENROUTER_MODEL_NAME,
        model_id=settings.OPENROUTER_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        router_api=settings.OPENROUTER_API_BASE,
    )


@pytest.fixture
def real_kg_service(neo4j_client):
    """Fixture para Knowledge Graph service real para testes de integração."""
    return KnowledgeGraphService(neo4j_client)


@pytest.fixture
def strategy_factory():
    """Fixture para StrategyFactory."""
    return StrategyFactory()


@pytest.fixture
def real_report_coordinator(
    mocker, strategy_factory, real_kg_service, real_llm_service
):
    """Fixture para ReportCoordinator com todos os serviços reais."""
    # Mock feature flags to use strategy mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = True

    return ReportCoordinator(
        strategy_factory=strategy_factory,
        kg_service=real_kg_service,
        base_llm_service=real_llm_service,
        prompt_registry=None,
        config_path="strategy_config.yaml",
    )

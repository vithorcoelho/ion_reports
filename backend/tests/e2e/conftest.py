"""Test configuration and fixtures for end-to-end tests.

This module provides specific fixtures and configuration for E2E tests,
including real service connections, test data, and complete workflow testing.
"""

import asyncio
import pathlib
from datetime import date

import docker
import pytest
from docker.errors import DockerException
from testcontainers.neo4j import Neo4jContainer

from app.api.dependencies import get_coordinator
from app.core import config
from app.core.config import settings
from app.db.knowledge_graph_builder import KnowledgeGraphBuilder
from app.db.neo4j_client import Neo4jClient
from app.db.unified_query import Neo4jKnowledgeQuery
from app.main import app
from app.schemas.exam import Metabolite, TNMExamData
from app.schemas.patient_anamnesis import (
    AlcoholConsumption,
    ContextFactors,
    IonNutriAnamnesis,
    Medication,
    PersonalData,
    PhysicalActivity,
    Sleep,
)
from app.services.kg.kg_service import KnowledgeGraphService
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report.strategy_factory import StrategyFactory
from app.services.report_coordinator import ReportCoordinator


@pytest.fixture(scope="function")
def neo4j_container(monkeypatch, tmp_path, ontology_json_path):
    """Pytest fixture that initializes a temporary Neo4j container for testing.

    This fixture:
    - Checks if Docker is available in the environment; otherwise, the test is skipped.
    - Creates and starts a Neo4j container with the 'neo4j:5.12' image.
    - Dynamically sets connection configurations (URI, user, password) using monkeypatch.
    - Initializes the client and the knowledge graph builder.
    - Creates constraints in the database and loads an ontology from a JSON file.
    - Ensures the container is stopped at the end of the test.

    Parameters
    ----------
    monkeypatch : _pytest.monkeypatch.MonkeyPatch
        Used to temporarily override application settings.
    tmp_path : pathlib.Path
        Temporary directory automatically provided by pytest.
    ontology_json_path : pathlib.Path
        Path to the ontology JSON file to be loaded into the database.

    Returns
    -------
    Neo4jContainer
        Instance of the running Neo4j container, available for use during tests.

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
        kg_builder = KnowledgeGraphBuilder(client)
        asyncio.run(kg_builder.create_constraints())
        asyncio.run(kg_builder.load_ontology(str(ontology_json_path)))

        yield neo4j


@pytest.fixture
def neo4j_client(neo4j_container):
    """Use in tests that require a connection to the database."""
    return Neo4jClient()


@pytest.fixture
def query_unified(neo4j_client: Neo4jClient):
    """Return an instance of Neo4jKnowledgeQuery client."""
    return Neo4jKnowledgeQuery(neo4j_client)


@pytest.fixture
def report_coordinator_e2e(mocker, neo4j_client: Neo4jClient):
    """Retorna uma instância real do ReportCoordinator com Strategy Pattern."""
    llm_service = OpenRouterLLMService(
        model_name=settings.OPENROUTER_MODEL_NAME,
        model_id=settings.OPENROUTER_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        router_api=settings.OPENROUTER_API_BASE,
    )
    kg_service = KnowledgeGraphService(neo4j_client)
    strategy_factory = StrategyFactory()

    # Mock feature flags to use strategy mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = True

    return ReportCoordinator(
        strategy_factory=strategy_factory,
        kg_service=kg_service,
        base_llm_service=llm_service,
        config_path="strategy_config.yaml",
    )


@pytest.fixture(autouse=True)
def setup_dependency_override(report_coordinator_e2e):
    """Auto-setup dependency override for all tests in this class."""
    app.dependency_overrides[get_coordinator] = lambda: report_coordinator_e2e
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def mock_exam_data():
    """Create example data for tests e2e."""
    return TNMExamData(
        patient_id="PAT001",
        exam_date=date.today(),
        metabolites=[
            Metabolite(
                name="1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                # value=Decimal("0.07"),
                value=0.07,
            ),
        ],
    )


@pytest.fixture
def mock_anamnesis():
    """Create example anamnesis data for tests e2e."""
    return IonNutriAnamnesis(
        patient_id="PAT001",
        anamnesis_type="ionnutri",
        date=date.today(),
        objective="Melhorar saúde metabólica",
        personal_data=PersonalData(
            age=35, gender="F", weight=65.0, height=1.65, bmi=23.9
        ),
        context_factors=ContextFactors(
            medical_history=["hipertensão leve"],
            intolerances=["lactose"],
            physical_activity=PhysicalActivity(
                type="caminhada", frequency="3", intensity="moderada"
            ),
            sleep=Sleep(quality="boa", hours=8, issues=[]),
            alcohol_consumption=AlcoholConsumption(frequency="2", amount="1 taça"),
            medications=[Medication(name="Losartana", frequency="1x/dia", dosage=None)],
            stress_level="moderado",
        ),
        family_history={"pai": "hipertensão", "mãe": "diabetes tipo 2"},
        environmental_exposure={"agrotóxicos": "baixa", "metais_pesados": "nenhuma"},
    )


@pytest.fixture(scope="session")
def ontology_json_path():
    """Return the path to the existing ontology.json file."""
    return pathlib.Path(__file__).parent / "data" / "ontology.json"

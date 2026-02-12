"""Test configuration and fixtures for API tests.

This module provides specific fixtures and configuration for API endpoint tests,
including mock services, test data, and API client setup.
"""

from datetime import datetime

import pytest

from app.api.dependencies import (
    get_coordinator,
    get_knowledge_query,
    get_llm_service,
    get_neo4j_client,
)
from app.db.unified_query import Neo4jKnowledgeQuery
from app.domain.kg_result import KGResult, MetaboliteInfo, ReferenceRange
from app.domain.report import (
    FindingsSection,
    IonNutriReport,
    NutritionalRecs,
    RecommendationsSection,
    SummaryContent,
)
from app.main import app
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report_coordinator import ReportCoordinator


@pytest.fixture
def mock_datetime(mocker):
    """Fixture que mocka datetime.now() para testes determinísticos."""
    fixed_time = datetime(2023, 10, 1, 12, 0, 0)
    return fixed_time


@pytest.fixture
def mock_uuid(mocker):
    """Fixture que mocka uuid.uuid4() para testes determinísticos."""
    mock_uuid = mocker.patch("uuid.uuid4")
    mock_uuid.return_value = "test-uuid-123"
    return mock_uuid


@pytest.fixture
def mock_kg_service(mocker):
    """Fixture para sobrescrever as dependências relacionadas ao Knowledge Graph.

    Isso inclui mockar o Neo4jClient e o Neo4jKnowledgeQuery.
    """
    mock_neo4j_client = mocker.patch(
        "app.db.neo4j_client.Neo4jClient",
        autospec=True,  # Garante que o mock se comporta como a classe real, ajudando a detectar erros de interface
    )

    mock_kg_service = mocker.MagicMock(spec=Neo4jKnowledgeQuery)

    # Sobrescreve as funções provedoras de dependência no FastAPI.
    app.dependency_overrides[get_neo4j_client] = lambda: mock_neo4j_client.return_value
    app.dependency_overrides[get_knowledge_query] = lambda: mock_kg_service

    yield mock_kg_service


@pytest.fixture
def mock_llm_service(mocker):
    """Fixture para sobrescrever a dependência do LLM Service.

    Configura um mock para simular o OpenRouterLLMService.
    """
    mock_llm_service = mocker.Mock(spec=OpenRouterLLMService)

    # Configura o comportamento básico do mock
    mock_llm_service.call_llm.return_value = {"content": "Mocked LLM content"}

    app.dependency_overrides[get_llm_service] = lambda: mock_llm_service
    yield mock_llm_service


@pytest.fixture
def mock_report(mocker):
    """Fixture para sobrescrever as dependências relacionadas ao Knowledge Graph.

    Isso inclui mockar o Neo4jClient e o Neo4jKnowledgeQuery.
    """
    mock_report = mocker.Mock(spec=ReportCoordinator)

    # Create a mock plugin and configure plugins dict
    mock_plugin = mocker.Mock()

    # Configure plugins attribute with default plugins
    mock_plugins = {
        "ionnutri": mock_plugin,
        "vidanova": mock_plugin,
    }
    mock_report.plugins = mock_plugins

    # Configure knowledge_query mock
    mock_knowledge_query = mocker.Mock()
    mock_knowledge_query.execute_unified_query = mocker.AsyncMock()
    mock_report.knowledge_query = mock_knowledge_query

    # Configure generate_report to return tuple (markdown, domain_report)
    async def mock_generate_report(exam_data, anamnesis, exam_type):
        return ("# Mock Report\n\nThis is a mock report content.", None)

    mock_report.generate_report = mocker.AsyncMock(side_effect=mock_generate_report)

    app.dependency_overrides[get_coordinator] = lambda: mock_report

    yield mock_report


@pytest.fixture
def standard_success_tnm_report(mock_uuid, mock_datetime):
    """Provide a standard TNMReport object representing a successful generation.

    Esse objeto pode ser usado para definir o return_value do mock_report.
    """
    return IonNutriReport(
        report_id=f"TNM_P413_{mock_uuid.return_value}",
        patient_id="PAT001",
        anamnesis_id=f"ana_{mock_uuid.return_value}",
        exam_id=f"exam_{mock_uuid.return_value}",
        version="1.0",
        timestamp=mock_datetime,
        summary=SummaryContent(content="Default summary."),
        findings=FindingsSection(items=[], conclusion="Default finding conclusion"),
        recommendations=RecommendationsSection(
            nutritional=NutritionalRecs(
                energetics=[], constructors=[], regulators=[], fats=[]
            ),
            lifestyle=[],
            supplements=[],
        ),
        deficiencies=[],
        general_guidelines="Default guideline",
        additional_exams=[],
    )


@pytest.fixture
def mock_tnm_result(mock_kg_service):
    """Fixture que configura o comportamento padrão do mock do TNM Service."""
    mock_kg_service.execute_unified_query.return_value = KGResult(
        metabolite_info=[
            MetaboliteInfo(
                name="Glicose",
                value=90,
                status="normal",
                reference_range=ReferenceRange(min=7, max=99),
            ),
        ],
        manifestations=[],
        recommended_interventions=[],
        foods=[],
        supplements=[],
        pathway_impacts=[],
        scientific_evidence=[],
        contraindications=[],
        error=None,
    )
    yield


@pytest.fixture
def llm_service_success_response(mock_llm_service):
    """Fixture that sets up the default (success) behavior for the mock LLM Service."""
    mock_llm_service.call_llm.return_value = {"content": ""}


@pytest.fixture
def setup_mock_tnm_report_success(mocker, mock_report, standard_success_tnm_report):
    """Fixture that sets up the default (success) behavior for the mock TNM Service to generate a report.

    This fixture receives the mock_report from conftest.py and configures its behavior.
    """
    # Configure generate_report to return tuple (markdown, domain_report)
    mock_markdown = "# Mock Medical Report\n\nTest report content with PAT001"
    mock_report.generate_report = mocker.AsyncMock(return_value=(mock_markdown, None))

    # Configure the plugin's get_markdown_report method for backward compatibility if needed
    for plugin in mock_report.plugins.values():
        plugin.get_markdown_report = mocker.AsyncMock(
            return_value=(mock_markdown, standard_success_tnm_report)
        )

    # Configure knowledge_query to return a successful KGResult
    successful_kg_result = KGResult(metabolite_info=[], error=None)
    mock_report.knowledge_query.execute_unified_query.return_value = (
        successful_kg_result
    )

    yield mock_report


@pytest.fixture
def setup_all_services_for_success(
    mock_tnm_result, llm_service_success_response, setup_mock_tnm_report_success
):
    """Configure the mocks for KG, LLM, and TNM for standard successful behavior."""
    yield

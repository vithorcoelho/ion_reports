"""Test configuration and fixtures for service tests."""

import pytest

from app.domain.kg_result import (
    Contraindication,
    Intervention,
    KGResult,
    Manifestation,
    MetaboliteInfo,
    PathwayImpact,
    RecommendedFood,
    RecommendedSupplement,
    ReferenceRange,
    ScientificEvidence,
    SupplementDosage,
)
from app.domain.report import FindingsSection, MarkdownReport, SummaryContent
from app.services.kg.kg_service import KnowledgeGraphService
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report.multistage_strategy import MultiStageReportStrategy
from app.services.report.onestage_strategy import OneStageReportStrategy
from app.services.report_coordinator import ReportCoordinator


@pytest.fixture
def llm_instance():
    """Return default instance of OpenRouterLLMService used in tests."""
    return OpenRouterLLMService(
        model_name="gemini",
        model_id="gemini-2.5",
        api_key="fake",  # pragma: allowlist secret
        router_api="http://url",
    )


@pytest.fixture
def llm_instance_valid_key():
    """Version with a test key for more semantic tests."""
    return OpenRouterLLMService(
        model_name="gemini",
        model_id="gemini-2.5",
        api_key="key",  # pragma: allowlist secret
        router_api="http://url",
    )


@pytest.fixture
def mock_llm_success_response(mocker):
    """Mock a successful response from the OpenAI API using pytest-mock."""
    mock_response = mocker.Mock()
    mock_message = mocker.Mock()
    mock_message.content = "resposta mock"
    mock_choice = mocker.Mock()
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]

    mock_openai = mocker.patch("app.services.llm_service.OpenAI")
    mock_openai.return_value.chat.completions.create.return_value = mock_response
    return mock_openai


@pytest.fixture
def mock_llm_failure_response(mocker):
    """Mock an exception raised when calling the OpenAI API using pytest-mock."""
    mock_openai = mocker.patch("app.services.llm_service.OpenAI")
    mock_openai.return_value.chat.completions.create.side_effect = Exception(
        "Erro na API"
    )
    return mock_openai


@pytest.fixture
def mock_kg_data():
    """Return a KGResult with mock data."""
    return KGResult.from_kg_data(
        {
            "metabolite_info": [
                {
                    "name": "Carnitina",
                    "status": "baixo",
                    "value": 25.0,
                    "reference_range_min": 30,
                    "reference_range_max": 60,
                }
            ]
        }
    )


@pytest.fixture
def mock_empty_kg_data():
    """Return a TNMResult with all fields empty."""
    return KGResult()


@pytest.fixture
def tnm_service_for_data_inclusion(
    mocker, mock_llm_service_for_data_inclusion, mock_kg_result_for_data_inclusion
):
    """ReportCoordinator configured with specific mocks for the data inclusion test."""
    mock_knowledge_query = mocker.Mock()
    mock_knowledge_query.execute_unified_query = mocker.AsyncMock(
        return_value=mock_kg_result_for_data_inclusion
    )

    # Mock feature flags to use plugins mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = False

    service = ReportCoordinator(
        llm_service=mock_llm_service_for_data_inclusion,
        knowledge_query=mock_knowledge_query,
    )
    return service, mock_llm_service_for_data_inclusion


@pytest.fixture
def mock_llm_service_for_data_inclusion(mocker):
    """Mock for OpenRouterLLMService with simple behavior for the data inclusion test."""
    mock_llm = mocker.Mock()

    # Note: generate_prompt is not available in OpenRouterLLMService
    mock_llm.call_llm = mocker.Mock(
        return_value={"content": "Mock LLM response for data inclusion"}
    )

    # mock_llm.parse_response is not called directly by ReportCoordinator, so it does not need to be mocked here.
    return mock_llm


@pytest.fixture
def mock_kg_result_for_data_inclusion():
    """Return a specific TNMResult for the data inclusion test."""
    return KGResult(
        metabolite_info=[
            MetaboliteInfo(
                name="L-carnitina",
                value=25.0,
                status="low",
                description="Metabólito L-carnitina apresenta status low, indicando possíveis deficiências",
                reference_range=ReferenceRange(min=30.0, max=100.0),
            )
        ],
        manifestations=[
            Manifestation(metabolite="L-carnitina", status="low", description="Fadiga")
        ],
        recommended_interventions=[
            Intervention(
                metabolite="L-carnitina",
                type="Nutricional",
                description="Aumentar ingestão de carnes",
            )
        ],
        foods=[RecommendedFood(metabolite="L-carnitina", name="Salmão")],
        supplements=[
            RecommendedSupplement(
                metabolite="L-carnitina",
                name="L-Carnitina",
                active_composition="L-Carnitina",
                dosage=SupplementDosage(minimum=500, maximum=1000, unit="mg"),
            )
        ],
        pathway_impacts=[
            PathwayImpact(
                metabolite="L-carnitina",
                name="Via energética",
                clinical_importance="Alta",
            )
        ],
        scientific_evidence=[
            ScientificEvidence(
                metabolite="L-carnitina", title="Estudo sobre L-carnitina"
            )
        ],
        contraindications=[
            Contraindication(
                intervention="Intervenção Y",
                metabolite="L-carnitina",
                reason="Alergia",
                type="medical_history",
            )
        ],
    )


@pytest.fixture
def mock_neo4j_client(mocker):
    """Mock Neo4j client for testing."""
    return mocker.MagicMock()


@pytest.fixture
def kg_instance(mock_neo4j_client, mock_knowledge_query_configured):
    """Create a KnowledgeGraphService instance for testing."""
    kg_service = KnowledgeGraphService(mock_neo4j_client)
    kg_service.kg_query = mock_knowledge_query_configured
    return kg_service


@pytest.fixture
def mock_exam_config(mocker):
    """Mock exam configuration for strategy testing."""
    mock_config = mocker.Mock()
    mock_config.get_exam_type.return_value = "ionnutri"
    mock_config.get_section_schemas.return_value = {
        "summary": SummaryContent,
        "findings": FindingsSection,
        "markdown_report": MarkdownReport,
    }
    mock_config.get_formatting_config.return_value = {
        "style": "Technical style",
        "format": "Markdown",
    }
    mock_config.get_complete_report_schema.return_value = MarkdownReport
    return mock_config


@pytest.fixture
def mock_prompt_registry(mocker):
    """Mock prompt registry for strategy testing."""
    mock_registry = mocker.Mock()

    def mock_load_prompt_by_uri(uri):
        mock_template = mocker.Mock()
        mock_template.format.return_value = f"Mock prompt for {uri}"
        return mock_template

    mock_registry.load_prompt_by_uri.side_effect = mock_load_prompt_by_uri
    return mock_registry


@pytest.fixture
def mock_llm_service_for_strategies(mocker):
    """Mock LLM service specifically for strategy testing."""
    mock_llm = mocker.Mock()

    async def mock_call_llm(user_prompt, schema=None, **kwargs):
        if schema is None:
            return "# Relatório Mock\n\nConteúdo gerado pelo LLM"
        return mocker.Mock(content=f"Mock result for {schema.__name__}")

    mock_llm.call_llm = mocker.AsyncMock(side_effect=mock_call_llm)
    return mock_llm


@pytest.fixture
def mock_kg_service_for_strategies(mocker):
    """Mock KG service specifically for strategy testing."""
    mock_kg = mocker.Mock()

    async def mock_get_knowledge_data(exam_data, anamnesis):
        # Return mock KG result
        from app.domain.kg_result import KGResult

        return KGResult()

    mock_kg.get_knowledge_data = mocker.AsyncMock(side_effect=mock_get_knowledge_data)
    return mock_kg


@pytest.fixture
def mock_services(
    mock_llm_service_for_strategies,
    mock_prompt_registry,
    mock_kg_service_for_strategies,
):
    """Mock services dictionary for strategy testing."""
    return {
        "llm_service": mock_llm_service_for_strategies,
        "prompt_registry": mock_prompt_registry,
        "kg": mock_kg_service_for_strategies,
    }


@pytest.fixture
def multistage_strategy(mock_exam_config, mock_services):
    """MultiStage strategy fixture."""
    return MultiStageReportStrategy(mock_exam_config, mock_services)


@pytest.fixture
def onestage_strategy(mock_exam_config, mock_services):
    """OneStage strategy fixture."""
    return OneStageReportStrategy(mock_exam_config, mock_services)


@pytest.fixture
def ionnutri_sections():
    """Return expected section order for IonNutri (explicit, not dynamic)."""
    return [
        "summary",
        "findings",
        "energetics",
        "constructors",
        "regulators",
        "fats",
        "lifestyle",
        "supplements",
        "foods",
        "deficiencies",
        "guidelines",
        "exams",
    ]


@pytest.fixture
def vidanova_sections():
    """Return expected section order for VidaNova (explicit, not dynamic)."""
    return ["summary", "findings", "diet_suggestions", "supplements", "training"]

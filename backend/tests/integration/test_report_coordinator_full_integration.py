"""Full integration tests for ReportCoordinator with all services."""

import pytest

from app.core.config import settings
from app.db.unified_query import Neo4jKnowledgeQuery
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report_coordinator import ReportCoordinator


@pytest.mark.integration
@pytest.mark.llm
@pytest.mark.neo4j
@pytest.mark.asyncio
async def test_report_coordinator_with_real_neo4j_and_real_llm(
    mocker,
    neo4j_client,
    sample_exam_data: TNMExamData,
    sample_anamnesis: PatientAnamnesis,
):
    """Integração completa com LLM real e Neo4j real.

    Objetivos:
    - Verificar geração do relatório completo com dados reais de grafo e conteúdo real do LLM.
    - Validar a estrutura e consistência das seções geradas.
    """
    real_llm_service = OpenRouterLLMService(
        model_name=settings.OPENROUTER_MODEL_NAME,
        model_id=settings.OPENROUTER_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        router_api=settings.OPENROUTER_API_BASE,
    )

    # For plugins mode, we need Neo4jKnowledgeQuery, not KnowledgeGraphService
    real_knowledge_query = Neo4jKnowledgeQuery(neo4j_client)

    # Mock feature flags to use plugins mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = False

    report_coordinator = ReportCoordinator(
        llm_service=real_llm_service,
        knowledge_query=real_knowledge_query,
    )

    result = await report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert len(markdown_report) > 100, (
        f"Relatório deve ter conteúdo substancial (atual: {len(markdown_report)})"
    )
    assert sample_exam_data.patient_id in markdown_report, "Deve conter ID do paciente"
    assert domain_report is not None, (
        "Plugin mode deve retornar domain_report estruturado"
    )
    assert hasattr(domain_report, "report_id"), "Domain report deve ter report_id"

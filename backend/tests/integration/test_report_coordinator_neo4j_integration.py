"""Integration tests for ReportCoordinator with Neo4j database."""

import pytest

from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.kg.kg_service import KnowledgeGraphService
from app.services.report.strategy_factory import StrategyFactory
from app.services.report_coordinator import ReportCoordinator


@pytest.mark.integration
@pytest.mark.neo4j
@pytest.mark.asyncio
async def test_report_coordinator_with_real_neo4j(
    mocker,
    neo4j_client,
    sample_exam_data: TNMExamData,
    sample_anamnesis: PatientAnamnesis,
    mock_llm_service_configured,
):
    """Integração completa entre TNMService e Neo4j real (Testcontainers ou local).

    Objetivos:
    - Validar construção e execução das queries Cypher
    - Verificar mapeamento correto dos dados para domínio clínico
    - Garantir integração fluida com LLM mockado
    """
    # Neo4j real
    real_kg_service = KnowledgeGraphService(neo4j_client)
    strategy_factory = StrategyFactory()

    # Serviço principal com Neo4j real + LLM fake
    # Mock feature flags to use strategy mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = True

    report_coordinator = ReportCoordinator(
        strategy_factory=strategy_factory,
        kg_service=real_kg_service,
        base_llm_service=mock_llm_service_configured,
        config_path="strategy_config.yaml",
    )

    # Gera relatório com dados reais de grafo
    result = await report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert len(markdown_report) > 100, "Relatório deve ter conteúdo substancial"
    assert sample_exam_data.patient_id in markdown_report, "Deve conter ID do paciente"
    assert domain_report is None, "Strategy mode deve retornar None para domain_report"

    assert "resumo gerado pelo llm para o paciente." in markdown_report.lower()

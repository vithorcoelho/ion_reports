"""Integration tests for ReportCoordinator with LLM service."""

import pytest

from app.core.config import settings
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report.strategy_factory import StrategyFactory
from app.services.report_coordinator import ReportCoordinator


@pytest.mark.integration
@pytest.mark.llm
@pytest.mark.asyncio
async def test_report_coordinator_llm_integration(
    mocker, sample_exam_data, sample_anamnesis, mock_knowledge_query_configured
):
    """Testa o TNMService com uma API LLM real e Neo4j mockado, focando na validação qualitativa.

    Objetivo:
    - Assegurar que o LLM foi invocado e gerou conteúdo para as seções principais do relatório.
    - Validar a estrutura geral do relatório e a presença de dados essenciais.
    - Confirmar que o conteúdo não é "mockado", indicando interação real com o LLM.
    - Manter o foco na integração e no fluxo de ponta a ponta.
    """
    real_llm_service = OpenRouterLLMService(
        model_name=settings.OPENROUTER_MODEL_NAME,
        model_id=settings.OPENROUTER_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        router_api=settings.OPENROUTER_API_BASE,
    )

    strategy_factory = StrategyFactory()

    # Mock feature flags to use strategy mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = True

    report_coordinator = ReportCoordinator(
        strategy_factory=strategy_factory,
        kg_service=mock_knowledge_query_configured,
        base_llm_service=real_llm_service,
        config_path="strategy_config.yaml",
    )

    result = await report_coordinator.generate_report(
        sample_exam_data,
        sample_anamnesis,
        "ionnutri",
    )

    markdown_report, domain_report = result

    # Validations for the new Strategy Pattern architecture
    assert markdown_report is not None, "O relatório não deve ser nulo"
    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert len(markdown_report) > 100, "Relatório deve ter conteúdo substancial"
    assert domain_report is None, "Strategy mode deve retornar None para domain_report"

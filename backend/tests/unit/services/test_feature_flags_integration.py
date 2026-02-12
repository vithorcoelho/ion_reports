"""Integration tests for feature flags with ReportCoordinator."""

import pytest

from app.core.feature_flags import FeatureFlags
from app.services.report_coordinator import ReportCoordinator


@pytest.mark.asyncio
async def test_plugins_mode_behavior(
    mocker,
    mock_llm_service_configured,
    mock_knowledge_query_configured,
    sample_exam_data,
    sample_anamnesis,
):
    """Test that plugins mode initializes correctly and returns domain report."""
    # Mock feature flags to use plugins mode
    mocker.patch(
        "app.services.report_coordinator.get_feature_flags",
        return_value=FeatureFlags(use_strategy_pattern=False),
    )

    coordinator = ReportCoordinator(
        llm_service=mock_llm_service_configured,
        knowledge_query=mock_knowledge_query_configured,
    )

    # Verify plugins mode initialization
    assert hasattr(coordinator, "plugins")
    assert hasattr(coordinator, "llm_service")
    assert hasattr(coordinator, "knowledge_query")
    assert not hasattr(coordinator, "strategy_factory")
    assert not hasattr(coordinator, "kg_service")

    result = await coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    # Verify plugins mode returns both markdown and domain report
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 100
    assert domain_report is not None
    assert hasattr(domain_report, "report_id")


@pytest.mark.asyncio
async def test_strategy_mode_behavior(
    mocker,
    strategy_factory,
    mock_llm_service_configured,
    mock_kg_service_for_strategies,
    sample_exam_data,
    sample_anamnesis,
):
    """Test that strategy mode initializes correctly and returns None for domain report."""
    # Mock feature flags to use strategy mode
    mocker.patch(
        "app.services.report_coordinator.get_feature_flags",
        return_value=FeatureFlags(use_strategy_pattern=True),
    )

    coordinator = ReportCoordinator(
        strategy_factory=strategy_factory,
        kg_service=mock_kg_service_for_strategies,
        base_llm_service=mock_llm_service_configured,
        prompt_registry=None,
        config_path="strategy_config.yaml",
    )

    # Verify strategy mode initialization
    assert hasattr(coordinator, "strategy_factory")
    assert hasattr(coordinator, "kg_service")
    assert hasattr(coordinator, "llm_service")
    assert hasattr(coordinator, "config")
    assert not hasattr(coordinator, "plugins")
    assert not hasattr(coordinator, "knowledge_query")

    result = await coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    # Verify strategy mode returns markdown and None for domain report
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 100
    assert domain_report is None

"""Integration tests for ReportCoordinator using the Strategy Pattern implementation."""

import pytest

from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.report.multistage_strategy import MultiStageReportStrategy
from app.services.report.onestage_strategy import OneStageReportStrategy


@pytest.mark.integration
@pytest.mark.llm
@pytest.mark.neo4j
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "exam_type, expected_strategy_type, expected_strategy_class",
    [
        ("ionnutri", "multistage", MultiStageReportStrategy),
        ("vidanova", "onestage", OneStageReportStrategy),
    ],
)
async def test_report_coordinator_strategy_pattern_integration(
    real_report_coordinator,
    strategy_factory,
    real_llm_service,
    sample_exam_data: TNMExamData,
    sample_anamnesis: PatientAnamnesis,
    exam_type: str,
    expected_strategy_type: str,
    expected_strategy_class,
):
    """Full integration test for ReportCoordinator with the Strategy Pattern using real services."""
    # Generate report using the coordinator and real services
    result = await real_report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, exam_type
    )

    # Main validations for the report
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2

    markdown_report, domain_report = result

    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 100
    assert domain_report is None  # Strategy mode returns None for domain report

    # Ensure the report does not contain mock content
    assert "mockado" not in markdown_report.lower()
    assert "mock" not in markdown_report.lower()

    # Validate the StrategyFactory returns the correct strategy type
    strategy = strategy_factory.create_strategy(
        exam_type,
        expected_strategy_type,
        {
            "llm_service": real_llm_service,
            "prompt_registry": real_report_coordinator.prompt_registry,
        },
    )

    assert strategy is not None
    assert isinstance(strategy, expected_strategy_class)

    # Ensure the strategy's exam configuration matches the exam type
    assert strategy.exam_config.get_exam_type() == exam_type

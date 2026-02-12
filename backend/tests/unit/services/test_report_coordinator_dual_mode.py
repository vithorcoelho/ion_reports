"""Unit tests for ReportCoordinator with separate plugins and strategy mode tests."""

import pytest


@pytest.mark.asyncio
async def test_plugins_mode(
    report_coordinator_plugins, sample_exam_data, sample_anamnesis
):
    """Test the complete for plugins mode."""
    coordinator = report_coordinator_plugins

    result = await coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    # Plugin mode returns a tuple (markdown, domain_report)
    assert isinstance(result, tuple)
    assert len(result) == 2

    markdown_report, domain_report = result

    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 50
    assert sample_exam_data.patient_id in markdown_report

    # Plugin mode returns a domain report
    assert domain_report is not None
    assert hasattr(domain_report, "report_id")


@pytest.mark.asyncio
async def test_strategy_mode(
    report_coordinator_strategy, sample_exam_data, sample_anamnesis
):
    """Test the complete for strategy mode."""
    coordinator = report_coordinator_strategy

    result = await coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    # Strategy mode returns a tuple (markdown, None)
    assert isinstance(result, tuple)
    assert len(result) == 2

    markdown_report, domain_report = result

    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 50
    assert sample_exam_data.patient_id in markdown_report

    # Strategy mode returns None for domain report
    assert domain_report is None

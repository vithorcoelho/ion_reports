"""Unit tests for report generation strategies."""

import pytest

from app.services.report.multistage_strategy import MultiStageReportStrategy
from app.services.report.onestage_strategy import OneStageReportStrategy


@pytest.mark.asyncio
async def test_multistage_executes_successfully(
    multistage_strategy,
    mock_exam_config,
    sample_exam_data,
    sample_anamnesis,
    mock_kg_data,
):
    """Test MultiStage executes and returns a string result."""
    mock_exam_config.get_exam_type.return_value = "ionnutri"

    result = await multistage_strategy.execute(
        sample_exam_data, sample_anamnesis, mock_kg_data
    )

    assert isinstance(result, str)
    assert len(result) > 0


@pytest.mark.asyncio
async def test_onestage_executes_successfully(
    onestage_strategy,
    mock_exam_config,
    sample_exam_data,
    sample_anamnesis,
    mock_kg_data,
):
    """Test OneStage executes and returns a string result."""
    mock_exam_config.get_exam_type.return_value = "ionnutri"

    result = await onestage_strategy.execute(
        sample_exam_data, sample_anamnesis, mock_kg_data
    )

    assert isinstance(result, str)
    assert len(result) > 0


@pytest.mark.asyncio
async def test_multistage_works_with_ionnutri_exam_type(
    mock_exam_config, mock_services, sample_exam_data, sample_anamnesis, mock_kg_data
):
    """Test MultiStage works with ionnutri exam type."""
    mock_exam_config.get_exam_type.return_value = "ionnutri"

    multistage = MultiStageReportStrategy(mock_exam_config, mock_services)

    result = await multistage.execute(sample_exam_data, sample_anamnesis, mock_kg_data)

    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_onestage_works_with_vidanova_exam_type(
    mock_exam_config, mock_services, sample_exam_data, sample_anamnesis, mock_kg_data
):
    """Test OneStage works with vidanova exam type."""
    mock_exam_config.get_exam_type.return_value = "vidanova"

    onestage = OneStageReportStrategy(mock_exam_config, mock_services)

    result = await onestage.execute(sample_exam_data, sample_anamnesis, mock_kg_data)

    assert isinstance(result, str)


def test_multistage_initializes_with_default_alias(mock_exam_config, mock_services):
    """Test MultiStage initializes with production alias by default."""
    multistage = MultiStageReportStrategy(mock_exam_config, mock_services)
    assert multistage.alias == "production"


def test_onestage_initializes_with_default_alias(mock_exam_config, mock_services):
    """Test OneStage initializes with production alias by default."""
    onestage = OneStageReportStrategy(mock_exam_config, mock_services)
    assert onestage.alias == "production"

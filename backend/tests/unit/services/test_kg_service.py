"""Tests for Knowledge Graph service functionality."""

import pytest

from app.domain.kg_result import KGResult


@pytest.mark.asyncio
async def test_get_knowledge_data_success(
    kg_instance, sample_exam_data, sample_anamnesis
):
    """Tests if get_knowledge_data returns correctly valid data."""
    result = await kg_instance.get_knowledge_data(sample_exam_data, sample_anamnesis)

    assert isinstance(result, KGResult)
    assert len(result.metabolite_info) == 1
    assert result.metabolite_info[0].name == "L-carnitina"
    assert result.metabolite_info[0].status == "deficit_severo"
    assert len(result.manifestations) == 1
    assert len(result.recommended_interventions) == 1
    assert len(result.foods) == 1
    assert len(result.supplements) == 1
    assert len(result.pathway_impacts) == 1
    assert len(result.scientific_evidence) == 1
    assert len(result.contraindications) == 1
    assert result.error is None


@pytest.mark.asyncio
async def test_get_knowledge_data_query_failure(
    kg_instance, sample_exam_data, sample_anamnesis, mocker
):
    """Tests if get_knowledge_data handles exception safely."""
    # Mock to simulate query error
    mocker.patch.object(
        kg_instance.kg_query,
        "execute_unified_query",
        new_callable=mocker.AsyncMock,
        side_effect=Exception("Neo4j connection error"),
    )

    result = await kg_instance.get_knowledge_data(sample_exam_data, sample_anamnesis)

    assert isinstance(result, KGResult)
    assert result.error is not None
    assert (
        "Error executing knowledge graph query: Neo4j connection error" in result.error
    )
    assert len(result.metabolite_info) == 0
    assert len(result.manifestations) == 0
    assert len(result.recommended_interventions) == 0


@pytest.mark.asyncio
async def test_get_knowledge_data_empty_result(
    kg_instance, sample_exam_data, sample_anamnesis, mock_empty_kg_data
):
    """Tests if get_knowledge_data handles empty results correctly."""
    # Mock to return empty result
    kg_instance.kg_query.execute_unified_query.return_value = mock_empty_kg_data

    result = await kg_instance.get_knowledge_data(sample_exam_data, sample_anamnesis)

    assert isinstance(result, KGResult)
    assert len(result.metabolite_info) == 0
    assert len(result.manifestations) == 0
    assert len(result.recommended_interventions) == 0
    assert len(result.foods) == 0
    assert len(result.supplements) == 0
    assert len(result.pathway_impacts) == 0
    assert len(result.scientific_evidence) == 0
    assert len(result.contraindications) == 0
    assert result.error is None


@pytest.mark.asyncio
async def test_get_knowledge_data_timeout_error(
    kg_instance, sample_exam_data, sample_anamnesis, mocker
):
    """Tests timeout error handling in get_knowledge_data."""
    mocker.patch.object(
        kg_instance.kg_query,
        "execute_unified_query",
        new_callable=mocker.AsyncMock,
        side_effect=TimeoutError("Query timeout"),
    )

    result = await kg_instance.get_knowledge_data(sample_exam_data, sample_anamnesis)

    assert isinstance(result, KGResult)
    assert result.error is not None
    assert "Error executing knowledge graph query: Query timeout" in result.error
    assert len(result.metabolite_info) == 0
    assert len(result.manifestations) == 0
    assert len(result.recommended_interventions) == 0


@pytest.mark.asyncio
async def test_get_knowledge_data_connection_error(
    kg_instance, sample_exam_data, sample_anamnesis, mocker
):
    """Tests connection error handling in get_knowledge_data."""
    mocker.patch.object(
        kg_instance.kg_query,
        "execute_unified_query",
        new_callable=mocker.AsyncMock,
        side_effect=ConnectionError("Database connection failed"),
    )

    result = await kg_instance.get_knowledge_data(sample_exam_data, sample_anamnesis)

    assert isinstance(result, KGResult)
    assert result.error is not None
    assert (
        "Error executing knowledge graph query: Database connection failed"
        in result.error
    )
    assert len(result.metabolite_info) == 0
    assert len(result.manifestations) == 0
    assert len(result.recommended_interventions) == 0


@pytest.mark.asyncio
async def test_get_knowledge_data_with_mock_kg_data(
    kg_instance, sample_exam_data, sample_anamnesis, mock_kg_data
):
    """Tests if get_knowledge_data works with mock specific data."""
    # Mock to return specific data
    kg_instance.kg_query.execute_unified_query.return_value = mock_kg_data

    result = await kg_instance.get_knowledge_data(sample_exam_data, sample_anamnesis)

    assert isinstance(result, KGResult)
    assert len(result.metabolite_info) == 1
    assert result.metabolite_info[0].name == "Carnitina"
    assert result.metabolite_info[0].status == "baixo"
    assert result.metabolite_info[0].value == 25.0

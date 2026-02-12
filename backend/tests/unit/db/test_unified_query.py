"""Unit tests for unified knowledge graph queries."""

from datetime import datetime

import pytest

from app.domain.kg_result import KGResult
from app.schemas.exam import Metabolite, TNMExamData


@pytest.mark.parametrize(
    "metabolites,expected_call_count",
    [
        ([Metabolite(name="Test1", value=1.0)], 1),
        ([Metabolite(name="Test1", value=1.0), Metabolite(name="Test2", value=2.0)], 1),
    ],
)
@pytest.mark.asyncio
async def test_execute_unified_query_calls_database(
    mocker, query_unified, sample_anamnesis, metabolites, expected_call_count
):
    """Query should always call the database, regardless of the number of metabolites."""
    mocker.patch.object(query_unified.client, "execute_query", return_value=[])

    exam_data = TNMExamData(
        patient_id="test_patient",
        exam_date=datetime.now(),
        metabolites=metabolites,
    )

    result = await query_unified.execute_unified_query(exam_data, sample_anamnesis)

    assert query_unified.client.execute_query.call_count == expected_call_count
    assert isinstance(result, KGResult)


@pytest.mark.asyncio
async def test_execute_unified_query_successful_connection(
    mocker, query_unified, sample_exam_data, sample_anamnesis, mock_kg_response
):
    """With a valid database response, should return a populated TNMResult."""
    mocker.patch.object(
        query_unified.client, "execute_query", return_value=mock_kg_response
    )

    result = await query_unified.execute_unified_query(
        sample_exam_data, sample_anamnesis
    )

    assert len(result.metabolite_info) == 1
    assert result.metabolite_info[0].name == "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]"
    assert result.metabolite_info[0].status == "deficit_severo"

    assert len(result.manifestations) == 1
    assert len(result.recommended_interventions) == 1
    assert len(result.foods) == 1
    assert len(result.supplements) == 1


@pytest.mark.parametrize(
    "db_response,expected_empty",
    [
        ([], True),
        ([{"result": None}], True),
        ([{"result": {}}], True),
        ([{}], True),
    ],
)
@pytest.mark.asyncio
async def test_execute_unified_query_empty_responses(
    mocker,
    query_unified,
    sample_exam_data,
    sample_anamnesis,
    db_response,
    expected_empty,
):
    """Empty/invalid responses should return an empty but valid TNMResult."""
    mocker.patch.object(query_unified.client, "execute_query", return_value=db_response)

    result = await query_unified.execute_unified_query(
        sample_exam_data, sample_anamnesis
    )

    if expected_empty:
        assert len(result.metabolite_info) == 0
        assert len(result.manifestations) == 0
        assert len(result.recommended_interventions) == 0


@pytest.mark.asyncio
async def test_execute_unified_query_database_connection_failure(
    mocker, query_unified, sample_exam_data, sample_anamnesis
):
    """Connection failure should return an empty but valid TNMResult."""
    mocker.patch.object(
        query_unified.client,
        "execute_query",
        side_effect=Exception("Connection timeout"),
    )

    result = await query_unified.execute_unified_query(
        sample_exam_data, sample_anamnesis
    )

    assert isinstance(result, KGResult)
    assert len(result.metabolite_info) == 0
    assert len(result.manifestations) == 0


@pytest.mark.asyncio
async def test_query_parameters_passed_correctly(
    mocker, query_unified, sample_anamnesis
):
    """Parameters must be passed in the correct structure to the database."""
    mocker.patch.object(query_unified.client, "execute_query", return_value=[])

    exam_data = TNMExamData(
        patient_id="test_patient",
        exam_date=datetime.now(),
        metabolites=[
            Metabolite(name="TestMetabolite1", value=75.5),
            Metabolite(name="TestMetabolite2", value=120.0),
        ],
    )

    await query_unified.execute_unified_query(exam_data, sample_anamnesis)

    call_args = query_unified.client.execute_query.call_args
    query_params = call_args[1]

    assert "metabolites" in query_params
    assert "context" in query_params

    metabolites = query_params["metabolites"]
    assert len(metabolites) == 2
    assert metabolites[0]["name"] == "TestMetabolite1"
    assert metabolites[0]["value"] == 75.5

    context = query_params["context"]
    assert context["age"] == 35
    assert context["gender"] == "F"
    assert "medical_history" in context
    assert "medications" in context


@pytest.mark.asyncio
async def test_contraindications_extraction(
    mocker, query_unified, sample_exam_data, sample_anamnesis
):
    """Contraindications should be correctly extracted from interventions."""
    mock_response = [
        {
            "result": {
                "metabolite_info": [],
                "manifestations": [],
                "interventions": [
                    {
                        "type": "dietary",
                        "description": "Increase choline intake",
                        "metabolite": "TestMetabolite",
                        "contraindicated": True,
                        "contraindication_reason": "Histórico de câncer de próstata avançado",
                        "medication_interaction": "Anticoagulantes",
                    }
                ],
                "foods": [],
                "supplements": [],
                "pathways": [],
                "evidence": [],
            }
        }
    ]

    mocker.patch.object(
        query_unified.client, "execute_query", return_value=mock_response
    )

    result = await query_unified.execute_unified_query(
        sample_exam_data, sample_anamnesis
    )

    assert len(result.contraindications) == 1
    contraindication = result.contraindications[0]
    assert contraindication.reason == "Histórico de câncer de próstata avançado"
    assert contraindication.type == "medical_history"


@pytest.mark.asyncio
async def test_real_database_connection(
    query_unified_with_test_db, sample_exam_data, sample_anamnesis
):
    """Real integration test with the database (requires test instance)."""
    result = await query_unified_with_test_db.execute_unified_query(
        sample_exam_data, sample_anamnesis
    )

    assert isinstance(result, KGResult)

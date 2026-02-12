"""End-to-end tests for error scenarios in the report generation pipeline.

This module contains tests that verify the system's behavior when handling
invalid input data, including:
- Invalid metabolite values
- Metabolite data not found in Neo4j
- Negative metabolite values
- Patient ID mismatch between exam data and anamnesis
"""

from datetime import date

import pytest

from app.schemas.exam import Metabolite, TNMExamData
from app.schemas.patient_anamnesis import (
    AlcoholConsumption,
    ContextFactors,
    Medication,
    PatientAnamnesis,
    PersonalData,
    PhysicalActivity,
    Sleep,
)


@pytest.mark.asyncio
@pytest.mark.integration
async def test_api_endpoint_with_invalid_metabolite_values(
    client,
    mock_anamnesis,
    report_coordinator_e2e,
    neo4j_container,
    setup_dependency_override,
    mock_mlflow,
):
    """Tests API endpoint behavior with invalid metabolite values.

    This test uses real validation to ensure that invalid metabolite values
    are properly handled by the system.
    """
    # Create exam data with invalid metabolite values
    invalid_metabolite_exam = {
        "patient_id": "PAT001",
        "exam_date": str(date.today()),
        "metabolites": [
            {
                "name": "",  # Invalid empty name
                "value": 0.07,
                "unit": "mmol/L",
            }
        ],
    }

    request_data = {
        "exam_data": invalid_metabolite_exam,
        "anamnesis": mock_anamnesis.model_dump(mode="json"),
    }

    response = client.post("/api/v1/reports/", json=request_data)

    assert response.status_code == 400
    error_data = response.json()
    assert "detail" in error_data


@pytest.mark.asyncio
@pytest.mark.integration
async def test_api_endpoint_with_unknown_metabolite(
    client,
    mock_anamnesis,
    report_coordinator_e2e,
    neo4j_container,
    setup_dependency_override,
    mock_mlflow,
):
    """Tests API endpoint behavior when metabolite data is not found in Neo4j.

    This test ensures that the system gracefully handles cases where
    metabolite information is missing from the knowledge graph, using
    real Neo4j queries.
    """
    # Create exam data with a metabolite that doesn't exist in Neo4j
    unknown_metabolite_exam = TNMExamData(
        patient_id="PAT001",
        anamnesis_type="ionnutri",
        exam_date=date.today(),
        metabolites=[
            Metabolite(
                name="UNKNOWN-METABOLITE-XYZ-NOT-IN-DATABASE",
                value=1.5,
            ),
        ],
    )

    request_data = {
        "exam_data": unknown_metabolite_exam.model_dump(mode="json"),
        "anamnesis": mock_anamnesis.model_dump(mode="json"),
    }

    response = client.post("/api/v1/reports/", json=request_data)

    # Should still return 200 but with limited information in the report
    assert response.status_code == 200
    report_data = response.json()

    # Verify basic structure is maintained
    assert report_data["patient_id"] == "PAT001"
    assert report_data["report_id"] == "PAT001"
    assert "report" in report_data
    assert isinstance(report_data["report"], str)
    assert len(report_data["report"]) > 0


@pytest.mark.asyncio
@pytest.mark.integration
async def test_api_endpoint_with_negative_metabolite_values(
    client,
    mock_anamnesis,
    report_coordinator_e2e,
    neo4j_container,
    setup_dependency_override,
    mock_mlflow,
):
    """Tests API endpoint behavior with negative metabolite values.

    This test ensures that the system properly handles negative values
    which might be invalid for certain metabolites.
    """
    # Create exam data with negative values
    negative_values_exam = {
        "patient_id": "PAT001",
        "exam_date": str(date.today()),
        "metabolites": [
            {
                "name": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                "value": -1.0,  # Negative value
                "unit": "mmol/L",
            }
        ],
    }

    request_data = {
        "exam_data": negative_values_exam,
        "anamnesis": mock_anamnesis.model_dump(mode="json"),
    }

    response = client.post("/api/v1/reports/", json=request_data)

    # Should handle gracefully - behavior depends on business rules
    assert response.status_code == 400
    error_data = response.json()
    assert "detail" in error_data


@pytest.mark.asyncio
@pytest.mark.integration
async def test_api_endpoint_with_missing_patient_id_mismatch(
    client, report_coordinator_e2e, neo4j_container, setup_dependency_override
):
    """Tests API endpoint behavior when patient IDs don't match between exam data and anamnesis.

    This test ensures that the system handles patient ID mismatches
    appropriately.
    """
    # Create exam data and anamnesis with different patient IDs
    exam_data = TNMExamData(
        patient_id="PAT001",
        exam_date=date.today(),
        metabolites=[
            Metabolite(
                name="1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                value=0.07,
            ),
        ],
    )

    anamnesis = PatientAnamnesis(
        patient_id="PAT002",  # Different patient ID
        date=date.today(),
        objective="Melhorar saúde metabólica",
        personal_data=PersonalData(
            age=35, gender="F", weight=65.0, height=1.65, bmi=23.9
        ),
        context_factors=ContextFactors(
            medical_history=["hipertensão leve"],
            intolerances=["lactose"],
            physical_activity=PhysicalActivity(
                type="caminhada", frequency="3", intensity="moderada"
            ),
            sleep=Sleep(quality="boa", hours=8, issues=[]),
            alcohol_consumption=AlcoholConsumption(frequency="2", amount="1 taça"),
            medications=[Medication(name="Losartana", frequency="1x/dia", dosage=None)],
            stress_level="moderado",
        ),
    )

    request_data = {
        "exam_data": exam_data.model_dump(mode="json"),
        "anamnesis": anamnesis.model_dump(mode="json"),
    }

    response = client.post("/api/v1/reports/", json=request_data)

    assert response.status_code == 400
    error_data = response.json()
    assert "detail" in error_data

"""Unit tests for API endpoints.

This module contains comprehensive tests for the FastAPI endpoints,
including report generation, validation, error handling, and response formatting.
"""

from app.domain.kg_result import KGResult


def test_reports_endpoint_success(
    client,
    sample_exam_data,
    sample_anamnesis,
    setup_all_services_for_success,
    mock_mlflow,
):
    """Tests if the endpoint correctly generates a report with valid data."""
    teste = {
        "exam_data": sample_exam_data.model_dump(mode="json"),
        "anamnesis": sample_anamnesis.model_dump(mode="json"),
    }
    response = client.post("/api/v1/reports/", json=teste)

    # Checks
    assert response.status_code == 200
    data = response.json()

    # Check report structure
    assert "report_id" in data
    assert data["patient_id"] == "PAT001"
    assert "anamnesis_id" in data
    assert "exam_id" in data
    assert "version" in data
    assert "timestamp" in data
    assert "report" in data
    assert isinstance(data["report"], str)  # Should be markdown content


def test_reports_endpoint_validation_missing_metabolites(
    client,
    sample_exam_data,
    sample_anamnesis,
    setup_all_services_for_success,
):
    """Tests if the API correctly validates data missing metabolites."""
    invalid_data = sample_exam_data.model_dump(mode="json")
    invalid_data.pop("metabolites")

    response = client.post(
        "/api/v1/reports/",
        json={
            "exam_data": invalid_data,
            "anamnesis": sample_anamnesis.model_dump(mode="json"),
        },
    )

    assert response.status_code == 400
    assert "metabolites" in response.text


def test_reports_endpoint_validation_invalid_value(
    client, sample_exam_data, sample_anamnesis, setup_all_services_for_success
):
    """Tests if the API correctly validates data with an invalid value."""
    invalid_data = sample_exam_data.model_dump(mode="json")
    invalid_data["metabolites"][0]["value"] = "não-numérico"

    response = client.post(
        "/api/v1/reports/",
        json={
            "exam_data": invalid_data,
            "anamnesis": sample_anamnesis.model_dump(mode="json"),
        },
    )

    assert response.status_code == 400
    assert "value" in response.text
    assert "float_parsing" in response.text


def test_reports_endpoint_patient_id_mismatch(
    client, sample_exam_data, sample_anamnesis, setup_all_services_for_success
):
    """Tests if the API validates when patient IDs do not match."""
    mismatched_data = sample_exam_data.model_dump(mode="json")
    mismatched_data["patient_id"] = "P414"

    response = client.post(
        "/api/v1/reports/",
        json={
            "exam_data": mismatched_data,
            "anamnesis": sample_anamnesis.model_dump(mode="json"),
        },
    )

    assert response.status_code == 400
    assert "IDs de paciente inconsistentes" in response.text


def test_reports_endpoint_kg_failure(
    mocker,
    client,
    sample_exam_data,
    sample_anamnesis,
    mock_kg_service,
    mock_llm_service,
    mock_report,  # Usar mock_tnm_service de conftest.py,
    mock_mlflow,
):
    """Tests the API response when the Knowledge Graph query fails."""
    # Configure generate_report to raise an exception to simulate KG failure
    mock_report.generate_report = mocker.AsyncMock(
        side_effect=Exception("Knowledge graph query failed: Simulated KG query error")
    )

    response = client.post(
        "/api/v1/reports/",
        json={
            "exam_data": sample_exam_data.model_dump(mode="json"),
            "anamnesis": sample_anamnesis.model_dump(mode="json"),
        },
    )

    assert response.status_code == 500
    assert "Knowledge graph query failed: Simulated KG query error" in response.text


def test_reports_endpoint_llm_failure(
    mocker,
    client,
    sample_exam_data,
    sample_anamnesis,
    mock_llm_service,
    mock_kg_service,
    mock_report,  # Usar mock_tnm_service de conftest.py
    mock_mlflow,
):
    """Testa a resposta da API quando a chamada ao LLM falha."""
    # Configure generate_report to fail with LLM error
    mock_report.generate_report = mocker.AsyncMock(
        side_effect=Exception("Erro na geração do relatório TNM")
    )

    response = client.post(
        "/api/v1/reports/",
        json={
            "exam_data": sample_exam_data.model_dump(mode="json"),
            "anamnesis": sample_anamnesis.model_dump(mode="json"),
        },
    )

    assert response.status_code == 500
    assert "Erro na geração do relatório TNM" in response.text


def test_reports_endpoint_validation_empty_metabolites_list(
    client, sample_exam_data, sample_anamnesis, mock_kg_service, mock_llm_service
):
    """Testa se a API valida corretamente uma lista de metabólitos vazia."""
    exam_data_empty_metabolites = sample_exam_data.model_dump(mode="json")
    exam_data_empty_metabolites["metabolites"] = []

    # Configurações específicas para este teste
    mock_kg_service.execute_unified_query.return_value = KGResult(metabolite_info=[])
    # Note: generate_prompt is not available in OpenRouterLLMService

    # O mock do LLM deve retornar findings vazios para este cenário
    mock_llm_service.call_llm.return_value = {
        "content": """
        {
            "findings": {"title": "Achados Principais", "items": []},
            "recommendations": {"title": "Recomendações", "items": []},
            "summary": "No specific findings for empty metabolites.",
            "deficiencies": {"title": "Deficiências", "items": []},
            "general_guidelines": {"title": "Orientações Gerais", "items": []},
        }
        """
    }

    response = client.post(
        "/api/v1/reports/",
        json={
            "exam_data": exam_data_empty_metabolites,
            "anamnesis": sample_anamnesis.model_dump(mode="json"),
        },
    )

    assert response.status_code == 400
    assert (
        "metabolites" in response.text
    )  # Verifica se o erro é sobre o campo 'metabolites'

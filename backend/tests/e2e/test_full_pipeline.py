"""End-to-end tests for the full report generation pipeline.

This module contains tests that verify the complete flow of report generation
from API request to final response, including:
- API endpoint integration
- Business logic orchestration
- Knowledge graph querying
- LLM interaction
- Report generation
"""

import pytest


@pytest.mark.asyncio
@pytest.mark.integration
async def test_api_endpoint_integration(
    client,
    mock_exam_data,
    mock_anamnesis,
    report_coordinator_e2e,
    neo4j_container,
    setup_dependency_override,
    mock_mlflow,
):
    """Tests the full integration flow of the API for report generation.

    This end-to-end test validates the integration of multiple system components,
    including:
    - The `/api/v1/reports/` endpoint of the FastAPI application.
    - The TNMService, orchestrating business logic.
    - The LLMService, simulating interaction with a real language model.
    - The Neo4jKnowledgeQuery, interacting with a real (containerized) Neo4j instance.

    The tested flow involves:
    1. Sending exam data (metabolites) and patient anamnesis to the API.
    2. Querying the knowledge graph (Neo4j) for contextual information.
    3. Generating a detailed report using the LLM.
    4. Validating the structure and format of the report response.

    Args:
        client: FastAPI test client for making HTTP requests.
        mock_exam_data: Fixture containing mocked exam data for the test.
        mock_anamnesis: Fixture containing mocked anamnesis data for the test.
        report_coordinator_e2e: Fixture providing a real instance of TNMService,
                         configured with real LLMService and Neo4jKnowledgeQuery.
        neo4j_container: Fixture that initializes and manages a temporary Neo4j
                         container for the test, ensuring an isolated environment.
        setup_dependency_override: Fixture that sets up dependency overrides for the test.
        mock_mlflow: Fixture that mocks the MLflow library for the test.

    Asserts:
        - The HTTP response status is 200 (OK).
        - The patient ID in the report matches the expected value ("PAT001").
        - The report ID contains the expected prefix ("TNM_PAT001_").
        - The report version is "1.0".
        - The report contains the essential keys: "summary", "findings",
          "recommendations", and "timestamp", ensuring the expected structure
          of the LLM and service output.

    """
    request_data = {
        "exam_data": mock_exam_data.model_dump(mode="json"),
        "anamnesis": mock_anamnesis.model_dump(mode="json"),
    }

    response = client.post("/api/v1/reports/", json=request_data)

    assert response.status_code == 200
    report_data = response.json()

    assert report_data["patient_id"] == "PAT001"
    assert report_data["report_id"] == "PAT001"
    assert report_data["version"] == "1.0"
    assert "report" in report_data
    assert isinstance(report_data["report"], str)
    assert len(report_data["report"]) > 0
    assert "timestamp" in report_data

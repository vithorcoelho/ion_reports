"""Performance tests for the IonNutri application.

This module contains performance and load tests that verify
the system's behavior under various load conditions and measure
response times, memory usage, and concurrent request handling.
"""

import time
import tracemalloc

import pytest

from app.api.dependencies import get_coordinator
from app.main import app


# Helper to generate unique data
def generate_data(sample_exam_data, sample_anamnesis, patient_id):
    """Generate test data with unique patient ID."""
    exam = sample_exam_data.model_copy()
    exam.patient_id = patient_id
    anamnesis = sample_anamnesis.model_copy()
    anamnesis.patient_id = patient_id
    return exam, anamnesis


@pytest.mark.asyncio
@pytest.mark.performance
async def test_response_time_single_request(
    sample_exam_data, sample_anamnesis, report_coordinator
):
    """Single request response time test.

    Criteria: < 5 seconds for a simple report.
    """
    exam, anamnesis = generate_data(sample_exam_data, sample_anamnesis, "PAT001")

    start = time.time()
    result = await report_coordinator.generate_report(exam, anamnesis, "ionnutri")
    elapsed = time.time() - start

    # Extract markdown report from tuple
    markdown_report, domain_report = result
    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert "PAT001" in markdown_report, "Deve conter ID do paciente"
    assert len(markdown_report) > 100, "Relatório deve ter conteúdo substancial"

    assert elapsed < 5.0


@pytest.mark.asyncio
@pytest.mark.performance
@pytest.mark.parametrize("patient_id", [f"PAT{i:03d}" for i in range(1, 11)])
async def test_concurrent_requests_performance(
    sample_exam_data, sample_anamnesis, report_coordinator, patient_id
):
    """Throughput test with multiple concurrent requests.

    Criteria: Process 10 reports in less than 10 seconds.
    """
    exam, anamnesis = generate_data(sample_exam_data, sample_anamnesis, patient_id)
    result = await report_coordinator.generate_report(exam, anamnesis, "ionnutri")
    markdown_report, domain_report = result
    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert len(markdown_report) > 100, "Relatório deve ter conteúdo substancial"


@pytest.mark.asyncio
@pytest.mark.performance
@pytest.mark.parametrize("patient_id", [f"MEM{i:03d}" for i in range(5)])
async def test_memory_usage_large_dataset(
    sample_exam_data, sample_anamnesis, report_coordinator, patient_id
):
    """Test memory usage with large dataset."""
    tracemalloc.start()
    exam, anamnesis = generate_data(sample_exam_data, sample_anamnesis, patient_id)
    result = await report_coordinator.generate_report(exam, anamnesis, "ionnutri")
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memory_mb = peak / 1024 / 1024
    markdown_report, domain_report = result
    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert len(markdown_report) > 100, "Relatório deve ter conteúdo substancial"
    assert memory_mb < 100


@pytest.mark.asyncio
@pytest.mark.performance
async def test_api_endpoint_performance(
    client, sample_exam_data, sample_anamnesis, mocker, report_coordinator, mock_mlflow
):
    """Teste de performance do endpoint da API."""
    app.dependency_overrides[get_coordinator] = lambda: report_coordinator

    data = {
        "exam_data": sample_exam_data.model_dump(mode="json"),
        "anamnesis": sample_anamnesis.model_dump(mode="json"),
    }

    start = time.time()
    response = client.post("/api/v1/reports/", json=data)
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 6.0


@pytest.mark.asyncio
@pytest.mark.performance
@pytest.mark.parametrize("patient_id", [f"CONC{i:03d}" for i in range(15)])
async def test_load_simulation(
    sample_exam_data, sample_anamnesis, report_coordinator, patient_id
):
    """Load simulation with sequential requests.

    Simulates usage by multiple users over a period of time,
    sending requests one after another in sequence.
    """
    exam, anamnesis = generate_data(sample_exam_data, sample_anamnesis, patient_id)

    start = time.time()
    result = await report_coordinator.generate_report(exam, anamnesis, "ionnutri")
    elapsed = time.time() - start

    markdown_report, domain_report = result
    assert isinstance(markdown_report, str), "Deve retornar string markdown"
    assert len(markdown_report) > 100, "Relatório deve ter conteúdo substancial"
    assert elapsed < 12.0

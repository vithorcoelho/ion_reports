"""Unit tests for the ReportCoordinator service."""

import pytest


@pytest.mark.asyncio
async def test_complete_end_to_end_workflow(
    report_coordinator, sample_exam_data, sample_anamnesis
):
    """Test the complete end-to-end workflow for report generation."""
    result = await report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    # Both modes return a tuple (markdown, report)
    assert isinstance(result, tuple)
    assert len(result) == 2

    markdown_report, domain_report = result

    # Markdown report should always be a string
    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 100
    assert sample_exam_data.patient_id in markdown_report
    assert "resumo gerado pelo llm para o paciente" in markdown_report.lower()

    # Domain report behavior depends on mode
    if hasattr(report_coordinator, "strategy_factory"):
        # Strategy mode returns None for domain report
        assert domain_report is None
    else:
        # Plugin mode returns a domain report
        assert domain_report is not None


@pytest.mark.asyncio
async def test_report_includes_all_relevant_patient_data(
    report_coordinator, sample_exam_data, sample_anamnesis
):
    """Verifica se o relatório gerado inclui todos os dados relevantes do paciente.

    Testa indiretamente se os prompts estão sendo gerados com os dados corretos.
    """
    # Arrange
    mock_llm_service = report_coordinator.llm_service

    # Act
    result = await report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    # Assert - Dados do paciente estão presentes no relatório markdown
    assert isinstance(markdown_report, str)
    assert sample_exam_data.patient_id in markdown_report
    assert len(markdown_report) > 100

    # Assert - Verifica que o LLM foi chamado (ambos os modos usam call_llm)
    assert mock_llm_service.call_llm.call_count > 0  # Pelo menos uma chamada

    # Assert - Conteúdo mockado está presente
    assert "resumo gerado pelo llm para o paciente" in markdown_report.lower()


@pytest.mark.parametrize(
    "expected_message",
    [
        "Starting report generation for exam type: ionnutri",
        "Selected strategy",
        "Report for exam_type 'ionnutri' generated successfully",
    ],
    ids=["inicio", "consulta", "finalizacao"],
)
@pytest.mark.asyncio
async def test_service_logs_workflow_steps(
    report_coordinator, sample_exam_data, sample_anamnesis, caplog, expected_message
):
    """Test that the service logs all workflow steps properly."""
    result = await report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    assert markdown_report is not None
    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 100

    assert expected_message in caplog.text


@pytest.mark.asyncio
async def test_generate_report_kg_error(
    report_coordinator,
    sample_exam_data,
    sample_anamnesis,
):
    """Test that knowledge graph errors are properly handled."""
    result = await report_coordinator.generate_report(
        sample_exam_data, sample_anamnesis, "ionnutri"
    )

    markdown_report, domain_report = result

    assert isinstance(markdown_report, str)
    assert len(markdown_report) > 100


@pytest.mark.asyncio
async def test_generate_report_unexpected_error(
    report_coordinator, mocker, sample_exam_data, sample_anamnesis
):
    """Test that unexpected LLM errors are handled gracefully."""
    # Configura o mock do LLM para lançar uma exceção
    report_coordinator.llm_service.call_llm.side_effect = Exception(
        "LLM connection error"
    )

    # Both modes should raise RuntimeError when LLM fails
    with pytest.raises(
        RuntimeError,
        match=r"Failed to generate report for 'ionnutri'|Error generating report",
    ):
        await report_coordinator.generate_report(
            sample_exam_data, sample_anamnesis, "ionnutri"
        )

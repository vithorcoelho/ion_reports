"""Unit tests for the OpenRouterLLM service."""

import pytest

from app.domain.report import SummaryContent


@pytest.mark.asyncio
async def test_call_llm_api_success(llm_instance, mocker):
    """Testa se call_llm_api retorna corretamente com resposta válida."""
    # Força o LLM a estar habilitado para testar o comportamento real
    mocker.patch("app.services.llm.llm_service.settings.ENABLE_LLM", True)

    mock_parsed_content = SummaryContent(content="resposta mock")
    mock_message = mocker.Mock(parsed=mock_parsed_content)
    mock_choice = mocker.Mock(message=mock_message)
    mock_completion = mocker.Mock(choices=[mock_choice])

    mocker.patch.object(
        llm_instance.client.beta.chat.completions,
        "parse",
        new_callable=mocker.AsyncMock,
        return_value=mock_completion,
    )

    result = await llm_instance.call_llm(
        user_prompt="prompt exemplo", schema=SummaryContent
    )

    assert isinstance(result, SummaryContent)
    assert result.content == "resposta mock"


@pytest.mark.asyncio
async def test_call_llm_api_failure(llm_instance, mocker):
    """Testa se call_llm_api lida com exceção de forma segura."""
    # Força o LLM a estar habilitado para testar o comportamento real
    mocker.patch("app.services.llm.llm_service.settings.ENABLE_LLM", True)

    mocker.patch.object(
        llm_instance.client.beta.chat.completions,
        "parse",
        new_callable=mocker.AsyncMock,
        side_effect=Exception("LLM API Error"),
    )

    with pytest.raises(
        ValueError,
        match=r"Cannot query model 'gemini' or process response: LLM API Error",
    ):
        await llm_instance.call_llm(user_prompt="prompt exemplo", schema=SummaryContent)


@pytest.mark.asyncio
async def test_call_llm_api_parse_response_fail(llm_instance, mocker):
    """Testa se call_llm_api lida com erro ao tentar parsear resposta ou validar schema."""
    # Força o LLM a estar habilitado para testar o comportamento real
    mocker.patch("app.services.llm.llm_service.settings.ENABLE_LLM", True)

    # Mock que retorna None para simular falha na validação
    mock_message = mocker.Mock(parsed=None)
    mock_choice = mocker.Mock(message=mock_message)
    mock_completion = mocker.Mock(choices=[mock_choice])

    mocker.patch.object(
        llm_instance.client.beta.chat.completions,
        "parse",
        new_callable=mocker.AsyncMock,
        return_value=mock_completion,
    )

    with pytest.raises(ValueError) as exc_info:
        await llm_instance.call_llm(user_prompt="prompt", schema=SummaryContent)

    assert "LLM returned None response" in str(exc_info.value)


# Note: generate_prompt method is not available in OpenRouterLLMService
# as it was specific to the legacy LLMService implementation

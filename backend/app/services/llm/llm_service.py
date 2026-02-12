"""OpenRouter LLM service implementation."""

from typing import TypeVar

import mlflow
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel, ValidationError

from app.core.config import settings
from app.core.logging import logger
from app.services.llm.base_llm_service import BaseLLMService

T = TypeVar("T", bound=BaseModel)


class OpenRouterLLMService(BaseLLMService):
    """Concrete implementation of the OpenRouter LLM service."""

    def __init__(
        self,
        model_name: str,
        model_id: str,
        api_key: str,
        router_api: str,
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ):
        """Construct the OpenRouter LLM service."""
        if not api_key:
            raise ValueError("The API key (api_key) is required and was not provided.")
        if not router_api:
            raise ValueError(
                "The API URL (router_api) is required and was not provided."
            )

        self.model_name = model_name
        self.model_id = model_id
        self.client = AsyncOpenAI(api_key=api_key, base_url=router_api)
        self.temperature = temperature
        self.max_tokens = max_tokens

    @mlflow.trace(name="llm_call", span_type="llm")
    async def call_llm(
        self,
        user_prompt: str,
        schema: type[T] | None = None,
        temperature: float = 0.3,
        max_tokens: int = 4096,
        system_prompt: str | None = None,
        **kwargs,
    ) -> str | T:
        """Unified implementation of the called LLM."""
        # Use mock responses when the LLM is disabled
        if not settings.ENABLE_LLM:
            if schema is None:
                return "Mock markdown response generated when LLM is disabled."
            dummy_response = self._get_mock_response(schema)
            return dummy_response

        try:
            messages: list[ChatCompletionMessageParam] = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt.strip()})
            messages.append({"role": "user", "content": user_prompt})

            logger.debug(
                f"Calling LLM API with model: {self.model_id}, "
                f"prompt length: {len(user_prompt)}, schema: {schema}"
            )

            if schema is None:
                # For plain text responses (like markdown), use regular completions
                completion = await self.client.chat.completions.create(
                    model=self.model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                response_content = completion.choices[0].message.content
                if response_content is None:
                    raise ValueError("LLM returned None response")
                return response_content
            else:
                # For structured responses, use parse
                completion = await self.client.beta.chat.completions.parse(
                    model=self.model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    response_format=schema,
                )
                validated_response = completion.choices[0].message.parsed
                if validated_response is None:
                    raise ValueError("LLM returned None response")
                return validated_response

        except ValidationError as e:
            error_msg = (
                f"LLM response failed Pydantic validation for schema {schema}: {e}"
            )
            logger.error(f"[VALIDATION ERROR]: {error_msg}")
            raise ValueError(error_msg) from e
        except Exception as e:
            error_msg = (
                f"Cannot query model '{self.model_name}' or process response: {str(e)}"
            )
            logger.error(f"[API ERROR]: {error_msg}")
            raise ValueError(error_msg) from e

    def _get_mock_response(self, schema: type[T]) -> T:
        """Generate mock response for testing when LLM is disabled."""
        try:
            # Try to create instance with empty data
            if hasattr(schema, "model_validate"):
                # Handle schemas that require specific fields, like MarkdownReport
                if (
                    "content" in schema.model_fields
                    and schema.model_fields["content"].is_required()
                ):
                    return schema.model_validate(
                        {"content": "Mock content for report."}
                    )
                else:
                    return schema.model_validate({})
            else:
                return schema()
        except Exception as e:
            logger.error(f"Error creating mock for schema {schema}: {e}")
            raise ValueError(f"Mock not defined for schema: {schema}") from e

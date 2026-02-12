"""Base class for LLM services."""

from abc import ABC, abstractmethod
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseLLMService(ABC):
    """Interface abstract for LLM services."""

    @abstractmethod
    async def call_llm(
        self, user_prompt: str, schema: type[T] | None = None, **kwargs
    ) -> str | T:
        """Call the LLM with optional prompt and schema."""
        pass

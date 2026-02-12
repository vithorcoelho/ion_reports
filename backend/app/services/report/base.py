"""Base definitions for report generation strategies."""

from abc import ABC, abstractmethod

from app.domain.exam_configs.base_config import BaseExamConfig
from app.services.llm.base_prompt_registry import BasePromptRegistry
from app.services.llm.llm_service import BaseLLMService


class BaseReportStrategy(ABC):
    """Schema to config report."""

    def __init__(
        self, exam_config: BaseExamConfig, services: dict, alias: str = "production"
    ):
        """Initialize the Base Report."""
        self.exam_config = exam_config  # Injected via constructor
        llm_service = services.get("llm_service")
        if not llm_service:
            raise ValueError("llm_service not found in services dictionary")
        self.llm_service: BaseLLMService = llm_service
        prompt_registry = services.get("prompt_registry")
        if not prompt_registry:
            raise ValueError("prompt_registry not found in services dictionary")
        self.prompt_registry: BasePromptRegistry = prompt_registry
        self.alias = alias

    @abstractmethod
    async def execute(self, exam_data, anamnesis, kg_data) -> str:
        """Execute report generation."""
        pass

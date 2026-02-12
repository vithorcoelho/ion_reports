"""Base class for prompt evaluation strategies.

This module provides the abstract base class for implementing different
prompt evaluation strategies using MLflow GenAI metrics.
"""

from abc import ABC, abstractmethod
from typing import Any


class BasePromptEvaluator(ABC):
    """Abstract base class for prompt evaluation strategies.

    This class defines the interface that all prompt evaluation strategies
    must implement to provide consistent evaluation capabilities.
    """

    @abstractmethod
    def evaluate(
        self, strategy_results: dict[str, list[Any]], test_data: list[Any]
    ) -> dict[str, dict[str, Any]]:
        """Evaluate prompt strategies against test data.

        Args:
            strategy_results: Dictionary mapping strategy names to their outputs
            test_data: List of test data samples for evaluation

        Returns:
            Dictionary mapping strategy names to evaluation results

        Raises:
            NotImplementedError: If the method is not implemented by subclasses

        """
        raise NotImplementedError("Subclasses must implement the evaluate method")

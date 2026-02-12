"""Unit tests for the MLflowPromptEvaluator service."""

import pytest

from app.services.llm.prompt_evaluator import MLflowPromptEvaluator


class TestMLflowPromptEvaluator:
    """Test cases for MLflowPromptEvaluator."""

    def test_initialization(self, mocker):
        """Test initialization with default experiment name."""
        mock_configure = mocker.patch(
            "app.services.llm.prompt_evaluator.configure_mlflow"
        )
        mock_mlflow = mocker.patch("app.services.llm.prompt_evaluator.mlflow")

        evaluator = MLflowPromptEvaluator()

        mock_configure.assert_called_once()
        mock_mlflow.set_experiment.assert_called_once_with("medical-prompts-v1")
        assert evaluator.experiment_name == "medical-prompts-v1"

    def test_initialization_custom_experiment(self, mocker):
        """Test initialization with custom experiment name."""
        mock_configure = mocker.patch(
            "app.services.llm.prompt_evaluator.configure_mlflow"
        )
        mock_mlflow = mocker.patch("app.services.llm.prompt_evaluator.mlflow")

        evaluator = MLflowPromptEvaluator(experiment_name="custom")

        mock_configure.assert_called_once()
        mock_mlflow.set_experiment.assert_called_once_with("custom")
        assert evaluator.experiment_name == "custom"

    def test_evaluate_success(self, mocker):
        """Test successful evaluation."""
        # Mock dependencies
        mocker.patch("app.services.llm.prompt_evaluator.configure_mlflow")
        mock_mlflow = mocker.patch("app.services.llm.prompt_evaluator.mlflow")
        mock_make_metric = mocker.patch(
            "app.services.llm.prompt_evaluator.make_genai_metric"
        )
        
        # Mock settings
        mock_settings = mocker.patch("app.services.llm.prompt_evaluator.settings")
        mock_settings.OPENROUTER_API_KEY = "test-key"  # pragma: allowlist secret

        # Mock MLflow evaluation result
        mock_result = mocker.Mock()
        mock_result.metrics = {"medical_completeness/v1/mean": 4.2}
        mock_mlflow.evaluate.return_value = mock_result
        mock_make_metric.return_value = mocker.Mock()

        # Test data
        strategy_results = {"strategy_a": ["output1", "output2"]}
        test_data = [
            {"inputs": {}, "targets": "target1"},
            {"inputs": {}, "targets": "target2"},
        ]

        # Execute
        evaluator = MLflowPromptEvaluator()
        results = evaluator.evaluate(strategy_results, test_data)

        # Verify
        assert "strategy_a" in results
        assert results["strategy_a"]["score"] == 4.2
        assert (
            results["strategy_a"]["evaluation_method"] == "genai_medical_completeness"
        )

    def test_evaluate_empty_inputs(self, mocker):
        """Test evaluation with empty inputs raises ValueError."""
        mocker.patch("app.services.llm.prompt_evaluator.configure_mlflow")

        evaluator = MLflowPromptEvaluator()

        with pytest.raises(ValueError, match="strategy_results cannot be empty"):
            evaluator.evaluate({}, [])

        with pytest.raises(ValueError, match="test_data cannot be empty"):
            evaluator.evaluate({"strategy": ["output"]}, [])

    def test_evaluate_strategy_with_no_outputs(self, mocker):
        """Test evaluation when strategy has no outputs."""
        mocker.patch("app.services.llm.prompt_evaluator.configure_mlflow")
        mock_logger = mocker.patch("app.services.llm.prompt_evaluator.logger")

        evaluator = MLflowPromptEvaluator()
        results = evaluator.evaluate(
            {"empty_strategy": []}, [{"inputs": {}, "targets": "target"}]
        )

        # Should log warning and return error result
        mock_logger.warning.assert_called_with(
            "Strategy 'empty_strategy' has no outputs"
        )
        assert "empty_strategy" in results
        assert results["empty_strategy"]["score"] == 0.0
        assert "error" in results["empty_strategy"]

"""MLflow-based prompt evaluation service.

This module provides MLflow GenAI evaluation capabilities for assessing
prompt effectiveness using standardized metrics.
"""

from typing import Any

import mlflow
import pandas as pd
from mlflow.metrics.genai import make_genai_metric

from app.core.config import configure_mlflow, settings
from app.core.logging import logger
from app.services.llm.base_prompt_evaluator import BasePromptEvaluator


class MLflowPromptEvaluator(BasePromptEvaluator):
    """MLflow-based prompt evaluation service using GenAI metrics."""

    def __init__(self, experiment_name: str = "medical-prompts-v1"):
        """Initialize the MLflow prompt evaluator focused on GenAI medical completeness."""
        # Configure MLflow with proper AWS credentials
        configure_mlflow()

        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)

    def evaluate(
        self, strategy_results: dict[str, list[Any]], test_data: list[Any]
    ) -> dict[str, dict[str, Any]]:
        """Evaluate prompt strategies using GenAI medical completeness metrics.

        Args:
            strategy_results: Dictionary mapping strategy names to their outputs
            test_data: List of test data samples for evaluation

        Returns:
            Dictionary mapping strategy names to evaluation results

        Raises:
            ValueError: If inputs are invalid or empty

        """
        if not strategy_results:
            raise ValueError("strategy_results cannot be empty")

        if not test_data:
            raise ValueError("test_data cannot be empty")

        results = {}

        for strategy_name, outputs in strategy_results.items():
            # Check if strategy has outputs
            if not outputs:
                logger.warning(f"Strategy '{strategy_name}' has no outputs")
                results[strategy_name] = {
                    "score": 0.0,
                    "metrics": {},
                    "error": "No outputs provided for evaluation",
                    "evaluation_method": "error",
                    "num_test_cases": len(test_data),
                    "num_outputs": 0,
                }
                continue

            try:
                with mlflow.start_run(run_name=f"strategy-eval-{strategy_name}"):
                    mlflow.log_param("strategy_name", strategy_name)
                    mlflow.log_param("num_test_cases", len(test_data))
                    mlflow.log_param("num_outputs", len(outputs))

                    # Focus on GenAI medical completeness only
                    main_score, metrics = self._evaluate_medical_completeness(
                        outputs, test_data
                    )

                    mlflow.log_metric("medical_completeness_score", main_score)

                    # Log additional metrics if available
                    for metric_name, metric_value in metrics.items():
                        if isinstance(metric_value, int | float):
                            mlflow.log_metric(metric_name, metric_value)

                    results[strategy_name] = {
                        "score": main_score,
                        "metrics": metrics,
                        "evaluation_method": "genai_medical_completeness",
                        "num_test_cases": len(test_data),
                        "num_outputs": len(outputs),
                    }
                    logger.info(
                        f"Evaluated strategy '{strategy_name}': medical_completeness={main_score:.3f}"
                    )

            except Exception as e:
                logger.error(f"Error evaluating strategy '{strategy_name}': {str(e)}")
                results[strategy_name] = {
                    "score": 0.0,
                    "metrics": {},
                    "error": str(e),
                    "evaluation_method": "error",
                    "num_test_cases": len(test_data),
                    "num_outputs": len(outputs) if outputs else 0,
                }

        return results

    def _evaluate_medical_completeness(
        self, outputs: list[str], test_data: list[Any]
    ) -> tuple[float, dict[str, float]]:
        """Evaluate using GenAI medical completeness metric only.

        Args:
            outputs: List of generated outputs to evaluate
            test_data: List of test data samples

        Returns:
            Tuple of (main_score, metrics_dict)

        Raises:
            ValueError: If outputs and test_data have mismatched lengths
            RuntimeError: If MLflow evaluation fails

        """
        if len(outputs) != len(test_data):
            raise ValueError(
                f"Outputs length ({len(outputs)}) must match test_data length ({len(test_data)})"
            )

        # Validate API key is available (using OpenRouter API key as OPENAI_API_KEY)
        if not settings.OPENROUTER_API_KEY:
            raise RuntimeError("OPENROUTER_API_KEY is required for evaluation")

        try:
            # Ensure MLflow tracking URI is set (might be reset by subprocess)
            mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
            logger.debug(f"MLflow tracking URI: {mlflow.get_tracking_uri()}")

            eval_df = pd.DataFrame(
                {
                    "inputs": [item.get("inputs", {}) for item in test_data],
                    "predictions": outputs,
                    "targets": [item.get("targets", "") for item in test_data],
                }
            )

            medical_completeness_metric = make_genai_metric(
                name="medical_completeness",
                definition="Avalia se a recomendação médica gerada é completa, cobrindo os três pilares essenciais: dieta, suplementação e estilo de vida/treino, com base no contexto fornecido (anamnese, exames, etc.).",
                grading_prompt=(
                    "Você é um especialista em nutrição funcional. Avalie a completude da recomendação gerada com base no contexto do paciente. "
                    "A recomendação ideal deve abordar dieta, suplementos e estilo de vida/treino de forma integrada.\n\n"
                    "Critérios de pontuação:\n"
                    "- 1: A recomendação é irrelevante ou ignora completamente os dados do paciente.\n"
                    "- 2: A recomendação aborda apenas um dos três pilares (dieta, suplementos, ou estilo de vida) de forma superficial.\n"
                    "- 3: A recomendação aborda dois dos três pilares ou aborda os três de forma muito genérica.\n"
                    "- 4: A recomendação aborda os três pilares (dieta, suplementos, estilo de vida), mas poderia ser mais específica ou integrada.\n"
                    "- 5: A recomendação é perfeitamente completa, integrando de forma clara e específica as orientações de dieta, suplementação e estilo de vida/treino, baseadas no contexto do paciente."
                ),
                version="v1",
                model=f"openai:/{settings.OPENROUTER_MODEL}",  # Pass full OpenRouter model: "openai:/openai/gpt-4o-mini"
                parameters={"temperature": 0.0},
                aggregations=["mean"],
                greater_is_better=True,
            )

            eval_result = mlflow.evaluate(
                data=eval_df,
                predictions="predictions",
                extra_metrics=[medical_completeness_metric],
            )

            metrics = eval_result.metrics
            main_score = metrics.get("medical_completeness/v1/mean", 0.0)

            return main_score, metrics

        except Exception as e:
            logger.error(f"Error in medical completeness evaluation: {str(e)}")
            raise RuntimeError(f"MLflow evaluation failed: {str(e)}") from e

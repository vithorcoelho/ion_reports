"""MLflow Prompt Development CLI.

CLI for registering prompts in MLflow.
Supports both ionnutri and vidanova exam types with multistage/onestage strategies.
"""

import asyncio
import json
import sys
from pathlib import Path

import pandas as pd
import typer
from dotenv import load_dotenv
from mlflow import MlflowClient

# Load environment variables from .env file BEFORE importing app modules
PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")

# Import app modules after loading environment variables
from app.core.config import configure_mlflow, settings  # noqa: E402
from app.db.neo4j_client import Neo4jClient  # noqa: E402
from app.domain.kg_result import KGResult  # noqa: E402
from app.schemas.exam import TNMExamData  # noqa: E402
from app.schemas.patient_anamnesis import PatientAnamnesis  # noqa: E402
from app.services.kg.kg_service import KnowledgeGraphService  # noqa: E402
from app.services.llm.llm_service import OpenRouterLLMService  # noqa: E402
from app.services.llm.prompt_evaluator import MLflowPromptEvaluator  # noqa: E402
from app.services.llm.prompt_registry import MLflowPromptRegistry  # noqa: E402
from app.services.report.strategy_factory import StrategyFactory  # noqa: E402

sys.path.append(str(PROJECT_ROOT))

configure_mlflow()

app = typer.Typer(
    name="prompt-dev", help="MLflow Prompt Development CLI", no_args_is_help=True
)
PROMPTS_BASE_PATH = PROJECT_ROOT / "app/scripts/report/prompts"
DEFAULT_VERSION = "1.0.0"
DEFAULT_ALIAS = "production"


class PromptRegistryError(Exception):
    """Exception for prompt registry operations."""


core_registry = MLflowPromptRegistry(PROMPTS_BASE_PATH)


@app.command()
def register(exam_type: str, section: str, version: str = DEFAULT_VERSION):
    """Register prompt at CLI."""
    try:
        prompt = core_registry.register_from_repo(
            exam_type, section, alias="current", metadata={"version": version}
        )
        typer.echo(f"Prompt registrado: {prompt.name} v{prompt.version}")
    except PromptRegistryError as e:
        typer.echo(f"Erro: {e}")
        raise typer.Exit(1) from None


@app.command()
def list_prompts(exam_type: str):
    """List prompts at CLE."""
    prompts = core_registry.list_prompts(prefix=f"prompt_{exam_type}_")
    if not prompts:
        typer.echo("Nenhum prompt registrado.")
        return
    for p in prompts:
        aliases = ", ".join(p.get("aliases", [])) or "none"
        typer.echo(f"{p['name']}: v{p['version']} (aliases: {aliases})")


@app.command()
def promote(exam_type: str, section: str, version: str, alias: str = DEFAULT_ALIAS):
    """Validate sections for prompts."""
    try:
        name = f"prompt_{exam_type}_{section}"
        core_registry.promote_prompt(name, version, alias)
        typer.echo(f"Prompt promovido: {name} v{version} → @{alias}")
    except PromptRegistryError as e:
        typer.echo(f"Erro: {e}")
        raise typer.Exit(1) from None


@app.command()
def evaluate(
    exam_type: str = typer.Option("ionnutri", help="Exam type: ionnutri or vidanova"),
    all_strategies: bool = typer.Option(
        False, "--all-strategies", help="Evaluate all strategies"
    ),
    strategy_type: str = typer.Option(
        None, "--strategy-type", help="Specific strategy type to evaluate"
    ),
    test_data_file: str = typer.Option(
        None, "--test-data", help="Path to test data JSON file"
    ),
    output_file: str = typer.Option(None, "--output", help="Output file for results"),
):
    """Evaluate prompt strategies using MLflow GenAI metrics.

    This command evaluates different prompt strategies against test data using
    MLflow's built-in GenAI evaluation metrics. Supports both individual strategy
    evaluation and comparative analysis across all strategies.
    """
    asyncio.run(
        _evaluate_async(
            exam_type,
            all_strategies,
            strategy_type,
            test_data_file,
            output_file,
        )
    )


async def _evaluate_async(
    exam_type: str,
    all_strategies: bool,
    strategy_type: str,
    test_data_file: str,
    output_file: str,
):
    """Async implementation of strategy evaluation."""
    typer.echo("🚀 Starting strategy evaluation...")
    typer.echo(f"Exam Type: {exam_type}")

    if all_strategies:
        typer.echo("Strategy: ALL (multistage vs onestage)")
    elif strategy_type:
        typer.echo(f"Strategy: {strategy_type}")
    else:
        typer.echo("⚠️  Please specify either --all-strategies or --strategy-type")
        raise typer.Exit(1)

    try:
        # Load test data
        if test_data_file:
            with open(test_data_file, encoding="utf-8") as f:
                test_data = json.load(f)
        else:
            # Use default sample data
            test_data = _get_default_test_data(exam_type)

        typer.echo(f"✅ Loaded {len(test_data)} test cases")

        # Initialize evaluator
        evaluator = MLflowPromptEvaluator()

        # Determine strategies to evaluate
        if all_strategies:
            strategies_to_eval = ["multistage", "onestage"]
        else:
            strategies_to_eval = [strategy_type]

        # Execute real strategies and generate results
        strategy_results = {}

        # Initialize services
        strategy_factory = StrategyFactory()
        neo4j_client = Neo4jClient()
        kg_service = KnowledgeGraphService(neo4j_client)
        llm_service = OpenRouterLLMService(
            model_name=settings.OPENROUTER_MODEL_NAME,
            model_id=settings.OPENROUTER_MODEL,
            api_key=settings.OPENROUTER_API_KEY,
            router_api=settings.OPENROUTER_API_BASE,
            temperature=settings.OPENROUTER_TEMPERATURE,
            max_tokens=settings.OPENROUTER_MAX_TOKENS,
        )

        for strategy in strategies_to_eval:
            typer.echo(f"🔍 Evaluating {strategy} strategy...")

            # Use MLflowPromptRegistry directly
            prompt_registry = MLflowPromptRegistry(PROMPTS_BASE_PATH)

            # Create strategy instance
            services = {
                "kg_service": kg_service,  # This is a stub, should be replaced with real service
                "prompt_registry": prompt_registry,
                "llm_service": llm_service,
            }

            strategy_instance = strategy_factory.create_strategy(
                exam_type, strategy, services
            )

            # Execute strategy for each test case
            strategy_outputs = []
            for i, test_case in enumerate(test_data):
                try:
                    typer.echo(f"  Processing test case {i + 1}/{len(test_data)}...")

                    # Extract structured data from the test case
                    inputs_data = test_case.get("inputs", {})
                    exam_data_dict = inputs_data.get("exam_data", {})
                    anamnesis_dict = inputs_data.get("anamnesis", {})

                    # The KG service expects Pydantic models, but for this script,
                    # we can convert them to the expected schema on the fly.
                    # The service's type hints (TNMExamData, PatientAnamnesis) will handle this.
                    exam_data_model = TNMExamData.model_validate(exam_data_dict)
                    anamnesis_model = PatientAnamnesis.model_validate(anamnesis_dict)
                    try:
                        kg_data = await kg_service.get_knowledge_data(
                            exam_data_model, anamnesis_model
                        )
                    except Exception as kg_error:
                        # If KG fails (e.g., due to schema mismatch in test data),
                        # we can still proceed with an empty KG context for evaluation purposes.
                        typer.echo(
                            f"  ⚠️  Warning: KG service failed: {kg_error}. Proceeding with empty KG data."
                        )
                        kg_data = KGResult()

                    # Execute strategy (async)
                    # The strategy also expects dictionaries or Pydantic models.
                    result = await strategy_instance.execute(
                        exam_data_dict, anamnesis_dict, kg_data
                    )
                    strategy_outputs.append(
                        str(result)
                    )  # Ensure result is a string for the evaluator

                except Exception as e:
                    typer.echo(f"  ⚠️  Error in test case {i + 1}: {str(e)}")
                    strategy_outputs.append(f"Error: {str(e)}")

            strategy_results[strategy] = strategy_outputs

        # Evaluate strategies
        typer.echo("📊 Running MLflow GenAI evaluation...")
        results = evaluator.evaluate(strategy_results, test_data)

        # Display results
        typer.echo("\n📈 Strategy Evaluation Results:")
        typer.echo("=" * 60)

        for strategy_name, result in results.items():
            score = result.get("score", 0.0)
            evaluation_method = result.get("evaluation_method", "unknown")

            typer.echo(f"Strategy: {strategy_name}")
            typer.echo(f"  Overall Score: {score:.3f}")
            typer.echo(f"  Evaluation Method: {evaluation_method}")

            metrics = result.get("metrics", {})

            # Display key metrics first
            key_metrics = [
                "medical_completeness_mean",
                "medical_completeness/v1/mean",
                "avg_prediction_length",
                "error_rate",
            ]

            for key_metric in key_metrics:
                if key_metric in metrics:
                    value = metrics[key_metric]
                    if isinstance(value, int | float) and not pd.isna(value):
                        typer.echo(f"  {key_metric}: {value:.3f}")

            # Display other metrics
            other_metrics = {k: v for k, v in metrics.items() if k not in key_metrics}
            for metric_name, metric_value in other_metrics.items():
                if isinstance(metric_value, int | float) and not pd.isna(metric_value):
                    typer.echo(f"  {metric_name}: {metric_value:.3f}")

            if "error" in result:
                typer.echo(f"  ⚠️  Error: {result['error']}")

            typer.echo()

        # Save results if output file specified
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            typer.echo(f"\nResults saved to {output_file}")

        typer.echo("\n✅ Strategy evaluation completed successfully!")
        typer.echo("📊 Check MLflow UI for detailed metrics and artifacts")

    except FileNotFoundError as e:
        typer.echo(f"❌ Test data file not found: {test_data_file}")
        raise typer.Exit(1) from e
    except json.JSONDecodeError as e:
        typer.echo(f"❌ Invalid JSON in test data file: {e}")
        raise typer.Exit(1) from e
    except Exception as e:
        typer.echo(f"❌ Error during evaluation: {str(e)}")
        raise typer.Exit(1) from e


@app.command()
def status(exam_type: str):
    """List anc check status of a prmopt."""
    prompts = core_registry.list_prompts(prefix=f"prompt_{exam_type}_")
    if not prompts:
        typer.echo("Nenhum prompt registrado.")
        return
    client = MlflowClient()
    for p in prompts:
        try:
            version_info = client.get_model_version_by_alias(p["name"], "latest")
            typer.echo(f"{p['name']}: v{version_info.version} (@latest)")
        except Exception:
            typer.echo(f"{p['name']}: não disponível (@latest)")


def _get_default_test_data(exam_type: str) -> list:
    """Get default test data for evaluation based on exam type."""
    if exam_type == "vidanova":
        # For 'vidanova', load data from specific patient files
        test_cases = []
        patient_ids = ["PP001", "PP020", "PP032"]

        data_base_path = Path(PROJECT_ROOT) / "app" / "scripts"
        input_dir = (
            data_base_path
            / "load_data"
            / "data_to_pass_api"
            / exam_type
            / "complete_data"
        )
        target_dir = data_base_path / "traces" / exam_type

        for patient_id in patient_ids:
            input_file = input_dir / f"{patient_id}.json"
            target_file = target_dir / f"{patient_id}.md"

            if not input_file.exists() or not target_file.exists():
                typer.echo(
                    f"⚠️  Warning: Skipping patient {patient_id} for exam type {exam_type}. Missing input or target file."
                )
                continue

            try:
                with open(input_file, encoding="utf-8") as f:
                    inputs_data = json.load(f)

                with open(target_file, encoding="utf-8") as f:
                    targets_data = f.read()

                test_cases.append(
                    {
                        "inputs": inputs_data,
                        "targets": targets_data,
                        "context": f"Exames e anamnese do paciente {patient_id} e o resultado das necessidades de intervenção.",
                    }
                )
            except Exception as e:
                typer.echo(
                    f"⚠️  Warning: Failed to load data for patient {patient_id}. Error: {e}"
                )

        if not test_cases:
            typer.echo(
                f"❌ Error: No valid default test data found for exam type '{exam_type}'. Please check file paths."
            )
            raise typer.Exit(1)

        return test_cases

    elif exam_type == "ionnutri":
        # For 'ionnutri', use mock data as specific files are not available
        typer.echo("ℹ️  Using mock data for 'ionnutri' evaluation.")
        return [
            {
                "inputs": {
                    "exam_data": {
                        "patient_id": "patient_01",
                        "exam_date": "2025-09-23",
                        "metabolites": [
                            {"name": "Iron", "value": 35, "unit": "μg/dL"},
                            {"name": "Vitamin D", "value": 15, "unit": "ng/mL"},
                        ],
                    },
                    "anamnesis": {
                        "patient_id": "patient_01",
                        "objective": "Improve energy",
                        "personal_data": {"age": 45, "gender": "female"},
                        "context_factors": {
                            "medical_history": ["fatigue", "hair loss"]
                        },
                    },
                },
                "targets": "Findings: Iron deficiency and Vitamin D deficiency. Recommendations: Increase iron-rich foods and supplement with Vitamin D3.",
                "context": "Patient with fatigue and hair loss shows low iron and vitamin D.",
            },
            {
                "inputs": {
                    "exam_data": {
                        "patient_id": "patient_02",
                        "exam_date": "2025-09-23",
                        "metabolites": [
                            {"name": "Magnesium", "value": 1.4, "unit": "mg/dL"},
                            {"name": "Creatine Kinase", "value": 450, "unit": "U/L"},
                        ],
                    },
                    "anamnesis": {
                        "patient_id": "patient_02",
                        "objective": "Improve recovery",
                        "personal_data": {"age": 28, "gender": "male"},
                        "context_factors": {
                            "medical_history": ["muscle cramps", "poor recovery"]
                        },
                    },
                },
                "targets": "Findings: Magnesium deficiency and muscle damage. Recommendations: Supplement with Magnesium and optimize recovery protocols.",
                "context": "Athlete with muscle cramps and high CK shows low magnesium.",
            },
        ]
    else:
        typer.echo(
            f"❌ Error: No default test data configuration for exam type '{exam_type}'."
        )
        raise typer.Exit(1)


if __name__ == "__main__":
    app()

"""Central application configuration (FastAPI, environment variables, etc.)."""

import os

import mlflow
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.logging import logger


class Settings(BaseSettings):
    """Configurações principais da aplicação."""

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Ion Nutri AP"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Server configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # Neo4j configuration
    NEO4J_URI: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "password")

    # OpenRouter LLM configuration
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_API_BASE: str = os.getenv(
        "OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"
    )
    OPENROUTER_MODEL: str = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    OPENROUTER_MODEL_NAME: str = os.getenv("OPENROUTER_MODEL_NAME", "gpt-4o-mini")
    OPENROUTER_MAX_TOKENS: int = int(os.getenv("OPENROUTER_MAX_TOKENS", "4096"))
    OPENROUTER_TEMPERATURE: float = float(os.getenv("OPENROUTER_TEMPERATURE", "0.1"))

    # OpenAI/OpenRouter compatible configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

    # Application paths
    ONTOLOGY_DIR: str = os.getenv("ONTOLOGY_DIR", "./data/ontologies")
    REPORT_TEMPLATE_PATH: str = os.getenv(
        "REPORT_TEMPLATE_PATH", "./docs/templates/tnm.md"
    )
    PROMPT_REGISTRY_PATH: str = os.getenv(
        "PROMPT_REGISTRY_PATH", "app/scripts/report/prompts"
    )

    # MLflow Configuration
    MLFLOW_ENABLED: bool = os.getenv("MLFLOW_ENABLED", "False").lower() == "true"
    MLFLOW_TRACKING_URI: str = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    MLFLOW_EXPERIMENT_NAME: str = os.getenv(
        "MLFLOW_EXPERIMENT_NAME", "ion-nutri-reports"
    )

    # MLflow S3 Configuration (MinIO)
    MLFLOW_S3_ENDPOINT_URL: str = os.getenv(
        "MLFLOW_S3_ENDPOINT_URL", "http://localhost:9000"
    )
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "minioadmin")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "minioadmin123")
    AWS_DEFAULT_REGION: str = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    MLFLOW_S3_IGNORE_TLS: str = os.getenv("MLFLOW_S3_IGNORE_TLS", "true")
    MLFLOW_S3_VERIFY_SSL: str = os.getenv("MLFLOW_S3_VERIFY_SSL", "false")
    # Feature flags
    INIT_KNOWLEDGE_BASE: bool = (
        os.getenv("INIT_KNOWLEDGE_BASE", "False").lower() == "true"
    )
    ENABLE_LLM: bool = os.getenv("ENABLE_LLM", "True").lower() == "true"

    # Foi modificado para tratar os warning dos testes
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="allow",  # Permitir variáveis extras
    )


# # Create global settings object
settings = Settings()


def configure_mlflow() -> bool:
    """Configura e inicia o MLflow com as variáveis de ambiente.

    Returns:
        bool: True se MLflow foi configurado com sucesso, False caso contrário.

    """
    if not settings.MLFLOW_ENABLED:
        logger.info("MLflow disabled (MLFLOW_ENABLED=false)")
        # Disable MLflow tracing to prevent @mlflow.trace decorators from connecting
        mlflow.tracing.disable()
        return False

    # Configure MLflow environment variables for MinIO S3
    os.environ.setdefault("MLFLOW_TRACKING_URI", settings.MLFLOW_TRACKING_URI)
    os.environ.setdefault("MLFLOW_S3_ENDPOINT_URL", settings.MLFLOW_S3_ENDPOINT_URL)
    os.environ.setdefault("AWS_ACCESS_KEY_ID", settings.AWS_ACCESS_KEY_ID)
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", settings.AWS_SECRET_ACCESS_KEY)
    os.environ.setdefault("AWS_DEFAULT_REGION", settings.AWS_DEFAULT_REGION)
    os.environ.setdefault("MLFLOW_S3_IGNORE_TLS", settings.MLFLOW_S3_IGNORE_TLS)

    # Always override OPENAI_API_KEY with OPENROUTER_API_KEY for MLflow GenAI metrics
    os.environ["OPENAI_API_KEY"] = settings.OPENROUTER_API_KEY
    os.environ["OPENAI_BASE_URL"] = settings.OPENROUTER_API_BASE

    # Verify AWS credentials are properly set if using an S3 backend
    if settings.MLFLOW_S3_ENDPOINT_URL and not settings.AWS_SECRET_ACCESS_KEY:
        logger.warning(
            "AWS_SECRET_ACCESS_KEY not found. MLflow may fail if using S3 backend."
        )

    try:
        mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
        mlflow.set_experiment(settings.MLFLOW_EXPERIMENT_NAME)
        mlflow.openai.autolog()
        mlflow.tracing.enable()
        logger.info(f"MLflow configured successfully: {settings.MLFLOW_TRACKING_URI}")
        return True
    except Exception as e:
        logger.warning(
            f"Failed to configure MLflow: {e}. Continuing without MLflow tracking."
        )
        settings.MLFLOW_ENABLED = False
        mlflow.tracing.disable()
        return False

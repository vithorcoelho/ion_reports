"""Guide to create prompt registry using MLflow Prompt Registry."""

from pathlib import Path
from string import Template

import mlflow

from app.services.llm.base_prompt_registry import (
    BasePromptRegistry,
    PromptRegistryError,
    PromptTemplate,
)


class MLflowPromptTemplate(PromptTemplate):
    """MLflow-based prompt template implementation."""

    def __init__(self, content: str):
        """Initialize prompt template with content."""
        # Use a safe template that doesn't raise errors for missing keys
        self.template = Template(content.replace("{{", "${").replace("}}", "}"))

    def format(self, **kwargs) -> str:
        """Format the prompt with provided context."""
        # Convert all values to string to be safe
        str_kwargs = {k: str(v) for k, v in kwargs.items()}
        return self.template.safe_substitute(str_kwargs)


class MLflowPromptRegistry(BasePromptRegistry):
    """MLflow-based implementation of the Prompt Registry."""

    def __init__(self, repo_base: Path):
        """Init MlFlow Class."""
        self.repo_base = repo_base

    def register_from_repo(
        self, name: str, prompt_text: str, alias="current", metadata=None
    ):
        """Register prompt directly from text + metadata."""
        prompt = mlflow.register_prompt(name=name, template=prompt_text)
        if alias:
            mlflow.genai.set_prompt_alias(
                name=name, version=prompt.version, alias=alias
            )
        return prompt

    def list_prompts(self, prefix=None):
        """List prompts according to prefix using mlflow.genai.load_prompt."""
        prompts = []
        for prompt_file in self.repo_base.glob(
            "*.txt"
        ):  # Ajuste conforme a extensão usada
            prompt_name = prompt_file.stem
            if prefix and not prompt_name.startswith(prefix):
                continue

            try:
                prompt_content = mlflow.load_prompt(f"mlflow://{prompt_name}@current")
            except Exception:
                prompt_content = None

            prompts.append(
                {
                    "name": prompt_name,
                    "version": "unknown",  # MLflow GenAI não retorna versão ao carregar
                    "aliases": ["current"],  # ajuste conforme o uso de aliases
                    "metadata": {
                        "content_preview": prompt_content[:100]
                        if prompt_content
                        else None
                    },
                }
            )

        return prompts

    def promote_prompt(self, name: str, version: str, alias: str):
        """Set alias for a prompt."""
        try:
            mlflow.genai.set_prompt_alias(name=name, version=version, alias=alias)
            return True
        except Exception as e:
            raise PromptRegistryError(
                f"Failed to promote {name} v{version} → @{alias}: {e}"
            ) from e

    def load_prompt_by_uri(self, prompt_uri: str) -> PromptTemplate:
        """Load a prompt template by URI."""
        # Parse URI: "vidanova_onestage_complete@production" -> name="vidanova_onestage_complete", alias="production"
        if "@" in prompt_uri:
            name, alias = prompt_uri.split("@", 1)
        else:
            name = prompt_uri
            alias = "current"

        # Try to load from file system
        prompt_file = self.repo_base / f"{name.replace('_', '/')}.txt"
        if prompt_file.exists():
            with open(prompt_file, encoding="utf-8") as f:
                content = f.read()
            return MLflowPromptTemplate(content)

        raise PromptRegistryError(f"Prompt not found: {prompt_uri}")

    def register_prompt(
        self,
        name: str,
        prompt_text: str,
        version: str | None = None,
        alias: str | None = None,
        metadata: dict | None = None,
    ) -> None:
        """Register a new version of a prompt."""
        prompt = mlflow.register_prompt(name=name, template=prompt_text)
        if alias:
            mlflow.genai.set_prompt_alias(
                name=name, version=prompt.version, alias=alias
            )

    def get_prompt_metadata(self, name: str, version: str | None = None) -> dict:
        """Get metadata for a prompt version."""
        return {"name": name, "version": version or "latest", "status": "active"}

    def list_versions(self, name: str) -> list[str]:
        """List all versions of a given prompt."""
        return ["latest"]

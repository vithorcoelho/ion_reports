"""Base class for prompt registry services."""

from abc import ABC, abstractmethod
from string import Template


class PromptTemplate(ABC):
    """Abstract base class for a format-able prompt template."""

    @abstractmethod
    def format(self, **kwargs) -> str:
        """Format the prompt with the provided arguments."""
        pass


class SimplePromptTemplate(PromptTemplate):
    """Concrete PromptTemplate using python's string.Template.

    Converts Jinja-like {{var}} into ${var} and uses safe_substitute so missing
    keys don't raise exceptions.
    """

    def __init__(self, content: str):
        # Use a safe template that doesn't raise errors for missing keys
        self.template = Template(content.replace("{{", "${").replace("}}", "}"))

    def format(self, **kwargs) -> str:
        str_kwargs = {k: str(v) for k, v in kwargs.items()}
        return self.template.safe_substitute(str_kwargs)


class BasePromptRegistry(ABC):
    """Abstract base class for a prompt registry."""

    @abstractmethod
    def load_prompt_by_uri(self, prompt_uri: str) -> str:
        """Load the content of a prompt from a given URI.

        Example:
            mlflow://summarizer@production

        """
        pass

    @abstractmethod
    def register_prompt(
        self,
        name: str,
        prompt_text: str,
        version: str | None = None,
        alias: str | None = None,
        metadata: dict | None = None,
    ) -> None:
        """Register a new version of a prompt."""
        pass

    @abstractmethod
    def get_prompt_metadata(self, name: str, version: str | None = None) -> dict:
        """Get metadata for a prompt version."""
        pass

    @abstractmethod
    def list_versions(self, name: str) -> list[str]:
        """List all versions of a given prompt."""
        pass


class PromptRegistryError(Exception):
    """Exception for prompt registry operations."""

    pass

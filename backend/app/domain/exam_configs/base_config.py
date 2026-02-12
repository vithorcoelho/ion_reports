"""Base definitions for exam configuration interfaces."""

from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseExamConfig(ABC):
    """Base exam schema to create exam configurations."""

    @abstractmethod
    def get_section_schemas(self) -> dict[str, type[BaseModel]]:
        """Pegar schemas."""
        ...

    @abstractmethod
    def get_exam_type(self) -> str:
        """Catch type."""
        ...

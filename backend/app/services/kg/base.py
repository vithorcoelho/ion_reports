"""Base class for Knowledge Graph services."""

from abc import ABC, abstractmethod

from app.domain.kg_result import KGResult
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis


class BaseKnowledgeGraphService(ABC):
    """Abstract interface for Knowledge Graph services."""

    @abstractmethod
    async def get_knowledge_data(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis
    ) -> KGResult:
        """Get knowledge data from the knowledge graph."""
        pass

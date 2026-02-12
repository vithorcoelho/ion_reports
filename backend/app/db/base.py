"""Base interfaces for database clients and knowledge graph builders.

This module defines abstract base classes that establish contracts for
database operations and knowledge graph management.
"""

from abc import ABC, abstractmethod
from typing import Any

from app.domain.kg_result import KGResult
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis


class IDatabaseClient(ABC):  # pragma: no cover
    """Abstract interface for asynchronous database clients.

    This class defines the basic structure that any database client must follow,
    requiring the implementation of methods to verify the connection, execute queries, and close the connection.
    """

    @abstractmethod
    async def verify_connection(self):
        """Verify database connection."""
        pass

    @abstractmethod
    async def execute_query(self, query: str, **params):
        """Execute database query."""
        pass

    @abstractmethod
    async def close(self):
        """Close database connection."""
        pass


class IknowledgeGraphBuilder(ABC):  # pragma: no cover
    """Interface for building knowledge graphs.

    Defines the methods that any implementer of a knowledge graph builder
    must provide: load ontology, build the knowledge base, and execute queries.
    """

    @abstractmethod
    async def load_ontology(self, ontology_file_path: str) -> dict[str, Any]:
        """Load ontology from file."""
        pass

    @abstractmethod
    async def create_relationships(
        self,
        json_content: str,
        source_entity: str,
        target_entity: str,
        relationship_type: str,
        relationship_key: str,
    ) -> int:
        """Create relationships between nodes in Neo4j from a JSON input using APOC procedures.

        Args:
            json_content (str): JSON string containing source nodes and their related target node IDs.
            source_entity (str): Key in the JSON for the source nodes.
            target_entity (str): Key in the JSON for the target nodes.
            relationship_type (str): Type of relationship to create.
            relationship_key (str): Key in the source node for related target node IDs.

        Returns:
            int: Number of relationships created.

        """
        pass

    @abstractmethod
    async def create_nodes(
        self,
        json_content: str,
        entity_type: str,
        node_label: str,
    ) -> int:
        """Create nodes in the Neo4j database from a JSON string using APOC procedures.

        Args:
            json_content (str): JSON string containing the entities to be created as nodes.
            entity_type (str): The key in the JSON that contains the list of entities.
            node_label (str): The label to assign to the created nodes in Neo4j.

        Returns:
            int: The number of nodes created or matched in the database.

        """
        pass


class IUnifiedQuery(ABC):  # pragma: no cover
    """Interface for unified query operations."""

    @abstractmethod
    async def execute_unified_query(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
    ) -> KGResult:
        """Execute a unified query to the knowledge graph based on the patient's metabolites and anamnesis factors.

        Args:
            exam_data: The exam data containing metabolite information
            anamnesis: The patient's anamnesis data

        Returns:
            KGResult: Structured result containing all knowledge graph data

        """
        pass

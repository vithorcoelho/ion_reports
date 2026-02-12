"""Knowledge Graph service implementation using Neo4j."""

import mlflow

from app.core.logging import logger
from app.db.neo4j_client import Neo4jClient
from app.db.unified_query import Neo4jKnowledgeQuery
from app.domain.kg_result import KGResult
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis
from app.services.kg.base import BaseKnowledgeGraphService


class KnowledgeGraphService(BaseKnowledgeGraphService):
    """Bridge to the existing Neo4j database layer."""

    def __init__(self, neo4j_client: Neo4jClient):
        """Initialize the Knowledge Graph service."""
        self.neo4j_client = neo4j_client
        self.kg_query = Neo4jKnowledgeQuery(neo4j_client)

    @mlflow.trace(name="kg_query", span_type="kg")
    async def get_knowledge_data(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis
    ) -> KGResult:
        """Bridge to the existing database layer.

        Args:
            exam_data: Examination data containing metabolite information
            anamnesis: Anamnesis data of the patient

        Returns:
            KGResult: Structured result of the knowledge graph

        Raises:
            Exception: If there is an error in the knowledge graph query

        """
        try:
            logger.debug(
                f"Executing KG query for patient {exam_data.patient_id} "
                f"with {len(exam_data.metabolites)} metabolites"
            )

            result = await self.kg_query.execute_unified_query(exam_data, anamnesis)

            logger.debug(
                f"KG query completed successfully. "
                f"Found {len(result.metabolite_info)} metabolites, "
                f"{len(result.manifestations)} manifestations, "
                f"{len(result.recommended_interventions)} interventions"
            )

            return result

        except Exception as e:
            error_msg = f"Error executing knowledge graph query: {str(e)}"

            # Return empty result in case of error, do not propagate exception
            return KGResult.create_error_result(error_msg)

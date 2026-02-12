"""Knowledge base query integration module (Neo4j)."""

import logging
from collections import defaultdict
from typing import Any

import mlflow

from app.db.base import IUnifiedQuery
from app.db.neo4j_client import Neo4jClient
from app.domain.kg_result import KGResult
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis


class Neo4jKnowledgeQuery(IUnifiedQuery):
    """Class that executes unified queries on the Neo4j knowledge graph."""

    def __init__(self, neo4j_client: Neo4jClient):
        """Initialize the class with a Neo4j client."""
        self.logger = logging.getLogger(__name__)
        self.client = neo4j_client

    @mlflow.trace(name="KG Query")
    async def execute_unified_query(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis
    ) -> KGResult:
        """Execute a unified query to the knowledge graph based on the patient's metabolites and anamnesis factors.

        Returns:
            KGResult: The structured result containing all the knowledge graph data

        """
        metabolites_data = [
            {
                "name": metabolite.name,
                "value": metabolite.value,
            }
            for metabolite in exam_data.metabolites
        ]

        context_factors = {
            "medical_history": anamnesis.context_factors.medical_history,
            "intolerances": anamnesis.context_factors.intolerances,
            "medications": [med.name for med in anamnesis.context_factors.medications],
            "age": anamnesis.personal_data.age,
            "gender": anamnesis.personal_data.gender,
            "bmi": anamnesis.personal_data.bmi,
            "activity_level": anamnesis.context_factors.physical_activity.intensity,
        }

        query = """
            // Parameters: $metabolites (list of {name, value}), $context (contextual factors)

            // 1. Create a CTE to calculate metabolite status once
            WITH $metabolites AS metabolites
            UNWIND metabolites AS m

            // 2. Match metabolites and calculate status
            MATCH (metab:METABOLITE)
            WHERE toLower(metab.name) = toLower(m.name)

            OPTIONAL MATCH (range:REFERENCE_RANGE)-[:HAS_RANGE]-(metab)

            // 3. Calculate status once and filter abnormal metabolites
            WITH metab, range, m.name AS name, m.value AS value,
                CASE
                    WHEN m.value < range.deficit_severo_max THEN 1
                    WHEN m.value < range.deficit_moderado_max THEN 2
                    WHEN m.value >= range.normal_min AND m.value <= range.normal_max THEN 3
                    WHEN m.value > range.excesso_severo_min THEN 5
                    WHEN m.value > range.excesso_moderado_min THEN 4
                    ELSE 3
                END AS status
            WHERE status <> 3

            // 4. Convert status to string format
            WITH metab, range, name, value, status,
                CASE status
                    WHEN 1 THEN "severe_deficit"
                    WHEN 2 THEN "moderate_deficit"
                    WHEN 4 THEN "moderate_excess"
                    WHEN 5 THEN "severe_excess"
                    ELSE "normal"
                END AS status_str

            // 5. Return metabolite info (one row per metabolite)
            RETURN {
                metabolite_info: [{
                    name: name,
                    value: value,
                    status: status_str,
                    definition: COALESCE(metab.definition, ""),
                    reference_range_min: range.normal_min,
                    reference_range_max: range.normal_max,
                    category: COALESCE(metab.category, "")
                }],
                manifestations: [],
                interventions: [],
                foods: [],
                supplements: [],
                pathways: [],
                evidence: []
            } AS result

            UNION

            // 6. Find related data for abnormal metabolites
            WITH $metabolites AS metabolites
            UNWIND metabolites AS m

            MATCH (metab:METABOLITE)
            WHERE toLower(metab.name) = toLower(m.name)

            OPTIONAL MATCH (range:REFERENCE_RANGE)-[:HAS_RANGE]-(metab)

            // 7. Reuse status calculation (same logic as above)
            WITH metab, range, m.name AS name, m.value AS value,
                CASE
                    WHEN m.value < range.deficit_severo_max THEN 1
                    WHEN m.value < range.deficit_moderado_max THEN 2
                    WHEN m.value >= range.normal_min AND m.value <= range.normal_max THEN 3
                    WHEN m.value > range.excesso_severo_min THEN 5
                    WHEN m.value > range.excesso_moderado_min THEN 4
                    ELSE 3
                END AS status
            WHERE status <> 3

            // 8. Keep status variable for manifestations filtering
            WITH metab, range, name, value, status,
                CASE status
                    WHEN 1 THEN "severe_deficit"
                    WHEN 2 THEN "moderate_deficit"
                    WHEN 4 THEN "moderate_excess"
                    WHEN 5 THEN "severe_excess"
                    ELSE "normal"
                END AS status_str

            // 9. Find manifestations based on status
            OPTIONAL MATCH (metab)-[:CAUSED_BY]->(manif:MANIFESTATION)
            WHERE (status IN [1, 2] AND toLower(manif.type) = "lowlevel")
               OR (status IN [4, 5] AND toLower(manif.type) = "highlevel")

            // 10. Find interventions for manifestations
            OPTIONAL MATCH (manif)-[:TREATED_BY]->(interv:INTERVENTION)

            // 11. Find foods and supplements for interventions
            OPTIONAL MATCH (interv)-[:INCLUDES]->(food:FOOD)
            OPTIONAL MATCH (interv)-[:INCLUDES]->(suppl:SUPPLEMENT)

            // 12. Find affected pathways and evidence
            OPTIONAL MATCH (metab)-[:PARTICIPATES_IN]->(pathway:METABOLIC_PATHWAY)
            OPTIONAL MATCH (evidence:SCIENTIFIC_EVIDENCE)-[:EVIDENCED_BY]->(metab)

            // 13. Return related data only (no metabolite duplication)
            RETURN {
                metabolite_info: [],
                manifestations: CASE WHEN manif IS NOT NULL THEN [manif {
                    .id,
                    .description,
                    metabolite: name,
                    status: status_str
                }] ELSE [] END,
                interventions: CASE WHEN interv IS NOT NULL THEN [interv {.*, metabolite: name}] ELSE [] END,
                foods: CASE WHEN food IS NOT NULL THEN [food {.*, metabolite: name, name: food.description}] ELSE [] END,
                supplements: CASE WHEN suppl IS NOT NULL THEN [suppl {.*, metabolite: name, name: suppl.description}] ELSE [] END,
                pathways: CASE WHEN pathway IS NOT NULL THEN [pathway {.*, metabolite: name}] ELSE [] END,
                evidence: CASE WHEN evidence IS NOT NULL THEN [evidence {.*, metabolite: name}] ELSE [] END
            } AS result
        """

        try:
            result = await self.client.execute_query(
                query, metabolites=metabolites_data, context=context_factors
            )

            if not result:
                return KGResult()

            consolidated_result: dict[str, list[Any]] = defaultdict(list)

            for row in result:
                if result_data := row.get("result"):
                    for key, values in result_data.items():
                        consolidated_result[key].extend(values)

            return KGResult.from_kg_data(consolidated_result)
        except Exception as e:
            self.logger.error(f"Error executing query on the knowledge graph: {e}")
            return KGResult.create_error_result(
                f"Error querying the knowledge graph: {str(e)}"
            )

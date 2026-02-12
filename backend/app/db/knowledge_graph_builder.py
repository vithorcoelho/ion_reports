"""Knowledge graph builder for loading ontology data into Neo4j.

This module provides the KnowledgeGraphBuilder class for loading and managing
ontology data in a Neo4j knowledge graph database. It handles the creation of
nodes, relationships, and provides validation of the loaded data.
"""

import datetime
import json
import os
import time
from typing import Any

from app.core.logging import logger
from app.db.base import IknowledgeGraphBuilder
from app.db.neo4j_client import Neo4jClient
from app.validators.ontology_data_validator import OntologyDataValidator


class KnowledgeGraphBuilder(IknowledgeGraphBuilder):
    """Builder for creating and managing knowledge graphs in Neo4j.

    This class provides functionality to load ontology data from JSON files
    and create corresponding nodes and relationships in a Neo4j knowledge graph.
    It includes validation, error handling, and performance tracking.

    Attributes:
        client (Neo4jClient): Neo4j client instance for database operations.
        _type_mapping (dict): Mapping of entity types for node creation.
        _relationship_mappings (dict): Mapping of relationship types.

    """

    def __init__(self, neo4j_client: Neo4jClient):
        """Initialize the knowledge graph builder with a Neo4j client.

        Args:
            neo4j_client (Neo4jClient): An instance of the Neo4jClient to interact with the Neo4j database.

        Attributes:
            client (Neo4jClient): Stores the provided Neo4j client instance.
            _type_mapping (dict): A mapping of types, initialized by the _get_type_mapping method.
            _relationship_mappings (dict): A mapping of relationships, initialized by the _get_relationship_mappings method.

        """
        self.client = neo4j_client
        self._type_mapping = self._get_type_mapping()
        self._relationship_mappings = self._get_relationship_mappings()

    async def load_ontology(self, file_path: str) -> dict[str, Any]:
        """Asynchronously loads an ontology from a JSON file, creating nodes and relationships in the knowledge graph.

        Args:
            file_path (str): The path to the JSON file containing the ontology data.

        Returns:
            Dict[str, Any]: A dictionary containing the result of the operation, including:
                - "success" (bool): Whether the ontology was loaded successfully.
                - "execution_time" (float): Time taken to execute the operation, in seconds.
                - "nodes_created" (int): Number of nodes created in the knowledge graph.
                - "relationships_created" (int): Number of relationships created in the knowledge graph.
                - "error" (str, optional): Error message if the operation failed.

        Raises:
            Exception: Any exception encountered during the loading process is caught and included in the result.

        Notes:
            - The method reads the ontology from a JSON file, creates nodes for each entity type, and establishes relationships between entities.
            - Uses internal mappings for entity types and relationships.
            - Logs debug information about the creation process and errors.

        """
        start = time.time()
        result: dict[str, Any] = {
            "success": False,
            "execution_time": 0.0,
            "nodes_created": 0,
            "relationships_created": 0,
        }

        backup_file = None  # only used when a modification is started.
        try:
            with open(file_path, encoding="utf-8") as f:
                json_content = f.read()
                parsed_json = json.loads(json_content)

            validator = OntologyDataValidator(parsed_json)
            is_valid, errors = validator.validate()
            if not is_valid:
                result["error"] = f"Validation failed: {errors}"
                return result

            # Now that validation has passed, create the backup
            try:
                backup_file = await self.create_backup()
            except Exception as e:
                result["error"] = f"Erro ao criar backup: {str(e)}"
                return result

            # Create nodes for each entity type
            for entity_type, node_label in self._type_mapping.items():
                nodes_created = await self.create_nodes(
                    json_content, entity_type, node_label
                )
                result["nodes_created"] += nodes_created
                logger.debug(f"Created {nodes_created} {node_label} nodes")

            # Create relationships between entities
            for relationship_mapping in self._relationship_mappings:
                relationships_created = await self.create_relationships(
                    json_content,
                    relationship_mapping["source"],
                    relationship_mapping["target"],
                    relationship_mapping["type"],
                    relationship_mapping["source_key"],
                )
                result["relationships_created"] += relationships_created
                logger.debug(
                    f"Created {relationships_created} {relationship_mapping['type']} relationships"
                )

            result["success"] = True

        except FileNotFoundError:
            result["error"] = f"File not found: {file_path}"

        except json.JSONDecodeError as e:
            result["error"] = f"Invalid JSON format: {str(e)}"

        except Exception as e:
            error_msg = str(e)
            logger.debug(f"Error loading ontology with APOC: {error_msg}")
            result["error"] = error_msg
            if backup_file:
                await self.restore_graph_from_backup(backup_file)
            logger.warning(
                f"Error loading ontology. Backup restored from: {backup_file}"
            )

        result["execution_time"] = time.time() - start
        return result

    async def create_nodes(
        self, json_content: str, entity_type: str, node_label: str
    ) -> int:
        """Create nodes in the Neo4j database from a JSON string using APOC procedures.

        The query performs the following steps:
        1. Parses the input JSON string into a map using `apoc.convert.fromJsonMap`.
        2. Extracts the list of entities of the specified `entity_type` from the parsed data.
        3. Uses `apoc.do.when` to check if the entities list is not null and contains elements:
            - If true, it unwinds the entities list and for each entity:
                - Merges (creates or matches) a node with the given `node_label` and the entity's `id`.
                - Sets all properties from the entity on the node, except for the `id` property, using `apoc.map.clean`.
                - Returns the count of nodes created or matched.
            - If false, returns 0.
        4. Returns the number of nodes created or matched as `nodes_created`.

        Args:
            json_content (str): JSON string containing the entities to be created as nodes.
            entity_type (str): The key in the JSON that contains the list of entities.
            node_label (str): The label to assign to the created nodes in Neo4j.

        Returns:
            int: The number of nodes created or matched in the database.

        """
        query = f"""
            WITH apoc.convert.fromJsonMap($json) AS data
            WITH data.{entity_type} AS entities
            CALL apoc.do.when(
                entities IS NOT NULL AND size(entities) > 0,
                'UNWIND $entities AS entity
                MERGE (n:{node_label} {{id: entity.id}})
                SET n += apoc.map.clean(entity, ["id"], [null])
                RETURN count(n) AS count',
                'RETURN 0 AS count',
                {{entities: entities}}
            ) YIELD value
            RETURN value.count AS nodes_created
        """
        try:
            result = await self.client.execute_query(query, json=json_content)
            return int(result[0].get("nodes_created", 0)) if result else 0
        except Exception as e:
            logger.debug(f"Error creating nodes for {entity_type}: {str(e)}")
            raise

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

        Logic:
            1. Parses the JSON and extracts the list of source entities.
            2. For each source, finds the node by ID.
            3. Extracts related target IDs from the specified key, handling nulls and single/multiple values.
            4. For each target ID, finds the target node and creates a relationship of the given type.
            5. Returns the number of relationships created.

        Returns:
            int: Number of relationships created.

        """
        source_label = self._type_mapping.get(source_entity)
        target_label = self._type_mapping.get(target_entity)

        if not source_label or not target_label:
            return 0

        query = f"""
            WITH apoc.convert.fromJsonMap($json) AS data
            WITH data.{source_entity} AS sources
            CALL apoc.do.when(
                sources IS NOT NULL AND size(sources) > 0,
                '
                UNWIND $sources AS source
                MATCH (s:{source_label} {{id: source.id}})
                WITH s, source,
                    CASE WHEN source.{relationship_key} IS NULL THEN []
                        WHEN size(source.{relationship_key}) > 1 OR source.{relationship_key}[0] IS NOT NULL THEN source.{relationship_key}
                        ELSE [source.{relationship_key}]
                    END AS targets
                UNWIND targets AS target_id
                MATCH (t:{target_label} {{id: target_id}})
                MERGE (s)-[r:{relationship_type}]->(t)
                RETURN count(r) AS total
                ',
                'RETURN 0 AS total',
                {{sources: sources}}
            ) YIELD value
            RETURN value.total AS relationships_created
        """
        try:
            result = await self.client.execute_query(query, json=json_content)
            return int(result[0].get("relationships_created", 0)) if result else 0
        except Exception as e:
            logger.debug(
                f"Error creating relationships for {source_entity}-[{relationship_type}]->{target_entity}: {str(e)}"
            )
            raise

    async def create_constraints(self) -> None:
        """Create uniqueness constraints to ensure that each node with `id` is unique."""
        for label in self._type_mapping.values():
            query = f"CREATE CONSTRAINT IF NOT EXISTS FOR (n:{label}) REQUIRE n.id IS UNIQUE"
            await self.client.execute_query(query)

    def _get_type_mapping(self) -> dict[str, str]:
        """Return a dictionary mapping entity type names from a JSON to their corresponding node labels in Neo4j."""
        return {
            "metabolites": "METABOLITE",
            "metabolic_pathways": "METABOLIC_PATHWAY",
            "manifestations": "MANIFESTATION",
            "interventions": "INTERVENTION",
            "foods": "FOOD",
            "supplements": "SUPPLEMENT",
            "contextual_factors": "CONTEXTUAL_FACTOR",
            "metabolic_profiles": "METABOLIC_PROFILE",
            "scientific_evidence": "SCIENTIFIC_EVIDENCE",
            "nutrients": "NUTRIENT",
            "biomarkers": "BIOMARKER",
            "clinical_conditions": "CLINICAL_CONDITION",
            "reference_ranges": "REFERENCE_RANGE",
            "recommendations": "RECOMMENDATION",
        }

    def _get_relationship_mappings(self) -> list[dict[str, str]]:
        """Define the possible relationships between nodes."""
        return [
            {
                "source": "metabolites",
                "type": "PARTICIPATES_IN",
                "target": "metabolic_pathways",
                "source_key": "metabolic_pathway",
            },
            {
                "source": "metabolites",
                "type": "CAUSED_BY",
                "target": "manifestations",
                "source_key": "manifestations",
            },
            {
                "source": "manifestations",
                "type": "TREATED_BY",
                "target": "interventions",
                "source_key": "intervention",
            },
            {
                "source": "contextual_factors",
                "type": "AFFECTS",
                "target": "metabolites",
                "source_key": "affected_metabolites",
            },
            {
                "source": "metabolic_profiles",
                "type": "CONTAINS",
                "target": "metabolites",
                "source_key": "characteristic_metabolites",
            },
            {
                "source": "interventions",
                "type": "INCLUDES",
                "target": "supplements",
                "source_key": "supplements",
            },
            {
                "source": "interventions",
                "type": "INCLUDES",
                "target": "foods",
                "source_key": "foods",
            },
            {
                "source": "scientific_evidence",
                "type": "EVIDENCED_BY",
                "target": "metabolites",
                "source_key": "metabolite",
            },
            {
                "source": "nutrients",
                "type": "HAS_BIOMARKER",
                "target": "biomarkers",
                "source_key": "biomarkers",
            },
            {
                "source": "biomarkers",
                "type": "HAS_RANGE",
                "target": "reference_ranges",
                "source_key": "reference_range",
            },
            {
                "source": "biomarkers",
                "type": "INDICATES",
                "target": "clinical_conditions",
                "source_key": "clinical_conditions",
            },
            {
                "source": "clinical_conditions",
                "type": "RECOMMENDED_FOR",
                "target": "recommendations",
                "source_key": "recommendation",
            },
            {
                "source": "nutrients",
                "type": "LINKED_TO",
                "target": "clinical_conditions",
                "source_key": "related_conditions",
            },
            {
                "source": "metabolites",
                "type": "HAS_RANGE",
                "target": "reference_ranges",
                "source_key": "reference_range",
            },
        ]

    async def create_backup(self) -> str:
        """Export the current state of the database to a Cypher file using APOC.

        Args:
            backup_file_path (str): The path where the Cypher backup file will be saved.

        """
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        backup_dir = os.path.join(os.getcwd(), "backups", "neo4j_backups")
        os.makedirs(backup_dir, exist_ok=True)

        backup_filename = f"kg_backup_{timestamp}.cypher"
        full_backup_path = os.path.join(backup_dir, backup_filename)

        export_relative_path = f"export/{backup_filename}"

        query = """
        CALL apoc.export.cypher.all($file, {
            useOptimizations: {type: "UNWIND_BATCH", unwindBatchSize: 20},
            format: "cypher-shell",
            cypherFormat: "create"
        })
        """

        try:
            async with self.client.session() as session:
                result = await session.run(
                    query, parameters={"file": export_relative_path}
                )
                summary = await result.single()
                logger.info(f"Backup criado com sucesso: {summary}")
        except Exception as e:
            logger.error(f"Erro ao criar backup: {e}")
            return ""

        logger.info(f"Backup salvo em: {full_backup_path}")
        return full_backup_path

    async def restore_graph_from_backup(self, backup_file: str) -> None:
        """Restore the graph by deleting the current state and executing Cypher commands from the backup file."""
        try:
            logger.warning(f"Restoring graph from backup: {backup_file}")
            await self.client.execute_query("MATCH (n) DETACH DELETE n")

            with open(backup_file, encoding="utf-8") as f:
                cypher_content = f.read()

            cypher_commands = cypher_content.split(";")

            for idx, command in enumerate(cypher_commands):
                clean_command = command.strip()
                if clean_command:
                    try:
                        logger.debug(
                            f"Executing command {idx + 1}: {clean_command[:80]}..."
                        )
                        await self.client.execute_query(clean_command)
                    except Exception as e:
                        logger.error(f"Failed to execute command {idx + 1}: {str(e)}")
                        raise
            logger.info(f"Graph successfully restored from backup: {backup_file}")

        except Exception as e:
            logger.error(f"Error restoring graph from backup: {str(e)}")
            raise

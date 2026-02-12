"""Main module to load ontology data files into the Neo4j database."""

import asyncio
import logging
import os

from tqdm import tqdm

# Suppress all logging before importing app modules
logging.disable(logging.CRITICAL)
import warnings

warnings.filterwarnings("ignore")

from app.db.knowledge_graph_builder import KnowledgeGraphBuilder
from app.db.neo4j_client import Neo4jClient


async def main():
    """Load ontology data files into the Neo4j database.

    Create database constraints and load ontology files if they exist.
    """
    files_to_load = [
        "ontology_with_ranges.json",
        "ontology.json",
    ]

    neo4j_client = Neo4jClient()
    graph_builder = KnowledgeGraphBuilder(neo4j_client)

    print("Creating constraints...")
    await graph_builder.create_constraints()

    total_nodes = 0
    total_relationships = 0

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "processed_data")

    # Process each file with progress bar
    for file_name in tqdm(files_to_load, desc="Loading files", unit="file"):
        file_path = os.path.join(data_dir, file_name)

        # Check if the file exists before attempting to load
        if not os.path.exists(file_path):
            print(f"File '{file_path}' not found. Skipping...")
            continue

        try:
            result = await graph_builder.load_ontology(file_path)

            if result.get("success"):
                nodes = result.get("nodes_created", 0)
                rels = result.get("relationships_created", 0)
                exec_time = result.get("execution_time", 0)

                total_nodes += nodes
                total_relationships += rels

                print(f"{file_name}")
                print(
                    f"   Nodes: {nodes:,} | Relationships: {rels:,} | Time: {exec_time:.2f}s"
                )
            else:
                error = result.get("error", "Unknown error")
                print(f"{file_name} - Error: {error}")

        except Exception as e:
            print(f"{file_name} - Exception: {e}")

    # Summary
    print("\n" + "=" * 60)
    print("Total Nodes Created:        " + f"{total_nodes:,}")
    print("Total Relationships Created: " + f"{total_relationships:,}")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

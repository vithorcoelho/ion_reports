"""Test configuration and fixtures for database tests."""

import json

import docker
import pytest
from docker.errors import DockerException
from pytest_mock import MockerFixture
from testcontainers.neo4j import Neo4jContainer

from app.core import config
from app.db.knowledge_graph_builder import KnowledgeGraphBuilder
from app.db.neo4j_client import Neo4jClient
from app.db.unified_query import Neo4jKnowledgeQuery


@pytest.fixture(scope="function")
def neo4j_container(monkeypatch):
    """Create a temporary Neo4j container to be used in tests.

    - Checks if Docker is available; if not, skips the test.
    - Starts a container with the 'neo4j:5.12' image.
    - Sets connection configurations  (URI, user, and password) using monkeypatch.
    - Ensures the container is terminated after the test.
    """
    try:
        docker.from_env().ping()
    except DockerException as e:
        pytest.skip(f"Docker is not available: {str(e)}")

    with Neo4jContainer("neo4j:5.12") as neo4j:
        bolt_url = neo4j.get_connection_url()

        monkeypatch.setattr(config.settings, "NEO4J_URI", bolt_url)
        monkeypatch.setattr(config.settings, "NEO4J_USER", "neo4j")
        monkeypatch.setattr(config.settings, "NEO4J_PASSWORD", "password")

        yield neo4j


@pytest.fixture
def mock_neo4j_client(mocker):
    """Create an asynchronous mock of the client to be used in tests."""
    client = mocker.AsyncMock(spec=Neo4jClient)
    client.execute_query = mocker.AsyncMock(return_value=None)
    return client


@pytest.fixture
def knowledge_graph_builder(mock_neo4j_client, mocker):
    """Return an instance of KnowledgeGraphBuilder using the mock client.

    Mocks create_backup and restore_graph_from_backup for isolated testing.
    """
    builder = KnowledgeGraphBuilder(neo4j_client=mock_neo4j_client)
    mocker.patch.object(
        builder,
        "create_backup",
        new_callable=mocker.AsyncMock,
        return_value="dummy_backup_path",
    )
    mocker.patch.object(
        builder,
        "restore_graph_from_backup",
        new_callable=mocker.AsyncMock,
        return_value=None,
    )
    mocker.patch("app.db.knowledge_graph_builder", return_value=None)
    return builder


def check_docker():
    """Check if Docker is available before running any tests."""
    try:
        docker.from_env().ping()
    except DockerException as e:
        pytest.skip(f"Docker is not available: {str(e)}")


@pytest.fixture
def neo4j_client(neo4j_container):
    """Use in tests that require a connection to the database."""
    return Neo4jClient()


@pytest.fixture
def sample_ontology_data():
    """Return a dictionary with simulated ontology data for testing.

    Includes examples of metabolites, metabolic pathways, and manifestations.
    """
    return {
        "metabolites": [
            {
                "id": "met-001",
                "name": "Glucose",
                "description": "Primary carbohydrate energy source",
                "metabolic_pathway": [{"id": "path-001"}],
            }
        ],
        "metabolic_pathways": [
            {
                "id": "path-001",
                "name": "Glycolysis",
                "description": "Breakdown of glucose to pyruvate",
            }
        ],
        "manifestations": [
            {
                "id": "manif-001",
                "name": "Hyperglycemia",
                "description": "High blood glucose levels",
                "metabolite": [{"id": "met-001"}],
            }
        ],
    }


@pytest.fixture
def ontology_file(tmp_path, sample_ontology_data):
    """Create a temporary file called "ontology.json" in the temporary directory provided by pytest."""
    file_path = tmp_path / "ontology.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(sample_ontology_data, f)
    return file_path


@pytest.fixture
def invalid_ontology_file(tmp_path):
    """Create a temporary file called "invalid_ontology.json" in the temporary directory provided by pytest."""
    file_path = tmp_path / "invalid_ontology.json"
    file_path.write_text("{invalid_json: true", encoding="utf-8")
    return file_path


@pytest.fixture
def query_unified(mock_neo4j_client):
    """Return an instance of KnowledgeGraphBuilder using the mock client."""
    return Neo4jKnowledgeQuery(neo4j_client=mock_neo4j_client)


@pytest.fixture
def mock_kg_response():
    """Mock knowledge graph response."""
    return [
        {
            "result": {
                "metabolite_info": [
                    {
                        "name": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                        "value": 0.07,
                        "unit": "mmol/L",
                        "status": "deficit_severo",
                        "definition": "O 1-estearoil-lisofosfatidilcolina (1-SLPC) é uma molécula...",
                        "reference_range_min": 0.8,
                        "reference_range_max": 1.2,
                        "category": "fosfolipídio",
                    }
                ],
                "manifestations": [
                    {
                        "metabolite": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                        "status": "baixo",
                        "description": "Comprometimento da função do HDL",
                        "type": "baixo",
                        "severity": "Moderada",
                        "affected_system": "Cardiovascular",
                    }
                ],
                "interventions": [
                    {
                        "type": "baixo",
                        "description": "Aumento do consumo de fontes de colina",
                        "priority": "high",
                        "metabolite": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                        "contraindicated": True,
                        "contraindication_reason": "Histórico de câncer de próstata avançado",
                        "medication_interaction": "Anticoagulantes",
                    }
                ],
                "foods": [
                    {
                        "name": "Gema de ovo",
                        "food_group": "Proteína Animal",
                        "main_nutrients": ["Colina", "Vitamina B12"],
                        "metabolite": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                    }
                ],
                "supplements": [
                    {
                        "name": "Ômega-3 (EPA/DHA)",
                        "active_composition": "Ácidos graxos poliinsaturados EPA e DHA",
                        "minimum_dosage": 1000,
                        "maximum_dosage": 3000,
                        "dosage_unit": "mg",
                        "metabolite": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                    }
                ],
                "pathways": [
                    {
                        "name": "Imunometabolismo - Ricas em Ômega 9 e Ômega 3",
                        "definition": "O imunometabolismo envolve...",
                        "metabolite": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                    }
                ],
                "evidence": [
                    {
                        "title": "The Fluid Aspect of the Mediterranean Diet...",
                        "authors": "Ditano-Vázquez, P., Torres-Peña, J. D.",
                        "year": "2019",
                        "metabolite": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
                    }
                ],
            }
        }
    ]


@pytest.fixture
def query_unified_with_test_db(neo4j_client):
    """Create and return an instance of Neo4jKnowledgeQuery using the provided Neo4j client."""
    return Neo4jKnowledgeQuery(neo4j_client=neo4j_client)


@pytest.fixture
def kg_connection(neo4j_client: Neo4jClient):
    """Return an instance of Neo4jKnowledgeQuery client."""
    return KnowledgeGraphBuilder(neo4j_client)


@pytest.fixture
def mock_validator(mocker: MockerFixture):
    """Mocka the ontology validator."""
    validator = mocker.Mock()
    mocker.patch(
        "app.db.knowledge_graph_builder.OntologyDataValidator", return_value=validator
    )
    return validator


@pytest.fixture
def mock_open_file(mocker: MockerFixture):
    """Mock the built-in open function for reading files."""
    return mocker.patch("builtins.open", mocker.mock_open(read_data="{}"))


@pytest.fixture
def mock_create_backup(mocker: MockerFixture, knowledge_graph_builder):
    """Mock the create_backup method of the knowledge graph builder."""
    return mocker.patch.object(
        knowledge_graph_builder, "create_backup", return_value="/backup/path.cypher"
    )


@pytest.fixture
def mock_restore_backup(mocker: MockerFixture, knowledge_graph_builder):
    """Mock the restore_graph_from_backup method of the knowledge graph builder."""
    return mocker.patch.object(knowledge_graph_builder, "restore_graph_from_backup")

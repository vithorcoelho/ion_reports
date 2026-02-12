"""Unit tests for KnowledgeGraphBuilder functionality."""

import json
import os

import pytest


@pytest.mark.asyncio
async def test_load_ontology_success(ontology_file, knowledge_graph_builder):
    """Test ontology loading."""
    result = await knowledge_graph_builder.load_ontology(str(ontology_file))

    assert result["success"] is True
    assert "error" not in result


@pytest.mark.asyncio
async def test_load_ontology_file_not_found(knowledge_graph_builder):
    """Test that load_ontology handles file not found errors gracefully."""
    result = await knowledge_graph_builder.load_ontology("non_existent_file.json")

    assert result["success"] is False
    assert "File not found" in result["error"]


@pytest.mark.asyncio
async def test_load_ontology_invalid_json(
    invalid_ontology_file, knowledge_graph_builder
):
    """Test that load_ontology handles invalid JSON gracefully."""
    result = await knowledge_graph_builder.load_ontology(str(invalid_ontology_file))

    assert result["success"] is False
    assert "error" in result


@pytest.mark.asyncio
async def test_node_creation(knowledge_graph_builder, mocker):
    """Test if nodes are created correctly."""
    json_content = json.dumps(
        {
            "metabolites": [
                {"id": "met1", "name": "Glucose"},
                {"id": "met2", "name": "Fructose"},
                {"id": "met3", "name": "Lactate"},
            ]
        }
    )

    mock_execute = mocker.patch.object(knowledge_graph_builder.client, "execute_query")
    mock_execute.return_value = [{"nodes_created": 3}]
    result = await knowledge_graph_builder.create_nodes(
        json_content, "metabolites", "METABOLITE"
    )
    assert result == 3
    mock_execute.assert_called_once()

    call_args = mock_execute.call_args
    query = call_args[0][0]
    assert "MERGE (n:METABOLITE {id: entity.id})" in query
    assert "data.metabolites AS entities" in query


@pytest.mark.asyncio
async def test_relationship_creation(knowledge_graph_builder, mocker):
    """Test if relationships are created correctly between nodes."""
    json_content = json.dumps(
        {
            "manifestations": [
                {"id": "man1", "metabolite": "met1"},
                {"id": "man2", "metabolite": ["met2", "met3"]},
            ]
        }
    )

    mock_execute = mocker.patch.object(knowledge_graph_builder.client, "execute_query")
    mock_execute.return_value = [{"relationships_created": 3}]

    result = await knowledge_graph_builder.create_relationships(
        json_content, "manifestations", "metabolites", "CAUSED_BY", "metabolite"
    )

    assert result == 3
    mock_execute.assert_called_once()
    call_args = mock_execute.call_args
    query = call_args[0][0]
    assert "MERGE (s)-[r:CAUSED_BY]->(t)" in query
    assert "MATCH (s:MANIFESTATION {id: source.id})" in query
    assert "MATCH (t:METABOLITE {id: target_id})" in query


@pytest.mark.asyncio
async def test_load_ontology_unexpected_file_read_error(
    knowledge_graph_builder, mocker
):
    """Test that load_ontology handles unexpected file read errors."""
    mocker.patch("builtins.open", side_effect=OSError("Unexpected error"))
    result = await knowledge_graph_builder.load_ontology("any_file.json")

    assert result["success"] is False
    assert "Unexpected error" in result["error"]


@pytest.mark.asyncio
async def test_neo4j_query_failure(
    ontology_file, mock_neo4j_client, knowledge_graph_builder
):
    """Tests the behavior of the `load_ontology` method of `knowledge_graph_builder` when a failure occurs during the execution of a query in Neo4j."""
    mock_neo4j_client.execute_query.side_effect = Exception("Neo4j connection error")

    result = await knowledge_graph_builder.load_ontology(str(ontology_file))

    assert result["success"] is False
    assert "Neo4j connection error" in result["error"]


@pytest.mark.asyncio
async def test_create_relationships_with_error(mocker, knowledge_graph_builder):
    """Test that relationship creation propagates exceptions from execute_query."""
    knowledge_graph_builder._type_mapping = {
        "some_source": "SomeSourceLabel",
        "some_target": "SomeTargetLabel",
    }

    knowledge_graph_builder._relationship_mappings = {
        ("some_source", "some_target"): {"type": "RELATED_TO", "key": "some_key"}
    }

    mocker.patch.object(
        knowledge_graph_builder.client,
        "execute_query",
        side_effect=Exception("Simulated error"),
    )

    with pytest.raises(Exception, match="Simulated error"):
        await knowledge_graph_builder.create_relationships(
            json_content="{}",
            source_entity="some_source",
            target_entity="some_target",
            relationship_type="RELATED_TO",
            relationship_key="some_key",
        )


@pytest.mark.asyncio
async def test_create_constraints_with_error(mocker, knowledge_graph_builder):
    """Test that create_constraints method raises exceptions when database errors occur.

    When an error occurs while creating constraints in the database (simulated by
    raising an exception when calling `execute_query`), the appropriate exception
    is raised with the expected message.
    """
    knowledge_graph_builder._type_mapping = {"some_node": "SomeNodeLabel"}

    mocker.patch.object(
        knowledge_graph_builder.client,
        "execute_query",
        side_effect=Exception("Constraint error"),
    )
    with pytest.raises(Exception, match="Constraint error"):
        await knowledge_graph_builder.create_constraints()


@pytest.mark.asyncio
async def test_restore_graph_restores_expected_data(
    neo4j_client, tmp_path, kg_connection
):
    """Tests if the Cypher backup restores the expected data in the Neo4j graph."""
    backup_file = tmp_path / "restore_test.cypher"

    # conteúdo que representa um grafo mínimo
    cypher_data = """
    CREATE (p:Person {id: 1, name: "Alice"});
    CREATE (p:Person {id: 2, name: "Bob"});
    """
    backup_file.write_text(cypher_data, encoding="utf-8")

    await kg_connection.restore_graph_from_backup(str(backup_file))

    query = """
    MATCH (p:Person)
    RETURN p.id AS id, p.name AS name
    ORDER BY id
    """
    # Agora, consultar o grafo para verificar se os nós foram realmente restaurados
    result = await neo4j_client.execute_query(query)

    assert result == [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


@pytest.mark.asyncio
async def test_load_ontology_validation_fails(
    knowledge_graph_builder, mock_validator, mock_open_file
):
    """Test that load_ontology correctly handles cases where ontology validation fails.

    This test mocks the `validate` method of the `mock_validator` to return a failure
    result (`False` and an error message). It then calls `load_ontology` and asserts
    that the returned result indicates `success` as `False` and that the error message
    contains "Validation failed". This ensures the system properly reports validation issues.
    """
    mock_validator.validate.return_value = (False, "Validation error")

    result = await knowledge_graph_builder.load_ontology("test.json")

    assert result["success"] is False
    assert "Validation failed" in result["error"]


@pytest.mark.asyncio
async def test_load_ontology_backup_fails(
    knowledge_graph_builder, mock_validator, mock_open_file, mocker
):
    """Test that load_ontology handles errors gracefully when backup creation fails.

    This test mocks the `validate` method to succeed, but then patches the
    `create_backup` method of `knowledge_graph_builder` to raise an `Exception`.
    It asserts that when `load_ontology` is called, it returns a result indicating
    `success` as `False` and that the error message contains "Erro ao criar backup",
    confirming that backup failures are caught and reported.
    """
    mock_validator.validate.return_value = (True, [])
    mocker.patch.object(
        knowledge_graph_builder, "create_backup", side_effect=Exception("Backup error")
    )

    result = await knowledge_graph_builder.load_ontology("test.json")

    assert result["success"] is False
    assert "Erro ao criar backup" in result["error"]


@pytest.mark.asyncio
async def test_load_ontology_rollback_on_error(
    knowledge_graph_builder,
    mock_validator,
    mock_create_backup,
    mock_restore_backup,
    mock_open_file,
    mocker,
):
    """Test that load_ontology performs a rollback (restores from backup) if an error occurs during node creation.

    This test simulates a scenario where ontology validation and backup creation succeed,
    but an error occurs during the `create_nodes` phase. It patches `create_nodes` to
    raise an `Exception`. The test then asserts that `load_ontology` returns `success` as `False`
    and, crucially, that `mock_restore_backup` was called exactly once with the expected
    backup path, confirming the rollback mechanism is triggered.
    """
    mock_validator.validate.return_value = (True, [])
    mocker.patch.object(
        knowledge_graph_builder, "create_nodes", side_effect=Exception("Node error")
    )

    result = await knowledge_graph_builder.load_ontology("test.json")

    assert result["success"] is False
    mock_restore_backup.assert_called_once_with("/backup/path.cypher")


@pytest.mark.asyncio
async def test_create_nodes_empty_entities(knowledge_graph_builder, mock_neo4j_client):
    """Test that create_nodes returns 0 when provided with an empty list of entities.

    This test provides `create_nodes` with JSON content containing an empty list for
    the "metabolites" key. It mocks `execute_query` to return a result indicating
    zero nodes created. The test asserts that the `create_nodes` method correctly
    returns 0, confirming its behavior when no entities are present to be created.
    """
    json_content = json.dumps({"metabolites": []})
    mock_neo4j_client.return_value = [{"nodes_created": 0}]

    result = await knowledge_graph_builder.create_nodes(
        json_content, "metabolites", "METABOLITE"
    )

    assert result == 0


@pytest.mark.asyncio
async def test_create_nodes_no_result(knowledge_graph_builder, mock_neo4j_client):
    """Test that create_nodes returns 0 when the underlying query execution returns no result.

    This test simulates a scenario where `execute_query` returns an empty list,
    implying that no nodes were reported as created by the database operation.
    It asserts that `create_nodes` correctly returns 0, ensuring it handles
    cases where the query result is empty.
    """
    json_content = json.dumps({"metabolites": []})
    mock_neo4j_client.return_value = []

    result = await knowledge_graph_builder.create_nodes(
        json_content, "metabolites", "METABOLITE"
    )

    assert result == 0


@pytest.mark.asyncio
async def test_create_relationships_invalid_labels(knowledge_graph_builder):
    """Test that create_relationships returns 0 when invalid source or target labels are provided.

    This test calls `create_relationships` with non-existent source and target labels
    ("invalid_source", "invalid_target"). It asserts that the method returns 0,
    indicating that no relationships were created, as it should not proceed with
    relationship creation if the specified entity types are not found or valid.
    """
    json_content = json.dumps({})

    result = await knowledge_graph_builder.create_relationships(
        json_content, "invalid_source", "invalid_target", "RELATES", "key"
    )

    assert result == 0


@pytest.mark.asyncio
async def test_create_relationships_empty_result(
    knowledge_graph_builder, mock_neo4j_client
):
    """Test that create_relationships returns 0 when the underlying query execution returns no result.

    This test simulates a scenario where `execute_query` returns an empty list,
    implying that no relationships were reported as created by the database operation.
    It asserts that `create_relationships` correctly returns 0, ensuring it handles
    cases where the query result is empty.
    """
    json_content = json.dumps({"manifestations": []})
    mock_neo4j_client.return_value = []

    result = await knowledge_graph_builder.create_relationships(
        json_content, "manifestations", "metabolites", "CAUSED_BY", "metabolite"
    )

    assert result == 0


@pytest.mark.asyncio
async def test_create_backup_success(mocker, tmp_path):
    """Test that create_backup creates a .cypher file and that this file can be read.

    This simulates a valid export. It does not verify internal calls to os.makedirs
    or timestamp format directly.
    """
    # Patch os.getcwd para redirecionar o diretório
    mocker.patch("os.getcwd", return_value=str(tmp_path))

    # Mocks para o session e run
    mock_session = mocker.AsyncMock()
    mock_result = mocker.AsyncMock()
    mock_result.single.return_value = {"nodes": 1}
    mock_session.run.return_value = mock_result

    # Create a KnowledgeGraphBuilder with a properly mocked client
    mock_neo4j_client = mocker.MagicMock()
    mock_neo4j_client.session.return_value.__aenter__.return_value = mock_session
    mock_neo4j_client.session.return_value.__aexit__.return_value = None

    from app.db.knowledge_graph_builder import KnowledgeGraphBuilder

    kg_builder = KnowledgeGraphBuilder(mock_neo4j_client)

    backup_path = await kg_builder.create_backup()

    assert backup_path.endswith(".cypher")
    assert os.path.dirname(backup_path) == os.path.join(
        str(tmp_path), "backups", "neo4j_backups"
    )

    mock_session.run.assert_awaited_once()
    called_query = mock_session.run.call_args[0][0]
    called_params = mock_session.run.call_args[1]["parameters"]
    assert "CALL apoc.export.cypher.all" in called_query
    assert called_params["file"].endswith(".cypher")

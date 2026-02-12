"""Unit tests for Neo4j database client."""

import pytest
from neo4j.exceptions import AuthError, Neo4jError, ServiceUnavailable

from app.core.config import settings
from app.db.neo4j_client import Neo4jClient


@pytest.mark.asyncio
async def test_neo4j_connection_valid(neo4j_client):
    """Verify if the connection to the database is valid."""
    await neo4j_client.verify_connection()


@pytest.mark.asyncio
async def test_neo4j_execute_simple_query(neo4j_client):
    """Verify if a simple query can be executed and returns the expected value."""
    result = await neo4j_client.execute_query("RETURN 42 AS answer")
    assert result[0]["answer"] == 42


@pytest.mark.asyncio
async def test_neo4j_close(neo4j_client):
    """Verify if the Neo4j client closes the connection without raising exceptions."""
    await neo4j_client.close()


@pytest.mark.asyncio
async def test_neo4j_verify_connection_error(neo4j_client, mocker):
    """Verify that a ServiceUnavailable exception is raised when the connection fails."""
    mocker.patch.object(
        neo4j_client.driver, "session", side_effect=ServiceUnavailable("test error")
    )
    with pytest.raises(ServiceUnavailable):
        await neo4j_client.verify_connection()


@pytest.mark.asyncio
async def test_execute_query_error(neo4j_client, mocker):
    """Verify that execute_query returns None when a Neo4jError is raised during query execution."""
    mock_session = mocker.AsyncMock()
    mock_session.run.side_effect = Neo4jError("test error")

    mock_context_manager = mocker.AsyncMock()
    mock_context_manager.__aenter__.return_value = mock_session
    mock_context_manager.__aexit__.return_value = None

    mocker.patch.object(
        neo4j_client.driver, "session", return_value=mock_context_manager
    )
    with pytest.raises(Neo4jError):
        await neo4j_client.execute_query("RETURN 1")


@pytest.mark.asyncio
async def test_neo4j_enter(neo4j_client):
    """Verify that the __enter__ method returns an instance of the Neo4j client."""
    client = await neo4j_client.__enter__()
    assert isinstance(client, type(neo4j_client))


@pytest.mark.asyncio
async def test_neo4j_exit(neo4j_client, mocker):
    """Verify that the __exit__ method properly closes the Neo4j driver."""
    mocker.patch.object(neo4j_client.driver, "close", new=mocker.AsyncMock())

    await neo4j_client.__exit__(None, None, None)
    neo4j_client.driver.close.assert_awaited_once()


def test_neo4j_client_missing_credentials(monkeypatch):
    """Verify that Neo4jClient raises a ValueError when required credentials are missing."""
    monkeypatch.setattr(settings, "NEO4J_URI", None)
    monkeypatch.setattr(settings, "NEO4J_USER", "user")
    monkeypatch.setattr(settings, "NEO4J_PASSWORD", "pass")

    with pytest.raises(ValueError, match="Neo4j credentials are not fully set."):
        Neo4jClient()


def test_neo4j_client_auth_error(monkeypatch, mocker):
    """Verify that Neo4jClient raises an AuthError when authentication fails."""
    monkeypatch.setattr(settings, "NEO4J_URI", "bolt://localhost:7687")
    monkeypatch.setattr(settings, "NEO4J_USER", "wrong_user")
    monkeypatch.setattr(settings, "NEO4J_PASSWORD", "wrong_pass")

    mocker.patch(
        "app.db.neo4j_client.AsyncGraphDatabase.driver",
        side_effect=AuthError("Auth failed"),
    )
    with pytest.raises(AuthError):
        Neo4jClient()


def test_neo4j_client_generic_error(monkeypatch, mocker):
    """Verify that Neo4jClient raises a generic Exception when an unexpected error occurs during driver initialization."""
    monkeypatch.setattr(settings, "NEO4J_URI", "bolt://localhost:7687")
    monkeypatch.setattr(settings, "NEO4J_USER", "user")
    monkeypatch.setattr(settings, "NEO4J_PASSWORD", "pass")

    mocker.patch(
        "app.db.neo4j_client.AsyncGraphDatabase.driver",
        side_effect=Exception("Generic error"),
    )
    with pytest.raises(Exception, match="Generic error"):
        Neo4jClient()

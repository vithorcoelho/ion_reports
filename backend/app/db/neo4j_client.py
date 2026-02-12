"""Asynchronous Neo4j database client.

This module provides the Neo4jClient class for managing asynchronous connections
to Neo4j databases, including authentication, connection management, and query
execution with proper error handling and resource cleanup.
"""

from typing import Any

from neo4j import AsyncGraphDatabase, AsyncSession, basic_auth
from neo4j.exceptions import AuthError, Neo4jError, ServiceUnavailable

from app.core.config import settings
from app.core.logging import logger
from app.db.base import IDatabaseClient


class Neo4jClient(IDatabaseClient):
    """Asynchronous client for connecting to and executing queries on a Neo4j database.

    This class manages the lifecycle of the Neo4j driver, including authentication,
    connection verification, and asynchronous execution of Cypher queries.
    """

    def __init__(self):
        """Initializes the asynchronous Neo4j driver with credentials and settings defined in the environment.

        Raises:
            ValueError: If any of the required environment variables (URI, user, or password) are missing.
            AuthError: If authentication fails.
            Exception: For any other driver initialization errors.

        """
        if not all([settings.NEO4J_URI, settings.NEO4J_USER, settings.NEO4J_PASSWORD]):
            raise ValueError("Neo4j credentials are not fully set.")

        try:
            self.driver = AsyncGraphDatabase.driver(
                settings.NEO4J_URI,
                auth=basic_auth(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
                max_connection_lifetime=1000,
                max_connection_pool_size=10,
                connection_timeout=30,
            )
            logger.info("Neo4j driver initialized.")
        except AuthError as e:
            logger.critical("Neo4j authentication failed: check credentials.")
            raise e
        except Exception as e:
            logger.critical(f"Failed to initialize Neo4j driver: {e}")
            raise e

    async def __enter__(self):
        """Returns: Neo4jClient: The instance of the client itself."""
        return self

    async def __exit__(self, exc_type, exc_value, traceback):
        """Exits the asynchronous context of the client, closing the driver."""
        await self.close()

    async def close(self):
        """Closes the Neo4j driver connection asynchronously."""
        await self.driver.close()
        logger.debug("Closing Neo4j driver.")

    async def verify_connection(self):
        """Verifies connectivity with the database."""
        try:
            async with self.driver.session() as session:
                await session.run("RETURN 1")
            logger.info("Successfully connected to Neo4j.")
        except (AuthError, ServiceUnavailable, Neo4jError, Exception) as e:
            logger.error(f"Neo4j connection verification failed: {e}")
            raise

    async def execute_query(self, query: str, **params) -> list[dict[str, Any]] | None:
        """Executes a Cypher query asynchronously on the database.

        Args:
            query: The Cypher query to execute
            **params: Query parameters

        Returns:
            Optional[List[Dict[str, Any]]]: The query results or None if there was an error

        """
        try:
            async with self.driver.session() as session:
                result = await session.run(query, **params)
                records = await result.data()
                await result.consume()  # Ensure all results are consumed
                logger.debug(
                    f"Query executed successfully: {query[:100]}... | Params: {params}"
                )
                return records
        except (Neo4jError, Exception) as e:
            logger.error(f"Failed to execute query: {query[:100]}... | Error: {e}")
            raise  # Re-raise the exception to be handled by the caller

    def session(self) -> AsyncSession:
        """Create a new async session from the Neo4j driver."""
        return self.driver.session()

# Ion Nutri FastAPI Application
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.config import configure_mlflow, settings
from app.core.logging import logger
from app.core.version import get_build_info, get_version
from app.db.neo4j_client import Neo4jClient


# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager: initializes Neo4j and MLflow, handles shutdown."""
    ...
    # Startup: Initialize Neo4j connection
    app.state.neo4j_client = Neo4jClient()
    configure_mlflow()

    yield  # Yield control back to FastAPI

    # Shutdown: Close Neo4j connection
    if hasattr(app.state, "neo4j_client"):
        await app.state.neo4j_client.close()


# Create FastAPI app
app = FastAPI(
    title="Ion Nutri API",
    description="API for Ion Nutri - Nutrição Metabólica",
    version=get_version(),
    lifespan=lifespan,
)


# Handles request validation exceptions and returns a JSON response
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle request validation errors and return JSON response."""
    logger.warning(f"Erro de validação: {exc}")
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder(
            {
                "detail": exc.errors(),
                "body": exc.body,
            }
        ),
    )


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api")


# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


# Version endpoint
@app.get("/version", tags=["info"])
async def get_version_info():
    """Get application version and build information."""
    return get_build_info()


if __name__ == "__main__":
    """
    Run the application directly when this file is executed
    """
    uvicorn.run(
        "app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG
    )

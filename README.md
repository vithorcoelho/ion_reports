# Ion Nutri - Automated Nutrimetabolomic Reports

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.0+-red.svg)](https://neo4j.com/)
[![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)](https://www.docker.com/)

This project automates the generation of nutrimetabolomic reports for Ion Nutri, significantly reducing processing time while maintaining analysis quality.

## 🚀 How to run the project

- **📦 [DEPLOYMENT.md](DEPLOYMENT.md)** - Complete application setup
- **📖 [USAGE.md](USAGE.md)** - How to use and generate reports

## 🔬 About Ion Nutri

Ion Nutri specializes in metabolic analyses performed from saliva samples, offering the Nutrimetabolomic Test (TNM) that enables precise and personalized evaluation of metabolic imbalances. This system automates the manual report generation process using advanced AI and knowledge graph technologies.

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (handled by setup script)
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ion-nutri
   ```

2. **Run the setup script:**
   ```bash
   ./setup.sh
   ```

   This will:
   - Install Python environment with uv
   - Start Neo4j database
   - Build and start the FastAPI application
   - Create necessary directories and configuration files

3. **Access the services:**
   - **API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **Version Info**: http://localhost:8000/version
   - **Neo4j Browser**: http://localhost:7474
   - **Neo4j Credentials**: neo4j/password

## 🛠️ Development

### Setup Options

The setup script provides several options for different development scenarios:

```bash
# Complete development environment
./setup.sh

# Python environment only
./setup.sh --python-only

# Docker services only
./setup.sh --docker-only

# Build services without starting them
./setup.sh --build-only

# Skip build step (use existing images)
./setup.sh --skip-build

# Use staging environment
./setup.sh --env staging

# Build specific services
./setup.sh api neo4j
```

### Environment Variables

Key environment variables (automatically configured by setup):

```bash
# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password

# Application Settings
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# LLM Settings
OPENROUTER_API_KEY=your_key_here
OPENROUTER_API_BASE=https://openrouter.ai/api/v1
OPENROUTER_MODEL=google/gemini-2.5-flash
OPENROUTER_MAX_TOKENS=4096
OPENROUTER_TEMPERATURE=0.1
OPENROUTER_MODEL_NAME=gemini-2.5-flash
```

### Project Structure

```
ion-nutri/
├── backend/               # Backend application
│   ├── app/              # FastAPI application
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Core configuration
│   ├── db/                # Database clients and utilities
│   ├── schemas/           # Pydantic models
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── docs/                  # Documentation
├── ml/                    # Machine learning demos and scripts
├── tests/                 # Test suite
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   │   └── services/     # Business logic services
│   ├── tests/            # Backend tests
│   │   ├── unit/         # Unit tests
│   │   ├── integration/  # Integration tests
│   │   ├── e2e/          # End-to-end tests
│   │   └── performance/  # Performance tests
│   ├── Dockerfile        # Backend container image
│   ├── pyproject.toml    # Python project configuration
│   └── uv.lock          # Python dependency lock file
├── frontend/             # Frontend application
│   ├── src/             # React source code
│   ├── Dockerfile       # Frontend container image
│   └── package.json     # Node.js dependencies
├── k8s/                 # Kubernetes manifests
├── docker-compose.yml   # Docker Compose configuration
└── setup.sh            # Development environment setup
```

### Testing

Run the test suite:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run all tests
pytest

# Run specific test categories
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/

# Run with coverage
pytest --cov=app tests/
```

### API Endpoints

The FastAPI application provides the following endpoints:

- `GET /health` - Health check
- `GET /version` - Version information
- `POST /reports/tnm` - Generate TNM report
- `GET /docs` - Interactive API documentation
- `GET /redoc` - Alternative API documentation

## 🏗️ Architecture

The system is built with:

- **FastAPI**: High-performance web framework for the API
- **Neo4j**: Graph database for knowledge representation
- **LLM Integration**: AI-powered report generation
- **Docker**: Containerized deployment
- **Pytest**: Comprehensive testing framework

Key architectural components:

1. **Knowledge Graph**: Neo4j database storing metabolic pathways and relationships
2. **LLM Service**: AI-powered analysis and report generation
3. **TNM Service**: Core business logic for nutrimetabolomic analysis
4. **API Layer**: RESTful endpoints for external integration

## 📚 Documentation

Comprehensive documentation is available in the `docs/` directory:

- [Current Process Overview](docs/processo-atual.md)
- [Automated Process Design](docs/processo-automatizado.md)
- [System Architecture](docs/arquitetura.md)
- [Development Guide](docs/development.md)
- [Ontologies](docs/ontologias.md)
- [Timeline and Metrics](docs/cronograma-metricas.md)
- [Limitations and Considerations](docs/limites-consideracoes.md)
- [TNM Report Template](docs/templates/tnm.md)
- [Testing Strategy](docs/tests.md)

## 🐳 Docker Commands

Common Docker operations:

```bash
# View service logs
docker compose logs -f

# Stop all services
docker compose down

# Restart services
docker compose restart

# Access Neo4j shell
docker compose exec neo4j cypher-shell -u neo4j -p password

# View service status
docker compose ps
```

## 🧪 Machine Learning Demos

The `ml/demos/` directory contains various demonstrations:

- **Graph RAG**: Knowledge graph retrieval augmentation
- **MLflow GenAI**: Experiment tracking for AI models
- **Structured Outputs**: Structured report generation examples

## 📊 Performance

The system is designed for high performance:

- FastAPI with async/await support
- Neo4j graph database for efficient relationship queries
- Docker containerization for scalable deployment
- Comprehensive caching strategies

## 🔒 Security

Security considerations:

- Environment variable management
- API authentication (when configured)
- Database access controls
- Container security best practices

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests
- Update documentation for new features
- Use type hints throughout the codebase
- **Pre-commit hooks**: The project uses comprehensive pre-commit hooks for code quality enforcement including:
  - **Code formatting**: Ruff (ultra-fast linting, formatting, and import sorting)
  - **Security scanning**: Bandit, detect-secrets, and pip-audit
  - **Type checking**: MyPy static analysis
  - **Documentation**: PyDocStyle for docstring standards
  - **Commit standards**: Commitizen for conventional commits

For detailed information about the development tools and pre-commit configuration, see the [Development Guide](docs/development.md#ferramentas-de-desenvolvimento).

## 📝 License

This project is proprietary software developed for Ion Nutri.

## 🆘 Support

For support and questions:

1. Check the [documentation](docs/)
2. Review existing [issues](https://github.com/your-org/ion-nutri/issues)
3. Create a new issue if needed

---

**Ion Nutri** - Transforming metabolic analysis through automation and AI.

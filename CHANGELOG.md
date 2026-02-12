# Changelog

All notable changes to the Ion Nutri project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-20

### Added

#### Frontend Application
- **React TypeScript Frontend**: Complete web interface for IonNutri Reports (#94)
  - Modern React 18 with TypeScript for type safety
  - Form handling with react-hook-form and Zod validation
  - Markdown rendering for report display with react-markdown
  - Tailwind CSS for responsive styling
  - Vite for fast development and optimized builds
  - Docker support with Nginx for production deployment
  - Health check endpoint for container monitoring

#### CI/CD & Automation
- **Claude Code GitHub Workflow**: Integration for automated code reviews and assistance (#95)
- **Windows Setup Script**: PowerShell-based setup for Windows development environments (#93)
  - Auto-detection for docker compose command (docker-compose vs docker compose) (#92)

#### Data & Knowledge Base
- **TNM Metabolite Data**: Process and inject new TNM metabolite data into the database (#87)
  - Expanded metabolite coverage
  - Enhanced pathway relationships
  - Improved data consistency

#### Documentation
- **Release Process Guide**: Complete RELEASE.md documentation with step-by-step instructions
  - Version numbering guidelines
  - CHANGELOG format specifications
  - Deployment automation details
  - Hotfix procedures

### Changed

#### Report Generation
- **Refined TNM Prompts**: Improved prompt engineering for report generation (#91)
  - Better context handling
  - More accurate recommendations
  - Enhanced readability

#### Architecture
- **ReportCoordinator Enhancement**: Updated with comprehensive strategy pattern support (#84)
  - Better separation of concerns
  - Improved extensibility
  - Enhanced maintainability

#### Development Experience
- Setup script improvements with better error handling
- Docker compose command auto-detection for cross-platform compatibility

### Fixed

- **MLflow Host Validation**: Resolved host header validation issue preventing API startup (#89)
  - Added proper CORS configuration
  - Fixed forwarded headers handling
- **Setup Scripts**: Auto-detection for docker compose command across different Docker versions (#92)

### Removed

- Unnecessary files and folders cleanup for better repository hygiene (#90)

### Technical Details

**New Technologies:**
- **Frontend Stack**: React 18.3+, TypeScript 5.6+, Vite 5.4+
- **Styling**: Tailwind CSS 3.4+
- **Validation**: Zod 3.23+
- **HTTP Client**: Axios 1.7+

**Infrastructure:**
- Frontend container runs on Nginx Alpine
- Health checks for all services
- Docker multi-stage builds for optimized images

### Migration Notes

This release adds a complete frontend interface to the previously backend-only system. The frontend is available at `http://localhost:3001` when running locally with Docker Compose.

**Breaking Changes:** None - all backend APIs remain backwards compatible.

**Deployment Notes:**
- Backend deployment to staging is automated via GitHub Actions on merge to main
- Frontend deployment to staging requires DevOps configuration (not yet automated)
- See RELEASE.md for complete deployment procedures

## [1.0.0] - 2025-09-30

### Added

#### Core Features
- **Report Generation System**: Complete TNM (Teste Nutrimetabólico) report generation pipeline
  - Personalized nutrition reports based on metabolite analysis
  - Integration with patient anamnesis data
  - Automated recommendations based on knowledge graph queries

#### MLflow Integration
- **Trace API**: Integration with MLflow Trace API SDK for LLM call tracking
- **Prompt Registry**: System for managing and versioning prompts
- **Prompt Evaluation**: Framework for evaluating prompt performance with custom metrics
- **Demo Projects**:
  - Prompt evaluation with custom metrics demo
  - Prompt optimization with MLflow demo
  - Tracking and versioning demo

#### Architecture & Services
- **Strategy Pattern Implementation**: Multistage and onestage report generation strategies
- **LLM Service**: Interface-based service for large language model interactions
- **Knowledge Graph Service**: Neo4j-based knowledge graph query service with interfaces
- **N-Layer Architecture**: Clean architecture implementation with Strategy Pattern

#### Documentation
- **Deployment Guide** (`DEPLOYMENT.md`): Complete deployment instructions
- **Usage Guide** (`USAGE.md`): API usage documentation with visual examples
- **Git Workflow** (`docs/GITFLOW.md`): Gitflow branching model documentation
- **Architecture Documentation**: N-Layer Architecture with Strategy Pattern documentation
- **API Screenshots**: Visual guides for API usage (5 step-by-step images)
- **MLflow Screenshots**: Visual guides for MLflow tracking (3 screenshots)

#### Development Tools
- Pre-commit hooks configuration
- Comprehensive test suite (105+ unit tests)
- Test coverage reporting
- Docker support with docker-compose setup

### Fixed
- Test suite updates to match current implementation
- Data loading adjustments for metabolite processing
- Data duplication and consistency checks in knowledge graph

### Changed
- Enhanced environment configuration (`.env.example` with 60+ configuration options)
- Improved graph data processing scripts with better documentation
- Setup script improvements for development environment

### Technical Details
- **Python**: 3.12+
- **Framework**: FastAPI with async/await support
- **Database**: Neo4j for knowledge graph
- **ML Platform**: MLflow for experiment tracking and prompt management
- **Dependencies**: OpenAI, boto3, pandas, Jinja2, and more

### Migration Notes
This is the first stable release (v1.0.0) of the Ion Nutri system. The system is production-ready with:
- Complete report generation pipeline
- MLflow integration for LLM tracking and evaluation
- Comprehensive documentation
- Robust test coverage
- Clean architecture with SOLID principles

[1.0.0]: https://github.com/edgebr/ion-nutri/releases/tag/v1.0.0

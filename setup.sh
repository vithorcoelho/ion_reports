#!/bin/bash

# Ion-Nutri Development Environment Setup Script
#
# This script sets up the development environment for the Ion-Nutri project,
# including creating a Python environment (uv) and starting the required Docker
# containers (Neo4j and API).
#
# Usage:
#   ./setup.sh                    # Full setup
#   ./setup.sh --python-only      # Python environment only
#   ./setup.sh --docker-only      # Docker environment only
#   ./setup.sh --build-only       # Build Docker services only
#   ./setup.sh --skip-build       # Skip build step
#   ./setup.sh --env staging      # Use staging environment
#   ./setup.sh --help             # Show help

set -euo pipefail

#=============================================================================
# CONFIGURATION
#=============================================================================

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_ROOT="${SCRIPT_DIR}"

# Docker Compose command (will be set during validation)
DOCKER_COMPOSE_CMD=""

# Service configuration
readonly NEO4J_USER="neo4j"
readonly NEO4J_PASSWORD="password"
readonly NEO4J_URI="bolt://localhost:7687"
readonly API_PORT="8000"
readonly NEO4J_BROWSER_PORT="7474"
readonly NEO4J_BOLT_PORT="7687"

# Timeouts
readonly NEO4J_TIMEOUT=60
readonly API_TIMEOUT=30

# Build configuration
ENVIRONMENT="development"
BUILD_ONLY=false
SKIP_BUILD=false
SERVICES=""

#=============================================================================
# COLORS AND OUTPUT
#=============================================================================

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly PURPLE='\033[0;35m'
readonly NC='\033[0m'

print_status() { echo -e "${BLUE}[INFO]${NC} $*"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $*"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $*"; }
print_error() { echo -e "${RED}[ERROR]${NC} $*" >&2; }
print_section() { echo -e "\n${PURPLE}====== $* ======${NC}"; }
print_step() { echo -e "${BLUE}[STEP]${NC} $*"; }

#=============================================================================
# UTILITY FUNCTIONS
#=============================================================================

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

is_docker_running() {
    docker info &>/dev/null
}

has_docker_compose() {
    command_exists docker-compose || docker compose version &>/dev/null
}

get_docker_compose_cmd() {
    if command_exists docker-compose; then
        echo "docker-compose"
    elif docker compose version &>/dev/null 2>&1; then
        echo "docker compose"
    else
        print_error "Neither docker-compose nor docker compose found"
        exit 1
    fi
}

file_exists() {
    [[ -f "$1" ]]
}

directory_exists() {
    [[ -d "$1" ]]
}

wait_for_port() {
    local port="$1"
    local timeout="${2:-30}"
    local count=0

    while [[ $count -lt $timeout ]]; do
        if nc -z localhost "$port" 2>/dev/null; then
            return 0
        fi
        ((count++))
        sleep 1
    done
    return 1
}

cleanup_on_error() {
    print_error "Setup failed. Cleaning up..."
    if [[ -n "$DOCKER_COMPOSE_CMD" ]]; then
        $DOCKER_COMPOSE_CMD down 2>/dev/null || true
    fi
}

#=============================================================================
# VERSION INFORMATION
#=============================================================================

capture_version_info() {
    print_step "Capturing version information..."

    # Check if we're in a git repository
    if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
        print_warning "Not in a git repository. Git information will be limited."
        export GIT_COMMIT="unknown"
        export GIT_BRANCH="unknown"
    else
        # Get git information
        export GIT_COMMIT=$(git rev-parse --short HEAD)
        export GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

        # Check if there are uncommitted changes
        if ! git diff-index --quiet HEAD --; then
            print_warning "There are uncommitted changes."
            export GIT_COMMIT="${GIT_COMMIT}-dirty"
        fi
    fi

    # Get build time
    export BUILD_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Set build number
    export BUILD_NUMBER="local-$(date +%Y%m%d%H%M%S)"

    print_status "Version: $(cat backend/pyproject.toml | grep '^version' | cut -d'"' -f2 || echo 'unknown')"
    print_status "Git Commit: $GIT_COMMIT"
    print_status "Git Branch: $GIT_BRANCH"
    print_status "Build Time: $BUILD_TIME"
    print_status "Build Number: $BUILD_NUMBER"
    print_status "Environment: $ENVIRONMENT"
}

#=============================================================================
# DOCKER COMPOSE CONFIGURATION
#=============================================================================

get_compose_files() {
    local compose_files="-f docker-compose.yml"

    case $ENVIRONMENT in
        development)
            compose_files="$compose_files -f docker-compose.override.yml"
            ;;
        staging)
            compose_files="$compose_files -f docker-compose.prod.yml"
            ;;
        production)
            compose_files="$compose_files -f docker-compose.prod.yml"
            ;;
        *)
            print_error "Unknown environment: $ENVIRONMENT"
            exit 1
            ;;
    esac

    echo "$compose_files"
}

#=============================================================================
# VALIDATION FUNCTIONS
#=============================================================================

validate_requirements() {
    local setup_type="${1:-full}"

    print_section "VALIDATING REQUIREMENTS"

    local missing_requirements=()

    # Check for Docker (always required)
    if ! command_exists docker; then
        missing_requirements+=("Docker (https://docs.docker.com/get-docker/)")
    fi

    if ! has_docker_compose; then
        missing_requirements+=("Docker Compose")
    fi

    # For MinIO-only setup, only Docker is required
    if [[ "$setup_type" == "minio-only" ]]; then
        if [[ ${#missing_requirements[@]} -gt 0 ]]; then
            print_error "Missing requirements for MinIO setup:"
            printf '  • %s\n' "${missing_requirements[@]}"
            return 1
        fi
        print_success "MinIO requirements validated"
        return 0
    fi

    # For full setup, check all required files
    if ! file_exists "backend/pyproject.toml"; then
        missing_requirements+=("backend/pyproject.toml file")
    fi

    if ! file_exists "docker-compose.yml"; then
        missing_requirements+=("docker-compose.yml file")
    fi

    if ! file_exists "backend/Dockerfile"; then
        missing_requirements+=("backend/Dockerfile")
    fi

    if [[ ${#missing_requirements[@]} -gt 0 ]]; then
        print_error "Missing requirements:"
        printf '  • %s\n' "${missing_requirements[@]}"
        return 1
    fi

    print_success "All requirements validated"
}

#=============================================================================
# UV AND PYTHON ENVIRONMENT
#=============================================================================

install_uv() {
    if command_exists uv; then
        print_status "uv is already installed"
        return 0
    fi

    print_status "Installing uv..."
    if ! curl -LsSf https://astral.sh/uv/install.sh | sh; then
        print_error "Failed to install uv"
        return 1
    fi

    export PATH="$HOME/.cargo/bin:$PATH"
    print_success "uv installed successfully"
}

setup_virtual_environment() {
    print_status "Setting up Python virtual environment..."

    # Change to backend directory
    cd "$PROJECT_ROOT/backend" || return 1

    # Clean up invalid venv
    if directory_exists ".venv" && ! file_exists ".venv/pyvenv.cfg"; then
        print_status "Removing invalid .venv directory..."
        rm -rf .venv
    fi

    # Ensure uv is in PATH
    export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"

    # Create virtual environment
    if ! uv venv; then
        print_error "Failed to create virtual environment"
        print_error "Please restart your shell and run the script again, or run:"
        print_error "  source ~/.bashrc  # or ~/.zshrc"
        print_error "  ./setup.sh"
        cd "$PROJECT_ROOT" || return 1
        return 1
    fi

    # Determine activation script path
    local activate_path
    if [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* || "$OSTYPE" == "win32" ]]; then
        activate_path=".venv/Scripts/activate"
    else
        activate_path=".venv/bin/activate"
    fi

    # Activate virtual environment
    if ! file_exists "$activate_path"; then
        print_error "Virtual environment activation script not found: $activate_path"
        cd "$PROJECT_ROOT" || return 1
        return 1
    fi

    # shellcheck source=/dev/null
    source "$activate_path"
    print_success "Virtual environment activated"

    # Return to project root
    cd "$PROJECT_ROOT" || return 1
}

install_python_dependencies() {
    print_status "Installing Python dependencies..."

    # Change to backend directory
    cd "$PROJECT_ROOT/backend" || return 1

    # Install main dependencies
    if ! uv pip install -e . --link-mode=copy; then
        print_error "Failed to install main dependencies"
        cd "$PROJECT_ROOT" || return 1
        return 1
    fi

    # Install development dependencies
    if ! uv pip install -e .[dev] --link-mode=copy; then
        print_error "Failed to install development dependencies"
        cd "$PROJECT_ROOT" || return 1
        return 1
    fi

    print_success "Python dependencies installed"

    # Return to project root
    cd "$PROJECT_ROOT" || return 1
}

setup_python_environment() {
    print_section "SETTING UP PYTHON ENVIRONMENT"

    mkdir -p ml/scripts

    install_uv || return 1
    setup_virtual_environment || return 1
    install_python_dependencies || return 1

    print_success "Python environment configured successfully"
}

#=============================================================================
# DOCKER ENVIRONMENT
#=============================================================================

validate_docker() {
    print_status "Validating Docker environment..."

    if ! is_docker_running; then
        print_error "Docker daemon is not running"
        print_status "Please start Docker Desktop or the Docker service"
        return 1
    fi

    # Set the Docker Compose command
    DOCKER_COMPOSE_CMD=$(get_docker_compose_cmd)
    print_status "Using Docker Compose command: $DOCKER_COMPOSE_CMD"

    print_success "Docker environment validated"
}

setup_minio() {
    print_status "Setting up MinIO for MLflow artifacts..."

    # Check if MLflow is enabled
    if [[ -f .env ]] && grep -q "MLFLOW_ENABLED=false" .env; then
        print_status "MLflow is disabled (MLFLOW_ENABLED=false), skipping MinIO setup"
        return 0
    fi

    # Configuration
    local MINIO_ENDPOINT="http://localhost:9000"
    local MINIO_CONSOLE="http://localhost:9001"
    local MINIO_ACCESS_KEY="minioadmin"
    local MINIO_SECRET_KEY="minioadmin123"
    local BUCKET_NAME="mlflow-artifacts"

    # Check if MinIO is running
    print_status "Checking if MinIO is running..."
    if ! curl -s "${MINIO_ENDPOINT}/minio/health/live" &>/dev/null; then
        print_warning "MinIO is not running or not accessible at ${MINIO_ENDPOINT}"
        print_status "Note: MinIO initialization happens automatically via docker-compose"
        return 0
    fi

    print_success "MinIO is running"

    # Note: Bucket creation is now handled by minio-init service in docker-compose
    print_status "Note: MinIO bucket '${BUCKET_NAME}' is created automatically by docker-compose"
    print_success "MinIO initialization completed!"
    print_status "MinIO Console: ${MINIO_CONSOLE}"
    print_status "MinIO API: ${MINIO_ENDPOINT}"
    print_status "Access Key: ${MINIO_ACCESS_KEY}"
    print_status "Secret Key: ${MINIO_SECRET_KEY}"
}

create_env_file() {
    print_status "Configuring .env file..."

    local env_content
    read -r -d '' env_content << 'EOF' || true
# Docker Settings - Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password

# Application Settings
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# LLM Settings (adjust as needed)
OPENAI_API_KEY=
EOF

    if file_exists ".env"; then
        if ! grep -q "NEO4J_URI" .env; then
            print_status "Adding Docker configurations to existing .env..."
            printf '\n%s\n' "$env_content" >> .env
            print_success "Docker configurations added to .env"
        else
            print_status ".env file already contains required configurations"
        fi
    else
        if file_exists ".env.example"; then
            cp .env.example .env
            print_success ".env file created from .env.example"
        else
            printf '%s\n' "$env_content" > .env
            print_success ".env file created with default configuration"
        fi
    fi
}

create_directories() {
    print_status "Creating necessary directories..."

    local directories=("logs" "data/neo4j-import")

    for dir in "${directories[@]}"; do
        mkdir -p "$dir"
    done

    print_success "Directories created successfully"
}

build_services() {
    local compose_files=$(get_compose_files)

    print_step "Building services with Docker Compose..."

    if [[ -n "$SERVICES" ]]; then
        print_status "Building services: $SERVICES"
        $DOCKER_COMPOSE_CMD $compose_files build $SERVICES
    else
        print_status "Building all services"
        $DOCKER_COMPOSE_CMD $compose_files build
    fi

    print_success "Services built successfully"
}

start_services() {
    local compose_files=$(get_compose_files)

    print_step "Starting services with Docker Compose..."

    if [[ -n "$SERVICES" ]]; then
        print_status "Starting services: $SERVICES"
        $DOCKER_COMPOSE_CMD $compose_files up -d $SERVICES
    else
        print_status "Starting all services"
        $DOCKER_COMPOSE_CMD $compose_files up -d
    fi

    print_success "Services started successfully"
}

build_and_start_services() {
    print_status "Building and starting Docker services..."

    # Stop existing services
    local compose_files=$(get_compose_files)
    $DOCKER_COMPOSE_CMD $compose_files down 2>/dev/null || true

    # Build only mode
    if [[ "$BUILD_ONLY" == "true" ]]; then
        print_step "Building services with Docker Compose..."
        if [[ -n "$SERVICES" ]]; then
            print_status "Building services: $SERVICES"
            $DOCKER_COMPOSE_CMD $compose_files build $SERVICES
        else
            print_status "Building all services"
            $DOCKER_COMPOSE_CMD $compose_files build
        fi
        print_success "Services built successfully"
        return 0
    fi

    # Build and start services together (unless skip-build is set)
    print_step "Building and starting services with Docker Compose..."
    if [[ "$SKIP_BUILD" == "true" ]]; then
        print_status "Starting all services (skipping build)"
        if [[ -n "$SERVICES" ]]; then
            print_status "Starting services: $SERVICES"
            $DOCKER_COMPOSE_CMD $compose_files up -d $SERVICES
        else
            print_status "Starting all services"
            $DOCKER_COMPOSE_CMD $compose_files up -d
        fi
    else
        if [[ -n "$SERVICES" ]]; then
            print_status "Building and starting services: $SERVICES"
            $DOCKER_COMPOSE_CMD $compose_files up --build -d $SERVICES
        else
            print_status "Building and starting all services"
            $DOCKER_COMPOSE_CMD $compose_files up --build -d
        fi
    fi

    print_success "Services built and started successfully"
}

wait_for_neo4j() {
    print_status "Waiting for Neo4j to be ready..."

    local compose_files=$(get_compose_files)
    local count=0
    while [[ $count -lt $NEO4J_TIMEOUT ]]; do
        if $DOCKER_COMPOSE_CMD $compose_files exec -T neo4j cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" "RETURN 1" &>/dev/null; then
            print_success "Neo4j is ready"
            return 0
        fi

        if (( count % 10 == 0 && count > 0 )); then
            print_status "Still waiting for Neo4j... (${count}/${NEO4J_TIMEOUT}s)"
        fi

        ((count++))
        sleep 1
    done

    print_error "Timeout waiting for Neo4j"
    print_warning "Check the logs: $DOCKER_COMPOSE_CMD logs neo4j"
    return 1
}

test_apoc_extension() {
    print_status "Testing APOC extension..."

    local compose_files=$(get_compose_files)
    local result
    result=$($DOCKER_COMPOSE_CMD $compose_files exec -T neo4j cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" \
        "CALL apoc.help('apoc') YIELD name RETURN count(name) > 0 as apoc_available" \
        --format plain 2>/dev/null | tail -n 1)

    if [[ "${result,,}" == *"true"* ]]; then
        print_success "APOC extension is working correctly"
    else
        print_error "APOC extension is not working properly"
        return 1
    fi
}

wait_for_api() {
    print_status "Checking API availability..."

    sleep 5  # Give API time to start

    local count=0
    while [[ $count -lt $API_TIMEOUT ]]; do
        if curl -f "http://127.0.0.1:${API_PORT}/health" &>/dev/null; then
            print_success "API is ready and responding"
            return 0
        fi
        ((count++))
        sleep 1
    done

    print_warning "API may not be fully ready yet (this is normal if /health endpoint doesn't exist)"
}

setup_docker_environment() {
    print_section "SETTING UP DOCKER ENVIRONMENT"

    validate_docker || return 1
    create_env_file || return 1
    create_directories || return 1
    capture_version_info || return 1
    build_and_start_services || return 1

    # Only wait for services if they were started
    if [[ "$BUILD_ONLY" != "true" ]]; then
        wait_for_neo4j || return 1
        test_apoc_extension || return 1
        setup_minio || return 1
        wait_for_api
    fi

    print_success "Docker environment configured successfully"
}

#=============================================================================
# INFORMATION DISPLAY
#=============================================================================

show_final_info() {
    print_section "SETUP COMPLETE"

    # Check if MLflow is enabled
    local MLFLOW_ENABLED=true
    if [[ -f .env ]] && grep -q "MLFLOW_ENABLED=false" .env; then
        MLFLOW_ENABLED=false
    fi

    cat << EOF

Development environment successfully configured!

Python Environment:
  - Virtual environment: backend/.venv/
  - Activation (Unix): source backend/.venv/bin/activate
  - Activation (Windows): backend\.venv\\Scripts\\activate

Docker Services:
  - Frontend: http://localhost:3001
  - FastAPI API: http://localhost:${API_PORT}
  - API Documentation: http://localhost:${API_PORT}/docs
  - Version Information: http://localhost:${API_PORT}/version
  - Neo4j Browser: http://localhost:${NEO4J_BROWSER_PORT}
  - Neo4j Bolt: ${NEO4J_URI}
EOF

    if [[ "$MLFLOW_ENABLED" == "true" ]]; then
        cat << EOF
  - PostgreSQL: localhost:5432
  - MinIO Console: http://localhost:9001
  - MinIO API: http://localhost:9000
  - MLflow: http://localhost:5000
EOF
    fi

    cat << EOF

Data Loading:
  - Database population is now AUTOMATIC when containers start
  - The 'load-data' service runs after Neo4j is healthy
  - API waits for data loading to complete before starting
  - View data loading logs: $DOCKER_COMPOSE_CMD logs load-data

Data Loading:
  - Database population is now AUTOMATIC when containers start
  - The 'load-data' service runs after Neo4j is healthy
  - API waits for data loading to complete before starting
  - View data loading logs: $DOCKER_COMPOSE_CMD logs load-data

Service Credentials:
  - Neo4j User: ${NEO4J_USER}
  - Neo4j Password: ${NEO4J_PASSWORD}
EOF

    if [[ "$MLFLOW_ENABLED" == "true" ]]; then
        cat << EOF
  - PostgreSQL User: mlflow
  - PostgreSQL Password: mlflow_password
  - PostgreSQL Database: mlflow
  - MinIO Access Key: minioadmin
  - MinIO Secret Key: minioadmin123
EOF
    fi

    cat << EOF

Build Information:
  - Environment: ${ENVIRONMENT}
  - Git Commit: ${GIT_COMMIT:-unknown}
  - Git Branch: ${GIT_BRANCH:-unknown}
  - Build Time: ${BUILD_TIME:-unknown}
  - MLflow Enabled: ${MLFLOW_ENABLED}

Useful Commands:
  - View logs: $DOCKER_COMPOSE_CMD logs -f
  - Stop services: $DOCKER_COMPOSE_CMD down
  - Restart services: $DOCKER_COMPOSE_CMD restart
  - Neo4j shell: $DOCKER_COMPOSE_CMD exec neo4j cypher-shell -u ${NEO4J_USER} -p ${NEO4J_PASSWORD}

Current Service Status:
EOF

    local compose_files=$(get_compose_files)
    $DOCKER_COMPOSE_CMD $compose_files ps 2>/dev/null || echo "  (Run '$DOCKER_COMPOSE_CMD ps' to see detailed status)"

    echo ""
    echo "You can now start developing!"
}

#=============================================================================
# HELP AND MAIN FUNCTIONS
#=============================================================================

show_help() {
    cat << 'EOF'
Ion-Nutri Development Environment Setup Script

USAGE:
    ./setup.sh [OPTIONS] [SERVICES...]

OPTIONS:
    --python-only         Set up only the Python environment
    --docker-only         Set up only the Docker environment
    --minio-only          Set up only MinIO (only needed if MLFLOW_ENABLED=true)
    --build-only          Build Docker services only (don't start them)
    --skip-build          Skip Docker build step
    --env ENVIRONMENT     Environment (development, staging, production)
    --help                Show this help message

DESCRIPTION:
    This script sets up the complete development environment for Ion-Nutri,
    including Python virtual environment with uv and Docker services
    (Neo4j database and FastAPI). MLflow infrastructure (PostgreSQL, MinIO,
    MLflow server) is optional and controlled by MLFLOW_ENABLED in .env.

    IMPORTANT: Database population (load-data service) is now AUTOMATIC!
    The database will be populated when the containers start without manual intervention.

    IMPORTANT: Database population (load-data service) is now AUTOMATIC!
    The database will be populated when the containers start without manual intervention.

REQUIREMENTS:
    - Docker and Docker Compose installed and running
    - uv for Python environment management (will be installed if not present)
    - Required project files: backend/pyproject.toml, docker-compose.yml, backend/Dockerfile
    - Data files: processed_data/ontology_with_ranges.json and processed_data/ontology.json

EXAMPLES:
    ./setup.sh                          # Complete setup (includes automatic database population)
    ./setup.sh --python-only            # Python environment only
    ./setup.sh --docker-only            # Docker services only (with automatic database population)
    ./setup.sh --minio-only             # MinIO setup only
    ./setup.sh --build-only             # Build services only
    ./setup.sh --env staging            # Setup with staging environment
    ./setup.sh --skip-build             # Skip build, just start services
    ./setup.sh api                      # Setup with only api service
    ./setup.sh --help                   # Show this help

NOTES:
    - Database population runs automatically via the 'load-data' service
    - API startup waits for data loading to complete
    - View data loading logs: docker-compose logs load-data

EOF
}

main() {
    # Set up error handling
    trap cleanup_on_error ERR

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --help|-h)
                show_help
                exit 0
                ;;
            --python-only)
                print_status "Setting up Python environment only..."
                validate_requirements "full" || exit 1
                setup_python_environment || exit 1
                print_success "Python environment setup completed"
                exit 0
                ;;
            --docker-only)
                print_status "Setting up Docker environment only..."
                validate_requirements "full" || exit 1
                setup_docker_environment || exit 1
                show_final_info
                exit 0
                ;;
            --minio-only)
                print_status "Setting up MinIO only..."
                validate_requirements "minio-only" || exit 1
                if [[ -f .env ]] && grep -q "MLFLOW_ENABLED=false" .env; then
                    print_warning "MLflow is disabled (MLFLOW_ENABLED=false)"
                    print_status "MinIO setup is not needed when MLflow is disabled"
                    exit 0
                fi
                setup_minio || exit 1
                print_success "MinIO setup completed"
                exit 0
                ;;
            --build-only)
                BUILD_ONLY=true
                shift
                ;;
            --skip-build)
                SKIP_BUILD=true
                shift
                ;;
            --env)
                ENVIRONMENT="$2"
                shift 2
                ;;
            -*)
                print_error "Unknown option: $1"
                echo "Use --help for usage information"
                exit 1
                ;;
            *)
                SERVICES="$SERVICES $1"
                shift
                ;;
        esac
    done

    # Complete setup
    print_status "Setting up complete development environment..."
    print_status "Environment: $ENVIRONMENT"

    validate_requirements "full" || exit 1
    setup_python_environment || exit 1
    setup_docker_environment || exit 1

    # Only show final info if services were started
    if [[ "$BUILD_ONLY" != "true" ]]; then
        show_final_info
    else
        print_success "Build completed successfully!"
    fi
}

#=============================================================================
# SCRIPT EXECUTION
#=============================================================================

# Only run main if script is executed directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

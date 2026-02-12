<#
.SYNOPSIS
    Ion-Nutri Development Environment Setup Script for Windows Server 2019

.DESCRIPTION
    This script sets up the development environment for the Ion-Nutri project,
    including creating a Python environment (uv) and starting the required Docker
    containers (Neo4j and API).

.PARAMETER PythonOnly
    Set up only the Python environment

.PARAMETER DockerOnly
    Set up only the Docker environment

.PARAMETER MinioOnly
    Set up only MinIO (create buckets for MLflow)

.PARAMETER BuildOnly
    Build Docker services only (don't start them)

.PARAMETER SkipBuild
    Skip Docker build step

.PARAMETER Environment
    Environment (development, staging, production). Default: development

.PARAMETER Services
    Specific services to build/start

.PARAMETER Help
    Show help message

.EXAMPLE
    .\setup.ps1
    Complete setup

.EXAMPLE
    .\setup.ps1 -PythonOnly
    Python environment only

.EXAMPLE
    .\setup.ps1 -DockerOnly
    Docker services only

.EXAMPLE
    .\setup.ps1 -Environment staging
    Setup with staging environment

.EXAMPLE
    .\setup.ps1 -Services api,neo4j
    Setup with specific services only
#>

[CmdletBinding()]
param(
    [switch]$PythonOnly,
    [switch]$DockerOnly,
    [switch]$MinioOnly,
    [switch]$BuildOnly,
    [switch]$SkipBuild,
    [ValidateSet('development', 'staging', 'production')]
    [string]$Environment = 'development',
    [string[]]$Services = @(),
    [switch]$Help
)

# Requires PowerShell 5.1 or later (Windows Server 2019 comes with 5.1)
#Requires -Version 5.1

# CONFIGURATION

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$script:SCRIPT_DIR = $PSScriptRoot
$script:PROJECT_ROOT = $SCRIPT_DIR

# Service configuration
$script:NEO4J_USER = "neo4j"
$script:NEO4J_PASSWORD = "password"
$script:NEO4J_URI = "bolt://localhost:7687"
$script:API_PORT = "8000"
$script:NEO4J_BROWSER_PORT = "7474"
$script:NEO4J_BOLT_PORT = "7687"

# Timeouts
$script:NEO4J_TIMEOUT = 60
$script:API_TIMEOUT = 30

# Docker Compose command (will be set during validation)
$script:DOCKER_COMPOSE_CMD = ""

# Build configuration
$script:BUILD_ONLY = $BuildOnly
$script:SKIP_BUILD = $SkipBuild
$script:SERVICES = $Services -join " "

# Version information
$script:GIT_COMMIT = ""
$script:GIT_BRANCH = ""
$script:BUILD_TIME = ""
$script:BUILD_NUMBER = ""


function Write-Status {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[SUCCESS] $Message" -ForegroundColor Green
}

function Write-Warning2 {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor Yellow
}

function Write-Error2 {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Write-Section {
    param([string]$Message)
    Write-Host ""
    Write-Host "====== $Message ======" -ForegroundColor Magenta
}

function Write-Step {
    param([string]$Message)
    Write-Host "[STEP] $Message" -ForegroundColor Cyan
}

# UTILITY FUNCTIONS

function Test-CommandExists {
    param([string]$Command)
    $null -ne (Get-Command $Command -ErrorAction SilentlyContinue)
}

function Test-DockerRunning {
    try {
        docker info 2>&1 | Out-Null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Test-DockerCompose {
    if (Test-CommandExists "docker-compose") {
        return $true
    }
    try {
        docker compose version 2>&1 | Out-Null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Get-DockerComposeCommand {
    if (Test-CommandExists "docker-compose") {
        return "docker-compose"
    }
    try {
        docker compose version 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            return "docker", "compose"
        }
    } catch {}

    Write-Error2 "Neither docker-compose nor docker compose found"
    exit 1
}

function Test-PortOpen {
    param(
        [int]$Port,
        [int]$Timeout = 30
    )

    $count = 0
    while ($count -lt $Timeout) {
        try {
            $tcpClient = New-Object System.Net.Sockets.TcpClient
            $tcpClient.Connect("localhost", $Port)
            $tcpClient.Close()
            return $true
        } catch {
            $count++
            Start-Sleep -Seconds 1
        }
    }
    return $false
}

function Invoke-Cleanup {
    Write-Error2 "Setup failed. Cleaning up..."
    if ($script:DOCKER_COMPOSE_CMD) {
        try {
            if ($script:DOCKER_COMPOSE_CMD -is [array]) {
                & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] down 2>&1 | Out-Null
            } else {
                & $script:DOCKER_COMPOSE_CMD down 2>&1 | Out-Null
            }
        } catch {}
    }
}

# VERSION INFORMATION

function Get-VersionInfo {
    Write-Step "Capturing version information..."

    # Check if we're in a git repository
    try {
        git rev-parse --is-inside-work-tree 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw
        }

        # Get git information
        $script:GIT_COMMIT = (git rev-parse --short HEAD).Trim()
        $script:GIT_BRANCH = (git rev-parse --abbrev-ref HEAD).Trim()

        # Check if there are uncommitted changes
        git diff-index --quiet HEAD -- 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Warning2 "There are uncommitted changes."
            $script:GIT_COMMIT = "$($script:GIT_COMMIT)-dirty"
        }
    } catch {
        Write-Warning2 "Not in a git repository. Git information will be limited."
        $script:GIT_COMMIT = "unknown"
        $script:GIT_BRANCH = "unknown"
    }

    # Get build time
    $script:BUILD_TIME = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

    # Set build number
    $script:BUILD_NUMBER = "local-$(Get-Date -Format 'yyyyMMddHHmmss')"

    # Get version from backend/pyproject.toml
    $version = "unknown"
    if (Test-Path "backend/pyproject.toml") {
        $content = Get-Content "backend/pyproject.toml" -Raw
        if ($content -match 'version\s*=\s*"([^"]+)"') {
            $version = $Matches[1]
        }
    }

    Write-Status "Version: $version"
    Write-Status "Git Commit: $($script:GIT_COMMIT)"
    Write-Status "Git Branch: $($script:GIT_BRANCH)"
    Write-Status "Build Time: $($script:BUILD_TIME)"
    Write-Status "Build Number: $($script:BUILD_NUMBER)"
    Write-Status "Environment: $Environment"

    # Set environment variables for Docker
    $env:GIT_COMMIT = $script:GIT_COMMIT
    $env:GIT_BRANCH = $script:GIT_BRANCH
    $env:BUILD_TIME = $script:BUILD_TIME
    $env:BUILD_NUMBER = $script:BUILD_NUMBER
}

# DOCKER COMPOSE CONFIGURATION

function Get-ComposeFiles {
    $composeFiles = @("-f", "docker-compose.yml")

    switch ($Environment) {
        "development" {
            $composeFiles += @("-f", "docker-compose.override.yml")
        }
        "staging" {
            $composeFiles += @("-f", "docker-compose.prod.yml")
        }
        "production" {
            $composeFiles += @("-f", "docker-compose.prod.yml")
        }
        default {
            Write-Error2 "Unknown environment: $Environment"
            exit 1
        }
    }

    return $composeFiles
}

# VALIDATION FUNCTIONS

function Test-Requirements {
    param([string]$SetupType = "full")

    Write-Section "VALIDATING REQUIREMENTS"

    $missingRequirements = @()

    # Check for Docker (always required)
    if (-not (Test-CommandExists "docker")) {
        $missingRequirements += "Docker (https://docs.docker.com/get-docker/)"
    }

    if (-not (Test-DockerCompose)) {
        $missingRequirements += "Docker Compose"
    }

    # For MinIO-only setup, only Docker is required
    if ($SetupType -eq "minio-only") {
        if ($missingRequirements.Count -gt 0) {
            Write-Error2 "Missing requirements for MinIO setup:"
            foreach ($req in $missingRequirements) {
                Write-Host "  • $req"
            }
            return $false
        }
        Write-Success "MinIO requirements validated"
        return $true
    }

    # For full setup, check all required files
    if (-not (Test-Path "backend/pyproject.toml")) {
        $missingRequirements += "backend/pyproject.toml file"
    }

    if (-not (Test-Path "docker-compose.yml")) {
        $missingRequirements += "docker-compose.yml file"
    }

    if (-not (Test-Path "backend/Dockerfile")) {
        $missingRequirements += "backend/Dockerfile"
    }

    if ($missingRequirements.Count -gt 0) {
        Write-Error2 "Missing requirements:"
        foreach ($req in $missingRequirements) {
            Write-Host "  • $req"
        }
        return $false
    }

    Write-Success "All requirements validated"
    return $true
}

# UV AND PYTHON ENVIRONMENT

function Install-Uv {
    if (Test-CommandExists "uv") {
        Write-Status "uv is already installed"
        $uvCmd = Get-Command uv
        Write-Status "Location: $($uvCmd.Source)"
        return $true
    }

    Write-Status "Installing uv..."
    try {
        # Install uv using the official installer for Windows
        Write-Status "Downloading and running uv installer..."
        $installScript = Invoke-WebRequest -Uri "https://astral.sh/uv/install.ps1" -UseBasicParsing
        Invoke-Expression $installScript.Content

        # Add to PATH for current session
        $uvPaths = @(
            "$env:USERPROFILE\.cargo\bin",
            "$env:USERPROFILE\.local\bin"
        )

        foreach ($path in $uvPaths) {
            if (Test-Path $path) {
                Write-Status "Adding to PATH: $path"
                $env:PATH = "$path;$env:PATH"
            }
        }

        # Verify installation
        Start-Sleep -Seconds 2
        if (Test-CommandExists "uv") {
            $uvCmd = Get-Command uv
            Write-Success "uv installed successfully"
            Write-Status "Location: $($uvCmd.Source)"
            Write-Status "Version: $(uv --version)"
            return $true
        } else {
            throw "uv command not found after installation"
        }
    } catch {
        Write-Error2 "Failed to install uv: $_"
        Write-Error2 ""
        Write-Error2 "Please try manual installation:"
        Write-Error2 "  1. Open PowerShell as Administrator"
        Write-Error2 "  2. Run: irm https://astral.sh/uv/install.ps1 | iex"
        Write-Error2 "  3. Close and reopen PowerShell"
        Write-Error2 "  4. Verify with: uv --version"
        Write-Error2 "  5. Then run this script again"
        return $false
    }
}

function Initialize-VirtualEnvironment {
    Write-Status "Setting up Python virtual environment..."

    # Change to backend directory
    $backendPath = Join-Path $ProjectRoot "backend"
    if (-not (Test-Path $backendPath)) {
        Write-Error2 "Backend directory not found: $backendPath"
        return $false
    }

    $originalLocation = Get-Location
    Set-Location $backendPath

    # Clean up invalid venv
    if ((Test-Path ".venv") -and -not (Test-Path ".venv\pyvenv.cfg")) {
        Write-Status "Removing invalid .venv directory..."
        Remove-Item -Path ".venv" -Recurse -Force
    }

    # Ensure uv is in PATH
    $uvPath = "$env:USERPROFILE\.cargo\bin"
    if (Test-Path $uvPath) {
        $env:PATH = "$uvPath;$env:PATH"
    }

    # Also check in local bin
    $uvLocalPath = "$env:USERPROFILE\.local\bin"
    if (Test-Path $uvLocalPath) {
        $env:PATH = "$uvLocalPath;$env:PATH"
    }

    # Verify uv is available
    $uvCommand = Get-Command uv -ErrorAction SilentlyContinue
    if (-not $uvCommand) {
        Write-Error2 "uv command not found in PATH"
        Write-Error2 "PATH: $env:PATH"
        Write-Error2 "Please close and reopen PowerShell, then run the script again"
        return $false
    }

    Write-Status "Using uv from: $($uvCommand.Source)"

    # Check Python version before creating venv
    Write-Status "Checking Python availability..."
    $pythonCmd = $null
    $pythonVersion = $null

    # Try to find Python
    $pythonCommands = @("python", "python3", "python3.13", "python3.12")
    foreach ($cmd in $pythonCommands) {
        try {
            $testCmd = Get-Command $cmd -ErrorAction SilentlyContinue
            if ($testCmd) {
                # Test that Python actually works
                $oldErrorAction = $ErrorActionPreference
                $ErrorActionPreference = 'Continue'
                $versionOutput = & $cmd --version 2>&1
                $ErrorActionPreference = $oldErrorAction

                if ($LASTEXITCODE -eq 0) {
                    # Verify Python version meets requirements (>=3.12)
                    if ($versionOutput -match 'Python (\d+)\.(\d+)') {
                        $major = [int]$Matches[1]
                        $minor = [int]$Matches[2]
                        if ($major -gt 3 -or ($major -eq 3 -and $minor -ge 12)) {
                            $pythonCmd = $cmd
                            $pythonVersion = $versionOutput
                            Write-Status "Found Python: $pythonVersion (using: $cmd)"
                            break
                        } else {
                            Write-Warning2 "Python $versionOutput found but version is too old (requires >=3.12)"
                        }
                    } else {
                        # If we can't parse version, still use it but warn
                        $pythonCmd = $cmd
                        $pythonVersion = $versionOutput
                        Write-Status "Found Python: $pythonVersion (using: $cmd)"
                        Write-Warning2 "Could not verify Python version meets requirements"
                        break
                    }
                }
            }
        } catch {
            # Continue to next command
        }
    }

    if (-not $pythonCmd) {
        Write-Warning2 "Python command not found. uv will try to auto-detect Python."
    }

    # Create virtual environment with better error handling
    Write-Status "Creating virtual environment with: uv venv"

    # Try with explicit Python if we found one
    $venvSuccess = $false
    $venvError = $null

    if ($pythonCmd) {
        Write-Status "Attempting to use Python: $pythonCmd"
        try {
            # Temporarily change error action to continue, then restore
            $oldErrorAction = $ErrorActionPreference
            $ErrorActionPreference = 'Continue'

            # Capture output but suppress PowerShell errors from stderr (uv writes info to stderr)
            $uvOutput = & uv venv --python $pythonCmd 2>&1 | ForEach-Object {
                if ($_ -is [System.Management.Automation.ErrorRecord]) {
                    # Convert error records to strings (these are often just informational)
                    $_.ToString()
                } else {
                    $_
                }
            } | Out-String
            $uvExitCode = $LASTEXITCODE

            $ErrorActionPreference = $oldErrorAction

            if ($uvExitCode -eq 0) {
                $venvSuccess = $true
                # Only show output if it contains actual errors (not just informational messages)
                if ($uvOutput -and $uvOutput.Trim() -and $uvOutput -notmatch '^Using CPython') {
                    Write-Status "uv venv output:"
                    $uvOutput -split "`n" | ForEach-Object {
                        if ($_.Trim()) {
                            Write-Host "  $_" -ForegroundColor Gray
                        }
                    }
                }
            } else {
                $venvError = "Exit code: $uvExitCode`nOutput: $uvOutput"
            }
        } catch {
            $ErrorActionPreference = $oldErrorAction
            $venvError = "Exception: $_`nException Type: $($_.Exception.GetType().FullName)`nStack: $($_.ScriptStackTrace)"
        }
    }

    # If explicit Python failed or wasn't found, try without specifying
    if (-not $venvSuccess) {
        Write-Status "Trying uv venv without explicit Python specification..."
        try {
            # Temporarily change error action to continue, then restore
            $oldErrorAction = $ErrorActionPreference
            $ErrorActionPreference = 'Continue'

            # Capture output but suppress PowerShell errors from stderr (uv writes info to stderr)
            $uvOutput = & uv venv 2>&1 | ForEach-Object {
                if ($_ -is [System.Management.Automation.ErrorRecord]) {
                    # Convert error records to strings (these are often just informational)
                    $_.ToString()
                } else {
                    $_
                }
            } | Out-String
            $uvExitCode = $LASTEXITCODE

            $ErrorActionPreference = $oldErrorAction

            if ($uvExitCode -eq 0) {
                $venvSuccess = $true
                # Only show output if it contains actual errors (not just informational messages)
                if ($uvOutput -and $uvOutput.Trim() -and $uvOutput -notmatch '^Using CPython') {
                    Write-Status "uv venv output:"
                    $uvOutput -split "`n" | ForEach-Object {
                        if ($_.Trim()) {
                            Write-Host "  $_" -ForegroundColor Gray
                        }
                    }
                }
            } else {
                if ($venvError) {
                    $venvError += "`n`nFallback attempt - Exit code: $uvExitCode`nOutput: $uvOutput"
                } else {
                    $venvError = "Exit code: $uvExitCode`nOutput: $uvOutput"
                }
            }
        } catch {
            $ErrorActionPreference = $oldErrorAction
            if ($venvError) {
                $venvError += "`n`nFallback attempt - Exception: $_`nException Type: $($_.Exception.GetType().FullName)`nStack: $($_.ScriptStackTrace)"
            } else {
                $venvError = "Exception: $_`nException Type: $($_.Exception.GetType().FullName)`nStack: $($_.ScriptStackTrace)"
            }
        }
    }

    if (-not $venvSuccess) {
        Write-Error2 "Failed to create virtual environment"
        Write-Error2 "Error details:"
        $venvError -split "`n" | ForEach-Object {
            if ($_.Trim()) {
                Write-Host "  $_" -ForegroundColor Red
            }
        }
        Write-Error2 ""
        Write-Error2 "Troubleshooting steps:"
        Write-Error2 "  1. Verify Python is installed: python --version"
        Write-Error2 "  2. Check if Python 3.12+ is available (project requires >=3.12)"
        Write-Error2 "  3. Try manually: uv venv"
        Write-Error2 "  4. If using Anaconda, ensure it's properly configured"
        Write-Error2 "  5. Try specifying Python explicitly: uv venv --python python3.12"
        Write-Error2 "  6. Check if the Python path has spaces (may cause issues)"
        Set-Location $originalLocation
        return $false
    }

    Write-Success "Virtual environment created successfully"

    # Activate virtual environment
    $activatePath = ".venv\Scripts\Activate.ps1"
    if (-not (Test-Path $activatePath)) {
        Write-Error2 "Virtual environment activation script not found: $activatePath"
        Write-Error2 "Expected path: $(Resolve-Path $activatePath -ErrorAction SilentlyContinue)"
        Set-Location $originalLocation
        return $false
    }

    Write-Status "Activating virtual environment..."
    try {
        & $activatePath
        Write-Success "Virtual environment activated"
        Set-Location $originalLocation
        return $true
    } catch {
        Write-Error2 "Failed to activate virtual environment: $_"
        Set-Location $originalLocation
        return $false
    }
}

function Install-PythonDependencies {
    Write-Status "Installing Python dependencies..."

    # Change to backend directory
    $backendPath = Join-Path $ProjectRoot "backend"
    if (-not (Test-Path $backendPath)) {
        Write-Error2 "Backend directory not found: $backendPath"
        return $false
    }

    $originalLocation = Get-Location
    Set-Location $backendPath

    # Initialize error action variable
    $oldErrorAction = $ErrorActionPreference

    try {
        # Temporarily change error action to continue (uv writes progress to stderr)
        $ErrorActionPreference = 'Continue'

        # Install main dependencies
        Write-Status "Installing main dependencies..."
        $installOutput = & uv pip install -e . --link-mode=copy 2>&1 | ForEach-Object {
            if ($_ -is [System.Management.Automation.ErrorRecord]) {
                # Convert error records to strings (these are often just progress messages)
                $_.ToString()
            } else {
                $_
            }
        } | Out-String
        $installExitCode = $LASTEXITCODE

        if ($installExitCode -ne 0) {
            $ErrorActionPreference = $oldErrorAction
            Write-Error2 "Failed to install main dependencies"
            Write-Error2 "Exit code: $installExitCode"
            Write-Error2 "Output: $installOutput"
            Set-Location $originalLocation
            return $false
        }

        # Install development dependencies
        Write-Status "Installing development dependencies..."
        $devInstallOutput = & uv pip install -e ".[dev]" --link-mode=copy 2>&1 | ForEach-Object {
            if ($_ -is [System.Management.Automation.ErrorRecord]) {
                # Convert error records to strings (these are often just progress messages)
                $_.ToString()
            } else {
                $_
            }
        } | Out-String
        $devInstallExitCode = $LASTEXITCODE

        # Restore error action
        $ErrorActionPreference = $oldErrorAction

        if ($devInstallExitCode -ne 0) {
            Write-Error2 "Failed to install development dependencies"
            Write-Error2 "Exit code: $devInstallExitCode"
            Write-Error2 "Output: $devInstallOutput"
            Set-Location $originalLocation
            return $false
        }

        Write-Success "Python dependencies installed"
        Set-Location $originalLocation
        return $true
    } catch {
        # Restore error action if it was changed
        if ($oldErrorAction) {
            $ErrorActionPreference = $oldErrorAction
        }
        Write-Error2 "Failed to install dependencies: $_"
        Write-Error2 "Exception type: $($_.Exception.GetType().FullName)"
        Set-Location $originalLocation
        return $false
    }
}

function Initialize-PythonEnvironment {
    Write-Section "SETTING UP PYTHON ENVIRONMENT"

    # Create necessary directories
    if (-not (Test-Path "ml\scripts")) {
        New-Item -ItemType Directory -Path "ml\scripts" -Force | Out-Null
    }

    if (-not (Install-Uv)) { return $false }
    if (-not (Initialize-VirtualEnvironment)) { return $false }
    if (-not (Install-PythonDependencies)) { return $false }

    Write-Success "Python environment configured successfully"
    return $true
}

# DOCKER ENVIRONMENT

function Test-Docker {
    Write-Status "Validating Docker environment..."

    if (-not (Test-DockerRunning)) {
        Write-Error2 "Docker daemon is not running"
        Write-Status "Please start Docker Desktop or the Docker service"
        return $false
    }

    # Set the Docker Compose command
    $script:DOCKER_COMPOSE_CMD = Get-DockerComposeCommand
    $cmdDisplay = if ($script:DOCKER_COMPOSE_CMD -is [array]) {
        $script:DOCKER_COMPOSE_CMD -join " "
    } else {
        $script:DOCKER_COMPOSE_CMD
    }
    Write-Status "Using Docker Compose command: $cmdDisplay"

    Write-Success "Docker environment validated"
    return $true
}

function Initialize-Minio {
    Write-Status "Setting up MinIO for MLflow artifacts..."

    # Configuration
    $MINIO_ENDPOINT = "http://localhost:9000"
    $MINIO_CONSOLE = "http://localhost:9001"
    $MINIO_ACCESS_KEY = "minioadmin"
    $MINIO_SECRET_KEY = "minioadmin123"
    $BUCKET_NAME = "mlflow-artifacts"

    # Check if MinIO is running
    Write-Status "Checking if MinIO is running..."
    try {
        $response = Invoke-WebRequest -Uri "$MINIO_ENDPOINT/minio/health/live" -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
        Write-Success "MinIO is running"
    } catch {
        Write-Error2 "MinIO is not running or not accessible at $MINIO_ENDPOINT"
        $cmdDisplay = if ($script:DOCKER_COMPOSE_CMD -is [array]) {
            $script:DOCKER_COMPOSE_CMD -join " "
        } else {
            $script:DOCKER_COMPOSE_CMD
        }
        Write-Status "Please start MinIO first: $cmdDisplay up minio"
        return $false
    }

    # Create bucket using MinIO client
    Write-Status "Creating bucket: $BUCKET_NAME"

    if (Test-CommandExists "mc") {
        # Use local mc client
        Write-Status "Using local MinIO client"
        mc alias set myminio $MINIO_ENDPOINT $MINIO_ACCESS_KEY $MINIO_SECRET_KEY 2>&1 | Out-Null
        mc mb "myminio/$BUCKET_NAME" --ignore-existing 2>&1 | Out-Null
        Write-Success "Bucket created using local MinIO client"
    } else {
        # Use Docker to run mc client
        Write-Status "Using Docker MinIO client"
        docker run --rm --network ion-nutri-network minio/mc:latest mc alias set myminio http://ion-nutri-minio:9000 $MINIO_ACCESS_KEY $MINIO_SECRET_KEY 2>&1 | Out-Null
        docker run --rm --network ion-nutri-network minio/mc:latest mc mb "myminio/$BUCKET_NAME" --ignore-existing 2>&1 | Out-Null
        Write-Success "Bucket created using Docker MinIO client"
    }

    Write-Success "MinIO initialization completed!"
    Write-Status "MinIO Console: $MINIO_CONSOLE"
    Write-Status "MinIO API: $MINIO_ENDPOINT"
    Write-Status "Bucket: $BUCKET_NAME"
    Write-Status "Access Key: $MINIO_ACCESS_KEY"
    Write-Status "Secret Key: $MINIO_SECRET_KEY"

    return $true
}

function New-EnvFile {
    Write-Status "Configuring .env file..."

    $envContent = @"
# Docker Settings - Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password

# Application Settings
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# LLM Settings (adjust as needed)
OPENAI_API_KEY=your_key_here
"@

    if (Test-Path ".env") {
        $content = Get-Content ".env" -Raw
        if ($content -notmatch "NEO4J_URI") {
            Write-Status "Adding Docker configurations to existing .env..."
            Add-Content -Path ".env" -Value "`n$envContent"
            Write-Success "Docker configurations added to .env"
        } else {
            Write-Status ".env file already contains required configurations"
        }
    } else {
        if (Test-Path ".env.example") {
            Copy-Item ".env.example" ".env"
            Write-Success ".env file created from .env.example"
        } else {
            Set-Content -Path ".env" -Value $envContent
            Write-Success ".env file created with default configuration"
        }
    }

    return $true
}

function New-Directories {
    Write-Status "Creating necessary directories..."

    $directories = @("logs", "data\neo4j-import")

    foreach ($dir in $directories) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }

    Write-Success "Directories created successfully"
    return $true
}

function Build-Services {
    $composeFiles = Get-ComposeFiles

    Write-Step "Building services with Docker Compose..."

    try {
        if ($script:SERVICES) {
            Write-Status "Building services: $($script:SERVICES)"
            if ($script:DOCKER_COMPOSE_CMD -is [array]) {
                & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles build $script:SERVICES.Split()
            } else {
                & $script:DOCKER_COMPOSE_CMD $composeFiles build $script:SERVICES.Split()
            }
        } else {
            Write-Status "Building all services"
            if ($script:DOCKER_COMPOSE_CMD -is [array]) {
                & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles build
            } else {
                & $script:DOCKER_COMPOSE_CMD $composeFiles build
            }
        }

        if ($LASTEXITCODE -ne 0) {
            throw "Build failed"
        }

        Write-Success "Services built successfully"
        return $true
    } catch {
        Write-Error2 "Failed to build services: $_"
        return $false
    }
}

function Start-Services {
    $composeFiles = Get-ComposeFiles

    Write-Step "Starting services with Docker Compose..."

    try {
        if ($script:SERVICES) {
            Write-Status "Starting services: $($script:SERVICES)"
            if ($script:DOCKER_COMPOSE_CMD -is [array]) {
                & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles up -d $script:SERVICES.Split()
            } else {
                & $script:DOCKER_COMPOSE_CMD $composeFiles up -d $script:SERVICES.Split()
            }
        } else {
            Write-Status "Starting all services"
            if ($script:DOCKER_COMPOSE_CMD -is [array]) {
                & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles up -d
            } else {
                & $script:DOCKER_COMPOSE_CMD $composeFiles up -d
            }
        }

        if ($LASTEXITCODE -ne 0) {
            throw "Start failed"
        }

        Write-Success "Services started successfully"
        return $true
    } catch {
        Write-Error2 "Failed to start services: $_"
        return $false
    }
}

function Build-AndStartServices {
    Write-Status "Building and starting Docker services..."

    # Stop existing services
    $composeFiles = Get-ComposeFiles
    try {
        if ($script:DOCKER_COMPOSE_CMD -is [array]) {
            & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles down 2>&1 | Out-Null
        } else {
            & $script:DOCKER_COMPOSE_CMD $composeFiles down 2>&1 | Out-Null
        }
    } catch {}

    # Build services (unless skipped)
    if (-not $script:SKIP_BUILD) {
        if (-not (Build-Services)) {
            return $false
        }
    }

    # Start services (unless build-only)
    if (-not $script:BUILD_ONLY) {
        if (-not (Start-Services)) {
            return $false
        }
    }

    return $true
}

function Wait-ForNeo4j {
    Write-Status "Waiting for Neo4j to be ready..."

    $composeFiles = Get-ComposeFiles
    $count = 0

    while ($count -lt $script:NEO4J_TIMEOUT) {
        try {
            if ($script:DOCKER_COMPOSE_CMD -is [array]) {
                $output = & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles exec -T neo4j cypher-shell -u $script:NEO4J_USER -p $script:NEO4J_PASSWORD "RETURN 1" 2>&1
            } else {
                $output = & $script:DOCKER_COMPOSE_CMD $composeFiles exec -T neo4j cypher-shell -u $script:NEO4J_USER -p $script:NEO4J_PASSWORD "RETURN 1" 2>&1
            }

            if ($LASTEXITCODE -eq 0) {
                Write-Success "Neo4j is ready"
                return $true
            }
        } catch {}

        if (($count % 10 -eq 0) -and ($count -gt 0)) {
            Write-Status "Still waiting for Neo4j... ($count/$($script:NEO4J_TIMEOUT)s)"
        }

        $count++
        Start-Sleep -Seconds 1
    }

    Write-Error2 "Timeout waiting for Neo4j"
    $cmdDisplay = if ($script:DOCKER_COMPOSE_CMD -is [array]) {
        $script:DOCKER_COMPOSE_CMD -join " "
    } else {
        $script:DOCKER_COMPOSE_CMD
    }
    Write-Warning2 "Check the logs: $cmdDisplay logs neo4j"
    return $false
}

function Test-ApocExtension {
    Write-Status "Testing APOC extension..."

    $composeFiles = Get-ComposeFiles

    try {
        if ($script:DOCKER_COMPOSE_CMD -is [array]) {
            $result = & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles exec -T neo4j cypher-shell -u $script:NEO4J_USER -p $script:NEO4J_PASSWORD "CALL apoc.help('apoc') YIELD name RETURN count(name) > 0 as apoc_available" --format plain 2>&1 | Select-Object -Last 1
        } else {
            $result = & $script:DOCKER_COMPOSE_CMD $composeFiles exec -T neo4j cypher-shell -u $script:NEO4J_USER -p $script:NEO4J_PASSWORD "CALL apoc.help('apoc') YIELD name RETURN count(name) > 0 as apoc_available" --format plain 2>&1 | Select-Object -Last 1
        }

        if ($result -match "true") {
            Write-Success "APOC extension is working correctly"
            return $true
        } else {
            Write-Error2 "APOC extension is not working properly"
            return $false
        }
    } catch {
        Write-Error2 "Failed to test APOC extension: $_"
        return $false
    }
}

function Wait-ForApi {
    Write-Status "Checking API availability..."

    Start-Sleep -Seconds 5  # Give API time to start

    $count = 0
    while ($count -lt $script:API_TIMEOUT) {
        try {
            $response = Invoke-WebRequest -Uri "http://127.0.0.1:$($script:API_PORT)/health" -UseBasicParsing -TimeoutSec 2 -ErrorAction Stop
            if ($response.StatusCode -eq 200) {
                Write-Success "API is ready and responding"
                return $true
            }
        } catch {}

        $count++
        Start-Sleep -Seconds 1
    }

    Write-Warning2 "API may not be fully ready yet (this is normal if /health endpoint doesn't exist)"
    return $true
}

function Initialize-DockerEnvironment {
    Write-Section "SETTING UP DOCKER ENVIRONMENT"

    if (-not (Test-Docker)) { return $false }
    if (-not (New-EnvFile)) { return $false }
    if (-not (New-Directories)) { return $false }
    Get-VersionInfo
    if (-not (Build-AndStartServices)) { return $false }

    # Only wait for services if they were started
    if (-not $script:BUILD_ONLY) {
        if (-not (Wait-ForNeo4j)) { return $false }
        if (-not (Test-ApocExtension)) { return $false }
        if (-not (Initialize-Minio)) { return $false }
        Wait-ForApi | Out-Null
    }

    Write-Success "Docker environment configured successfully"
    return $true
}

# INFORMATION DISPLAY

function Show-FinalInfo {
    Write-Section "SETUP COMPLETE"

    $cmdDisplay = if ($script:DOCKER_COMPOSE_CMD -is [array]) {
        $script:DOCKER_COMPOSE_CMD -join " "
    } else {
        $script:DOCKER_COMPOSE_CMD
    }

    Write-Host @"

Development environment successfully configured!

Python Environment:
  - Virtual environment: .venv\
  - Activation (PowerShell): .venv\Scripts\Activate.ps1
  - Activation (CMD): .venv\Scripts\activate.bat

Docker Services:
  - Neo4j Browser: http://localhost:$($script:NEO4J_BROWSER_PORT)
  - Neo4j Bolt: $($script:NEO4J_URI)
  - PostgreSQL: localhost:5432
  - MinIO Console: http://localhost:9001
  - MinIO API: http://localhost:9000
  - MLflow: http://localhost:5000
  - FastAPI API: http://localhost:$($script:API_PORT)
  - API Documentation: http://localhost:$($script:API_PORT)/docs
  - Version Information: http://localhost:$($script:API_PORT)/version

Service Credentials:
  - Neo4j User: $($script:NEO4J_USER)
  - Neo4j Password: $($script:NEO4J_PASSWORD)
  - PostgreSQL User: mlflow
  - PostgreSQL Password: mlflow_password
  - PostgreSQL Database: mlflow
  - MinIO Access Key: minioadmin
  - MinIO Secret Key: minioadmin123

Build Information:
  - Environment: $Environment
  - Git Commit: $($script:GIT_COMMIT)
  - Git Branch: $($script:GIT_BRANCH)
  - Build Time: $($script:BUILD_TIME)

Useful Commands:
  - View logs: $cmdDisplay logs -f
  - Stop services: $cmdDisplay down
  - Restart services: $cmdDisplay restart
  - Neo4j shell: $cmdDisplay exec neo4j cypher-shell -u $($script:NEO4J_USER) -p $($script:NEO4J_PASSWORD)

Current Service Status:
"@

    $composeFiles = Get-ComposeFiles
    try {
        if ($script:DOCKER_COMPOSE_CMD -is [array]) {
            & $script:DOCKER_COMPOSE_CMD[0] $script:DOCKER_COMPOSE_CMD[1] $composeFiles ps
        } else {
            & $script:DOCKER_COMPOSE_CMD $composeFiles ps
        }
    } catch {
        Write-Host "  (Run '$cmdDisplay ps' to see detailed status)"
    }

    Write-Host ""
    Write-Host "You can now start developing!" -ForegroundColor Green
}

# HELP FUNCTION

function Show-Help {
    Get-Help $PSCommandPath -Detailed
}

# MAIN FUNCTION

function Main {
    try {
        # Show environment info
        Write-Host "PowerShell Version: $($PSVersionTable.PSVersion)" -ForegroundColor Gray
        Write-Host "Execution Policy: $(Get-ExecutionPolicy)" -ForegroundColor Gray
        Write-Host "Current Directory: $PWD" -ForegroundColor Gray
        Write-Host ""

        # Show help if requested
        if ($Help) {
            Show-Help
            exit 0
        }

        # Handle specific setup modes
        if ($PythonOnly) {
            Write-Status "Setting up Python environment only..."
            if (-not (Test-Requirements "full")) { exit 1 }
            if (-not (Initialize-PythonEnvironment)) { exit 1 }
            Write-Success "Python environment setup completed"
            exit 0
        }

        if ($DockerOnly) {
            Write-Status "Setting up Docker environment only..."
            if (-not (Test-Requirements "full")) { exit 1 }
            if (-not (Initialize-DockerEnvironment)) { exit 1 }
            Show-FinalInfo
            exit 0
        }

        if ($MinioOnly) {
            Write-Status "Setting up MinIO only..."
            if (-not (Test-Requirements "minio-only")) { exit 1 }
            if (-not (Initialize-Minio)) { exit 1 }
            Write-Success "MinIO setup completed"
            exit 0
        }

        # Complete setup
        Write-Status "Setting up complete development environment..."
        Write-Status "Environment: $Environment"

        if (-not (Test-Requirements "full")) { exit 1 }
        if (-not (Initialize-PythonEnvironment)) { exit 1 }
        if (-not (Initialize-DockerEnvironment)) { exit 1 }

        # Only show final info if services were started
        if (-not $script:BUILD_ONLY) {
            Show-FinalInfo
        } else {
            Write-Success "Build completed successfully!"
        }

    } catch {
        Invoke-Cleanup
        Write-Error2 "An error occurred: $_"
        Write-Error2 $_.ScriptStackTrace
        exit 1
    }
}

# SCRIPT EXECUTION

# Change to script directory
Push-Location $PSScriptRoot

try {
    Main
} finally {
    Pop-Location
}

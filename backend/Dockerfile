FROM python:3.13-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install system dependencies
# - curl, git: Basic utilities
# - wkhtmltopdf: PDF generation from HTML (required for report PDFs)
# - fontconfig, lib*: Dependencies for wkhtmltopdf
# - xfonts-*, fonts-*: Font packages for proper PDF rendering
RUN apt-get update && apt-get install -y \
    curl \
    git \
    wkhtmltopdf \
    fontconfig \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
    fonts-liberation \
    fonts-dejavu-core \
    fonts-freefont-ttf \
    fonts-roboto \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash appuser

COPY pyproject.toml uv.lock* ./

RUN chown -R appuser:appuser /app

USER appuser

RUN uv sync --no-install-project

# Copy source code
COPY ./app ./app

# Copy configuration files
COPY strategy_config.yaml ./

# Copy git information if available (for build metadata)
COPY .git* ./

# Fix ownership of all files (needed because COPY operations run as root)
USER root
RUN mkdir -p /app/app/artifacts
RUN chown -R appuser:appuser /app
USER appuser

# Set build-time environment variables
ARG BUILD_TIME
ARG GIT_COMMIT
ARG GIT_BRANCH
ARG BUILD_NUMBER
ARG ENVIRONMENT=production

ENV BUILD_TIME=${BUILD_TIME}
ENV GIT_COMMIT=${GIT_COMMIT}
ENV GIT_BRANCH=${GIT_BRANCH}
ENV BUILD_NUMBER=${BUILD_NUMBER}
ENV ENVIRONMENT=${ENVIRONMENT}

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

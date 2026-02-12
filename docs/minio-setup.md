# MinIO Setup for MLflow Artifacts

This document explains how to set up MinIO for MLflow artifact storage in the Ion Nutri project.

## Overview

MinIO is used as an S3-compatible object storage service for MLflow artifacts. It stores model files, logs, and other artifacts generated during MLflow tracking and tracing.

## Quick Setup

### Automatic Setup (Recommended)

The project includes automatic MinIO initialization:

1. **Docker Compose Setup**: The `docker-compose.yml` includes a `minio-init` service that automatically creates the required bucket.

2. **Setup Script**: Run the setup script which includes MinIO initialization:
   ```bash
   ./setup.sh
   ```

   Or run MinIO setup only:
   ```bash
   ./setup.sh --minio-only
   ```

### Manual Setup

If you need to set up MinIO manually:

1. **Start MinIO**:
   ```bash
   docker-compose up minio -d
   ```

2. **Initialize MinIO**:
   ```bash
   ./setup.sh --minio-only
   ```

3. **Start remaining services**:
   ```bash
   docker-compose up -d
   ```

## Configuration

### MinIO Credentials

- **Access Key**: `minioadmin`
- **Secret Key**: `minioadmin123`
- **Endpoint**: `http://localhost:9000` (external) / `http://ion-nutri-minio:9000` (internal)
- **Console**: `http://localhost:9001`

### Buckets

- **mlflow-artifacts**: Main bucket for MLflow artifacts

### Environment Variables

The following environment variables are automatically configured:

```bash
# MinIO Configuration
AWS_ACCESS_KEY_ID=minioadmin
AWS_SECRET_ACCESS_KEY=minioadmin123
AWS_DEFAULT_REGION=us-east-1
MLFLOW_S3_ENDPOINT_URL=http://ion-nutri-minio:9000
MLFLOW_S3_IGNORE_TLS=true
MLFLOW_S3_VERIFY_SSL=false
```

## Troubleshooting

### Common Issues

1. **"NoCredentialsError: Unable to locate credentials"**
   - **Cause**: The `mlflow-artifacts` bucket doesn't exist
   - **Solution**: Run `./setup.sh --minio-only` or restart with `docker-compose up -d`

2. **MinIO not accessible**
   - **Cause**: MinIO service not running
   - **Solution**: Check if MinIO is running: `docker-compose ps minio`

3. **Bucket creation fails**
   - **Cause**: MinIO not fully initialized
   - **Solution**: Wait for MinIO health check to pass, then retry or run `./setup.sh --minio-only`

### Verification

1. **Check MinIO status**:
   ```bash
   curl http://localhost:9000/minio/health/live
   ```

2. **Access MinIO Console**:
   - Open: http://localhost:9001
   - Login with: `minioadmin` / `minioadmin123`

3. **List buckets**:
   ```bash
   mc alias set myminio http://localhost:9000 minioadmin minioadmin123
   mc ls myminio
   ```

## Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    API      │    │   MLflow    │    │   MinIO     │
│  Service    │    │   Server    │    │   Storage   │
└─────────────┘    └─────────────┘    └─────────────┘
       │                   │                   │
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                    ┌─────────────┐
                    │ PostgreSQL  │
                    │   Database  │
                    └─────────────┘
```

- **API Service**: Connects to MLflow for tracking and MinIO for artifacts
- **MLflow Server**: Uses PostgreSQL for metadata and MinIO for artifacts
- **MinIO**: S3-compatible storage for MLflow artifacts

## Development

### Local Development

For local development, you can use the MinIO client (`mc`) to manage buckets:

```bash
# Install MinIO client (optional)
# macOS: brew install minio/stable/mc
# Linux: wget https://dl.min.io/client/mc/release/linux-amd64/mc

# Configure client
mc alias set myminio http://localhost:9000 minioadmin minioadmin123

# List buckets
mc ls myminio

# Create bucket manually
mc mb myminio/mlflow-artifacts

# List objects in bucket
mc ls myminio/mlflow-artifacts
```

### Production Considerations

For production deployments:

1. **Security**: Change default credentials
2. **Persistence**: Ensure proper volume mounting
3. **Backup**: Implement backup strategies for MinIO data
4. **Monitoring**: Set up monitoring for MinIO health and usage

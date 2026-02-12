# Session: Frontend Staging Deployment and Repository Refactoring

**Date:** 2026-01-27
**Topic:** Add frontend to staging Kubernetes deployment and refactor repository structure into backend/frontend monorepo

---

## 🎯 Initial Goal

Evaluate if the frontend is being deployed to staging environment and implement it if missing.

---

## 🔍 Initial Analysis

### Current Staging Deployment Status

**Investigation:** Checked `k8s/staging.yml` and `.github/workflows/build.yml`

**Finding:** ❌ Frontend was **NOT** deployed to staging

**Current staging deployment included only:**
- API container (Port 8000)
- Neo4j database (Ports 7474/7687)

**Frontend service existed only in:**
- `docker-compose.yml` (local development)

---

## 📋 Implementation Plan

### Phase 1: Repository Restructuring

**Decision:** Refactor repository to use `backend/` and `frontend/` directories for better organization

**Rationale:**
- Clear separation of concerns
- Better scalability for monorepo structure
- Aligns with industry best practices

### Phase 2: Add Frontend to Staging

**Approach:**
- Add Kubernetes manifests for frontend
- Configure nginx with API proxy
- Update CI/CD pipeline to build and deploy both services
- Use same ECR repository with different tag prefixes

---

## 🛠️ Implementation Steps

### 1. Repository Restructuring ✅

**Moved backend code to `backend/` directory:**
```
app/                → backend/app/
tests/              → backend/tests/
Dockerfile          → backend/Dockerfile
pyproject.toml      → backend/pyproject.toml
uv.lock            → backend/uv.lock
strategy_config.yaml → backend/strategy_config.yaml
```

**Updated configuration files:**
- ✅ `docker-compose.yml` - Changed build context to `./backend`
- ✅ `docker-compose.override.yml` - Updated paths and volumes
- ✅ `docker-compose.prod.yml` - Updated artifact paths
- ✅ `.pre-commit-config.yaml` - Updated file patterns to `backend/app`, `backend/tests`
- ✅ `setup.sh` - Modified to work from backend directory
- ✅ `CLAUDE.md` - Added notes about running uv from backend/
- ✅ `README.md` - Updated project structure documentation

### 2. Kubernetes Staging Configuration ✅

**Updated `k8s/staging.yml`:**

**API Changes:**
- Renamed deployment: `ion-nutri-staging` → `ion-nutri-staging-api`
- Service type: `NodePort` → `ClusterIP` (internal only)

**Frontend Addition:**
- **Deployment:** `ion-nutri-staging-frontend`
  - Image: `ion-nutri:frontend-latest-staging`
  - Port 80 exposed
  - No ConfigMap (nginx config baked into image)

- **Service:** `ion-nutri-staging-frontend` (NodePort)
  - Exposes frontend externally

**Initial ConfigMap Approach (Later Removed):**
- Initially created ConfigMap for nginx configuration
- **Refactored:** Moved to `frontend/nginx.staging.conf` and bake into Docker image at build time
- **Benefit:** Simpler deployment, no runtime configuration needed

### 3. Frontend Docker Configuration ✅

**Created `frontend/nginx.staging.conf`:**
```nginx
location /api/ {
    proxy_pass http://ion-nutri-staging-api/;
    # ... proxy headers and configuration
}
```

**Updated `frontend/Dockerfile`:**
```dockerfile
ARG NGINX_CONFIG=nginx.conf
ARG VITE_API_URL=http://localhost:8000

ENV VITE_API_URL=$VITE_API_URL

COPY ${NGINX_CONFIG} /etc/nginx/conf.d/default.conf
```

**Benefits:**
- Environment-specific nginx configs
- Configuration baked in at build time
- Supports different API URLs per environment

### 4. CI/CD Pipeline Updates ✅

**Modified `.github/workflows/build.yml`:**

**Backend Build:**
```yaml
- name: Build, tag, and push the Backend image
  run: |
    docker build \
      -t $ECR_REGISTRY/$ECR_REPOSITORY:backend-$IMAGE_TAG \
      -t $ECR_REGISTRY/$ECR_REPOSITORY:backend-latest-staging \
      -f backend/Dockerfile \
      ./backend
```

**Frontend Build:**
```yaml
- name: Build, tag, and push the Frontend image
  run: |
    docker build \
      --build-arg VITE_API_URL=/api \
      --build-arg NGINX_CONFIG=nginx.staging.conf \
      -t $ECR_REGISTRY/$ECR_REPOSITORY:frontend-$IMAGE_TAG \
      -t $ECR_REGISTRY/$ECR_REPOSITORY:frontend-latest-staging \
      -f frontend/Dockerfile \
      ./frontend
```

**Deployment:**
```yaml
kubectl set image deployment/ion-nutri-staging-api api=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG_BACKEND
kubectl set image deployment/ion-nutri-staging-frontend frontend=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG_FRONTEND
```

**Tag Strategy:**
- Backend: `backend-{hash}-{timestamp}`, `backend-latest-staging`
- Frontend: `frontend-{hash}-{timestamp}`, `frontend-latest-staging`
- **Single ECR repository:** `ion-nutri` with different tag prefixes

---

## 🐛 Issues Encountered and Resolved

### Issue 1: MLflow Health Check Failing ❌

**Symptom:**
```
Container ion-nutri-mlflow (unhealthy)
```

**Root Cause:** MLflow container image didn't have `curl` installed for health check

**Solution:**
```dockerfile
# Dockerfile.mlflow
FROM ghcr.io/mlflow/mlflow:v3.8.1

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
```

**Additional Fix:** Pinned MLflow to `v3.8.1` for reproducibility

### Issue 2: MLflow Database Schema Mismatch ❌

**Symptom:**
```
ERROR: Detected out-of-date database schema (found version 1bd49d398cd23, but expected 2c33131f4dae)
```

**Root Cause:** Upgrading from `latest` to `v3.8.1` required database migration

**Solution:**
```bash
docker compose run --rm mlflow mlflow db upgrade postgresql://mlflow:mlflow_password@ion-nutri-postgres:5432/mlflow
```

**Alternative (used):** Recreated PostgreSQL database with fresh schema

### Issue 3: Frontend Health Check Failing ❌

**Symptom:**
```
Container ion-nutri-frontend (unhealthy)
wget: can't connect to remote host: Connection refused
```

**Root Cause:** Alpine Linux containers don't resolve `localhost` properly

**Investigation:**
```bash
# Failed
wget --spider http://localhost/health

# Worked
wget --spider http://127.0.0.1/health
```

**Solution:**
```yaml
# docker-compose.yml
healthcheck:
  test: ["CMD-SHELL", "wget --quiet --tries=1 --spider http://127.0.0.1/health || exit 1"]
```

### Issue 4: MLflow Experiment Not Found ❌

**Symptom:**
```
mlflow.exceptions.RestException: RESOURCE_DOES_NOT_EXIST: No Experiment with id=1 exists
```

**Root Cause:** Fresh PostgreSQL database had no experiments

**Initial Manual Fix (Incorrect Approach):**
```bash
curl -X POST http://localhost:5000/api/2.0/mlflow/experiments/create \
  -d '{"name": "ion-nutri-reports"}'
```

**Correct Solution:** ✅ The code already handles this automatically!

**Code Investigation:**
```python
# backend/app/main.py
@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_mlflow()  # Calls mlflow.set_experiment() which auto-creates
    yield

# backend/app/core/config.py
def configure_mlflow():
    mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
    mlflow.set_experiment(settings.MLFLOW_EXPERIMENT_NAME)  # Auto-creates if doesn't exist
```

**Lesson Learned:** Trust the code first! Simply restarting services let the code do its job.

### Issue 5: setup.sh Validation Failed ❌

**Symptom:**
```
[ERROR] Missing requirements:
  • Dockerfile
```

**Root Cause:** Script looking for Dockerfile in root, but it was moved to `backend/`

**Solution:**
```bash
# setup.sh
if ! file_exists "backend/Dockerfile"; then
    missing_requirements+=("backend/Dockerfile")
fi
```

---

## 🎯 Final Architecture

### Staging Deployment Architecture

```
User Browser
    ↓
Frontend Service (NodePort) - External access
    ↓
Frontend Pod (nginx + React SPA)
    ↓ /api/* requests proxied
API Service (ClusterIP) - Internal only
    ↓
API Pod + Neo4j Sidecar
```

### Repository Structure

```
ion-nutri/
├── backend/                    # Backend application
│   ├── app/                   # FastAPI code
│   │   ├── api/              # API endpoints
│   │   ├── core/             # Core configuration
│   │   ├── db/               # Database layer
│   │   ├── domain/           # Domain models
│   │   ├── plugins/          # Plugin system
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── scripts/          # Utility scripts
│   │   └── services/         # Business logic
│   ├── tests/                # Backend tests
│   │   ├── unit/            # Unit tests
│   │   ├── integration/     # Integration tests
│   │   ├── e2e/             # End-to-end tests
│   │   └── performance/     # Performance tests
│   ├── Dockerfile           # Backend container image
│   ├── pyproject.toml       # Python dependencies
│   ├── uv.lock             # Dependency lock file
│   └── strategy_config.yaml # Strategy configuration
├── frontend/                  # Frontend application
│   ├── src/                  # React source code
│   ├── Dockerfile            # Frontend container image
│   ├── nginx.conf            # Local nginx config
│   ├── nginx.staging.conf    # Staging nginx config
│   └── package.json          # Node dependencies
├── k8s/                      # Kubernetes manifests
│   └── staging.yml           # Staging deployment
├── docker-compose.yml        # Local development
└── .github/workflows/        # CI/CD pipelines
    └── build.yml            # Build and deploy workflow
```

### Service Status (Final)

```
✅ Frontend     - http://localhost:3001 (healthy)
✅ API          - http://localhost:8000 (healthy)
✅ MLflow       - http://localhost:5000 (healthy)
✅ Neo4j        - http://localhost:7474 (healthy)
✅ PostgreSQL   - localhost:5432 (healthy)
✅ MinIO        - http://localhost:9001 (healthy)
```

---

## 📦 Deliverables

### Git Commit

**Branch:** `feat/add-frontend-staging-and-refactor-repo-structure`

**Commit Stats:**
- 169 files changed
- 202 insertions(+)
- 48 deletions(-)

**Major Changes:**
- All backend files moved to `backend/`
- Frontend deployment added to staging
- CI/CD pipeline updated for dual builds
- Health checks fixed for all services
- MLflow pinned to v3.8.1

### Pull Request

**PR #98:** https://github.com/edgebr/ion-nutri/pull/98

**Title:** feat: add frontend to staging and refactor repository structure

**Base Branch:** `develop`

**Description Highlights:**
- Comprehensive summary of changes
- Architecture diagram
- Testing status
- Migration notes
- Next steps for deployment

---

## 📝 Key Learnings

### 1. Trust the Code First ⭐
- **Bad:** Manually creating MLflow experiments with curl
- **Good:** Understanding that `mlflow.set_experiment()` auto-creates experiments
- **Lesson:** Investigate code behavior before manual interventions

### 2. Alpine Linux Networking ⭐
- Alpine containers use musl libc, not glibc
- `localhost` resolution behaves differently
- **Solution:** Use `127.0.0.1` explicitly in health checks

### 3. Docker Image Versioning ⭐
- **Bad:** Using `latest` tags (unpredictable)
- **Good:** Pinning specific versions (e.g., `v3.8.1`)
- **Benefit:** Reproducible builds, predictable behavior

### 4. Configuration Management ⭐
- **Bad:** Runtime configuration via ConfigMaps (more complex)
- **Good:** Bake configuration into Docker image at build time
- **Benefit:** Simpler deployments, no runtime dependencies

### 5. Monorepo Organization ⭐
- Clear `backend/` and `frontend/` separation
- Single repository for related services
- Unified CI/CD pipeline
- Better developer experience

---

## 🚀 Next Steps

### When PR is Merged to Main

1. **GitHub Actions will automatically:**
   - Build backend image: `ion-nutri:backend-{hash}-{timestamp}`
   - Build frontend image: `ion-nutri:frontend-{hash}-{timestamp}`
   - Push both to ECR
   - Deploy both to staging Kubernetes cluster

2. **Manual Steps Required:**
   - Verify staging deployment health
   - Test frontend → API communication
   - Verify MLflow experiment creation works

3. **Production Deployment:**
   - Create production Kubernetes manifests
   - Update workflow for production deployment
   - Configure production environment variables

---

## 🔧 Configuration Notes

### Environment Variables (Backend)

```bash
# MLflow Configuration
MLFLOW_TRACKING_URI=http://ion-nutri-mlflow:5000
MLFLOW_EXPERIMENT_NAME=ion-nutri-reports

# Neo4j Configuration
NEO4J_URI=bolt://ion-nutri-neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

### Build Arguments (Frontend)

```bash
# Local Development
VITE_API_URL=http://localhost:8000
NGINX_CONFIG=nginx.conf

# Staging
VITE_API_URL=/api
NGINX_CONFIG=nginx.staging.conf
```

### Docker Compose Commands

```bash
# Start all services
docker compose up -d

# Restart after changes
docker compose restart api frontend

# View logs
docker compose logs -f api frontend

# Check health
docker compose ps
```

---

## 📚 References

### Files Modified

**Configuration:**
- `.github/workflows/build.yml` - CI/CD pipeline
- `k8s/staging.yml` - Kubernetes manifests
- `docker-compose.yml` - Local development
- `docker-compose.override.yml` - Dev overrides
- `docker-compose.prod.yml` - Production config
- `.pre-commit-config.yaml` - Pre-commit hooks
- `setup.sh` - Development setup
- `README.md` - Documentation
- `CLAUDE.md` - AI assistant rules

**Backend:**
- All files moved to `backend/` directory

**Frontend:**
- `frontend/Dockerfile` - Enhanced with build args
- `frontend/nginx.staging.conf` - New staging config

**Infrastructure:**
- `Dockerfile.mlflow` - Pinned version + curl

### External Resources

- MLflow Documentation: https://mlflow.org/docs/latest/
- Kubernetes Documentation: https://kubernetes.io/docs/
- Docker Compose Documentation: https://docs.docker.com/compose/
- GitHub Actions Documentation: https://docs.github.com/en/actions

---

## 🔄 Additional Fixes (Pre-Merge)

### Issue 6: Pre-commit Hook Configuration ❌

**Symptom:**
```
`pre-commit` not found.  Did you forget to activate your virtualenv?
```

**Root Cause:** 
- Git pre-commit hook was pointing to old, non-existent path: `/home/warley/dev/ion-nutri/.venv/bin/python`
- Current repository is at `/home/warley/life/1-projects/work/ion-nutri` with venv in `backend/.venv`
- `pip-audit` hook in `.pre-commit-config.yaml` wasn't configured to run from backend directory

**Investigation:**
```bash
# Check hook configuration
cat .git/hooks/pre-commit | head -20
# INSTALL_PYTHON=/home/warley/dev/ion-nutri/.venv/bin/python  # ❌ Wrong path

# Check where pre-commit is actually installed
cd backend && uv run which pre-commit
# /home/warley/life/1-projects/work/ion-nutri/backend/.venv/bin/pre-commit  # ✅ Correct
```

**Solution:**

1. **Updated `.pre-commit-config.yaml`** to run `pip-audit` from backend directory:
```yaml
- repo: local
  hooks:
    - id: pip-audit
      name: pip-audit
      entry: bash -c 'cd backend && uv run --no-sync pip-audit --local --desc --format=json'
      language: system
      pass_filenames: false
```

2. **Reinstalled pre-commit hooks** from backend environment:
```bash
cd backend && uv run pre-commit install
```

3. **Verified the fix** - Updated hook now points to correct path:
```bash
INSTALL_PYTHON=/home/warley/life/1-projects/work/ion-nutri/backend/.venv/bin/python3
```

**Results:**
- ✅ Pre-commit hooks now execute successfully
- ✅ All hooks (ruff, mypy, pip-audit, etc.) run from correct environment
- ✅ Formatting fixes applied automatically on commit

**Commits:**
- `2f68ca4` - style: apply pre-commit formatting fixes
- `73efaba` - fix: update pip-audit hook to run from backend directory

---

## ✅ Summary

Successfully implemented frontend deployment to staging and refactored the repository structure into a clean monorepo with `backend/` and `frontend/` directories. All services are healthy and tested locally. CI/CD pipeline updated to build and deploy both services automatically. Pull request created and additional pre-commit configuration fixes applied.

**Total Time:** ~4 hours
**Complexity:** High
**Impact:** Major architectural improvement
**Status:** ✅ Complete and ready for merge

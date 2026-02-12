# Deployment - Ion Nutri

Simple guide to deploy the Ion Nutri application from scratch.

## Prerequisites

- **Docker** and **Docker Compose** installed
  - For Windows users: Download [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)
- **Minimum 10-15 GB free disk space** (recommended: 15-20 GB)

### 2. Run Setup

**Linux/macOS:**
```bash
./setup.sh
```

**Windows (PowerShell):**
```powershell
.\setup.ps1
```

**What happens:**
- Creates the `.env` file (if it doesn't exist) with default settings
- Installs Python environment with uv

**Note:** If you get a "uv: command not found" error on first run, restart your shell and run the setup again:
```bash
# Restart shell or source your profile
source ~/.bashrc  # or ~/.zshrc for zsh users
./setup.sh
```

### 3. Configure API Key
```bash
# Edit the .env file (created by setup.sh)
nano .env

# Replace with your actual key:
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### 4. Restart Services
```bash
docker compose down && docker compose up -d
```

### 5. Populate Database (AUTOMATIC)

The database population is **now completely automatic**! 

When you run `./setup.sh` or `docker compose up -d`, the `load-data` service:
- Automatically waits for Neo4j to be healthy
- Loads medical ontology (metabolites, pathways, symptoms)
- Populates knowledge base for reports
- Completes before API starts

**No manual steps needed!** The API will only start after data loading is complete.

**Monitor the data loading:**
```bash
docker compose logs -f load-data
```

**Old Manual Method (NO LONGER NEEDED):**
```bash
# This is not needed anymore
# cd backend/app/scripts/load_data && python main.py
```

**What happens automatically:**
- Creates structures in Neo4j
- Loads medical ontology
- Populates knowledge base for reports
- Ensures database is ready before API starts

## Verification

Wait a few minutes and access:

- **Frontend**: http://localhost:3001
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Neo4j Browser**: http://localhost:7474
- **MLflow**: http://localhost:5000
- **MinIO Console**: http://localhost:9001


## Useful Commands

```bash
# View logs
docker compose logs -f

# View only data loading logs
docker compose logs -f load-data

# Stop everything
docker compose down

# Restart after .env changes
docker compose down && docker compose up -d

# View service status
docker compose ps
```

## Troubleshooting

### API not starting
Check if data loading completed:
```bash
docker compose logs load-data
```

### Data loading failed
Ensure these files exist:
- `processed_data/ontology_with_ranges.json`
- `processed_data/ontology.json`

Then restart:
```bash
docker compose down
docker compose up -d
```

## Next Steps

After deployment, see [USAGE.md](USAGE.md) to learn how to use the application.

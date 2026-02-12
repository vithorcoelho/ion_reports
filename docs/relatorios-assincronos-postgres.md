# Relatórios Assíncronos com PostgreSQL (API + Worker)

## Objetivo

Implementar geração assíncrona de relatórios mantendo o endpoint atual, com o mínimo de alteração estrutural:

- manter `POST /api/v1/reports` com `?async=true`
- criar endpoint para consultar resultado
- persistir no PostgreSQL:
  - payload de entrada do job
  - status da fila
  - markdown final
  - PDF final em binário (`BYTEA`)
- processar jobs em container `worker` separado
- fornecer um compose recomendado para produção simplificada

## O que foi alterado

## 1. Endpoint de criação de relatório

Arquivo: `backend/app/api/v1/reports.py`

- `POST /api/v1/reports/` agora aceita query param `async`:
  - `async=false` (padrão): comportamento síncrono original
  - `async=true`: cria job na fila (PostgreSQL) e retorna `job_id`

Resposta assíncrona:

```json
{
  "job_id": "uuid",
  "status": "queued",
  "message": "Relatório enfileirado para processamento assíncrono."
}
```

## 2. Novos endpoints de consulta

Arquivo: `backend/app/api/v1/reports.py`

- `GET /api/v1/reports/jobs/{job_id}`
  - retorna status (`queued|running|completed|failed`)
  - retorna markdown quando concluído
  - informa se existe PDF (`has_pdf`)
- `GET /api/v1/reports/jobs/{job_id}/pdf`
  - retorna PDF binário armazenado no PostgreSQL
  - só funciona quando status = `completed`

## 3. Persistência de jobs no PostgreSQL

Arquivo: `backend/app/db/report_job_repository.py`

Tabela criada automaticamente: `report_jobs`

Campos principais:

- `id` (UUID)
- `status` (`queued`, `running`, `completed`, `failed`)
- `exam_type`
- `request_payload` (JSONB)
- `result_markdown` (TEXT)
- `result_pdf` (BYTEA)
- `error_message`
- `worker_id`
- timestamps (`created_at`, `updated_at`, `started_at`, `finished_at`)

Operações implementadas:

- criar job
- claim atômico com `FOR UPDATE SKIP LOCKED`
- marcar concluído (markdown + PDF)
- marcar falha
- consultar job
- recuperar PDF

## 4. Worker assíncrono separado

Arquivo: `backend/app/workers/report_worker.py`

Fluxo:

1. faz polling da tabela `report_jobs`
2. faz claim de um job `queued`
3. reconstrói payload (`exam_data`, `anamnesis`, `exam_type`)
4. gera markdown via `ReportCoordinator`
5. gera PDF via `PDFService`
6. salva markdown + PDF no PostgreSQL
7. atualiza status para `completed` ou `failed`

Execução:

```bash
uv run python -m app.workers.report_worker
```

## 5. Configuração

Arquivo: `backend/app/core/config.py`

Novas variáveis:

- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `REPORT_JOBS_DATABASE_URL` (opcional, sobrescreve as anteriores)
- `REPORT_WORKER_POLL_INTERVAL_SECONDS`

## 6. Dependência Python

Arquivo: `backend/pyproject.toml`

- adicionada: `psycopg[binary]>=3.2.9`

## 7. Compose recomendado

Arquivo: `docker-compose.recommended.yml`

Serviços:

- `postgres` (fila + resultados)
- `neo4j` (base de conhecimento)
- `load-data` (carga inicial no neo4j)
- `api` (FastAPI)
- `worker` (processamento assíncrono)

Sem dependência de MLflow/MinIO para o fluxo de geração assíncrona.

## Fluxo final de integração

1. Cliente chama:

```http
POST /api/v1/reports?async=true
```

2. API retorna `job_id` imediatamente.
3. Cliente consulta:

```http
GET /api/v1/reports/jobs/{job_id}
```

4. Quando `status=completed`:
  - markdown disponível no mesmo endpoint
  - PDF disponível em:

```http
GET /api/v1/reports/jobs/{job_id}/pdf
```

## Observações operacionais

- O worker está isolado em container próprio, sem acoplamento de processo com a API.
- O endpoint original foi preservado.
- O armazenamento de PDF no banco foi mantido conforme solicitado.

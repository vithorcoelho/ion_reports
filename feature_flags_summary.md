# Feature Flags

## Como Usar

**1. Editar o arquivo `.env`:**

```env
# Para usar STRATEGY PATTERN (novo padrão)
FEATURE_USE_STRATEGY_PATTERN=true

# Para usar PLUGINS (padrão atual)
FEATURE_USE_STRATEGY_PATTERN=false
```

**2. Aplicar as mudanças:**

```bash
# Parar e subir novamente
docker-compose down
docker-compose up

```

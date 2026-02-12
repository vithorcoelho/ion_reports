# MLflow Trace Report Generator

Este script Python gera relatórios detalhados e resumidos a partir de traces do MLflow, sendo especialmente útil para análise de execuções de modelos de ML e geração de relatórios

## Funcionalidades

O script gera dois tipos de relatórios:

1. **Debug Report** (`trace_report_debug.md`) - Relatório técnico completo com todos os spans e detalhes da execução
2. **Simple Report** (`simple_report.md`) - Relatório final formatado baseado nos dados estruturados encontrados

## Como Usar

### Sintaxe Básica

```bash
python script.py [--run-id RUN_ID] [--trace-id TRACE_ID] [--output-dir OUTPUT_DIR]
```

### Parâmetros

- `--run-id`: ID da execução do MLflow para buscar o trace
- `--trace-id`: ID específico do trace (opcional)
- `--output-dir`: Diretório local para salvar os relatórios (opcional)

### Exemplos

```bash
# Usar o run mais recente
python script.py --output-dir ./reports

# Usar um run específico
python script.py --run-id abc123 --output-dir ./reports

# Usar um trace específico
python script.py --trace-id xyz789 --output-dir ./reports
```

## Tipos de Relatórios Suportados

O script identifica automaticamente o tipo de relatório baseado na estrutura dos dados:

### IonNutri Report
Para dados que contêm `recommendations`:
- Resumo executivo
- Achados clínicos
- Recomendações nutricionais (energéticos, construtores, reguladores, gorduras)
- Suplementação
- Estilo de vida

### Vida Nova Report
Para dados que contêm `diet_suggestions`:
- Resumo executivo
- Achados
- Sugestões dietéticas
- Suplementação sugerida
- Dicas de treinamento

### Relatório Genérico
Para outros tipos de dados estruturados

## Funcionamento Interno

### 1. Busca do Trace
- Se não for fornecido um `run-id`, busca a execução mais recente
- Tenta encontrar o trace até 5 vezes com intervalos de 3 segundos
- Suporta busca por `trace-id` específico

### 2. Geração do Debug Report
- Extrai informações básicas do trace (ID, estado, tempo de execução)
- Lista todos os spans com detalhes técnicos
- Inclui dados de uso de tokens quando disponível
- Formata saídas JSON de forma legível

### 3. Geração do Simple Report
- Procura spans específicos que contêm relatórios estruturados:
  - `build_ionnutri_report`
  - `build_vidanova_report`
  - `build_structured_report`
- Extrai dados estruturados desses spans
- Gera relatório final em Markdown formatado

### 4. Salvamento
- Salva ambos os relatórios como artefatos do MLflow
- Opcionalmente salva cópias locais no diretório especificado


## Configuração

O script utiliza configurações do módulo `app.core.config.settings`:
- `MLFLOW_TRACKING_URI`: URI do servidor MLflow
- `MLFLOW_EXPERIMENT_NAME`: Nome do experimento MLflow

## Tratamento de Erros

- Retry automático para busca de traces (até 5 tentativas)
- Tratamento robusto de erros de parsing JSON
- Logs detalhados de erro com stack trace
- Continua execução mesmo se um tipo de relatório falhar

## Estrutura de Saída

### Arquivos Gerados
- `trace_report_debug.md`: Relatório técnico completo
- `simple_report.md`: Relatório final formatado

### Localização
- **MLflow**: Artefatos salvos na execução correspondente
- **Local**: Diretório especificado em `--output-dir` (opcional)

## Exemplo de Uso Típico

```bash
# Gerar relatórios da execução mais recente e salvar localmente
python generate_reports.py --output-dir ./output

# Verificar os arquivos gerados
ls ./output/
# trace_report_debug.md
# simple_report.md
```

## Notas Importantes

- O script aguarda até 15 segundos (5 tentativas × 3 segundos) por traces que ainda não estão disponíveis
- Dados JSON são formatados com indentação para melhor legibilidade
- Suporta caracteres não-ASCII na saída
- Cria automaticamente diretórios de saída se não existirem

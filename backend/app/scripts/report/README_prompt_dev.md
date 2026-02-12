# Prompt Development CLI (prompt_dev.py)

Ferramenta de linha de comando para registrar e avaliar prompts no MLflow. Suporta dois tipos de exame: **ionnutri** e **vidanova** e oferece comandos para registrar, listar, promover e avaliar estratégias de prompt.

## Tipos de Exame Suportados

- **ionnutri**
- **vidanova**

## Estratégias Disponíveis

- **multistage**: Prompts modulares por seção
- **onestage**: Prompts completos em uma única etapa

## Estrutura de Arquivos

```
app/scripts/report/prompts/
├── ionnutri/
│   ├── multistage/
│   │   ├── findings.txt
│   │   ├── deficiencies.txt
│   │   ├── nutrition.txt
│   │   ├── supplements.txt
│   │   ├── lifestyle.txt
│   │   ├── exams.txt
│   │   ├── summary.txt
│   │   └── markdown.txt
│   └── onestage/
│       ├── complete.txt
│       └── markdown.txt
└── vidanova/
    ├── multistage/
    │   ├── findings.txt
    │   ├── diet.txt
    │   ├── supplements.txt
    │   ├── training.txt
    │   ├── summary.txt
    │   └── markdown.txt
    └── onestage/
        ├── complete.txt
        └── markdown.txt
```

## Como Usar

### Comandos Principais

#### 1. **Registrar um Prompt**
O comando disponível é `register` e os parâmetros são: `exam_type` (ex.: ionnutri|vidanova), `section` (ex.: findings) e a opção `--version` (opcional, default 1.0.0).

Exemplos:
```bash
# Posicional
python app/scripts/report/prompt_dev.py register ionnutri findings

# Com opção de versão
python app/scripts/report/prompt_dev.py register ionnutri findings --version 1.0.0
```

#### 2. **Registrar em lote**
O script fornece o comando `register` para registrar prompts individuais a partir do repositório de templates. Para registrar todos os arquivos de uma vez, empacote-os e invoque `register` em loop ou crie um script auxiliar.

#### 3. **Ver Status dos Prompts**
O comando disponível é `status`.

```bash
# Ver prompts de um tipo
python app/scripts/report/prompt_dev.py status ionnutri

# Ver todos os prompts (sem parâmetro)
python app/scripts/report/prompt_dev.py status
```

#### 4. **Avaliar Prompts**
O comando `evaluate` permite comparar uma ou todas as estratégias configuradas usando dados de teste.

Principais opções (implementadas no script):
- `--exam-type` (default: ionnutri)
- `--all-strategies` (flag)
- `--strategy-type` (avaliar uma estratégia específica)
- `--test-data` (caminho para JSON de testes)
- `--output` (arquivo para salvar resultados JSON)

Exemplos:
```bash
# Avaliar uma estratégia específica
python app/scripts/report/prompt_dev.py evaluate --exam-type ionnutri --strategy-type multistage

# Avaliar todas as estratégias do exam_type
python app/scripts/report/prompt_dev.py evaluate --exam-type ionnutri --all-strategies

# Avaliar com arquivo de teste e salvar resultado
python app/scripts/report/prompt_dev.py evaluate --test-data tests/sample_prompt_tests.json --output results.json
```

### Formato do arquivo de teste (`--test-data`)

O avaliador espera um arquivo JSON contendo um array de casos de teste. Cada caso deve ter pelo menos duas chaves:
- `inputs`: objeto com os dados que serão fornecidos à estratégia (por exemplo `exam_data` e `anamnesis`)
- `targets`: string com o texto alvo (a referência esperada usada pelo avaliador)

1) Exemplo mínimo (arquivo: `tests/minimal_test_data.json`):

```json
[
  {
    "inputs": {
      "exam_data": { "patient_id": "p1", "exam_date": "2025-09-23", "metabolites": [] },
      "anamnesis": { "patient_id": "p1", "objective": "Improve energy" }
    },
    "targets": "Findings: ... Recommendations: ..."
  }
]
```

2) Exemplo esperado (formato usado pelos arquivos em `app/scripts/load_data/data_to_pass_api/`)

Os arquivos sob `app/scripts/load_data/data_to_pass_api/` normalmente contêm as chaves `exam_data` e `anamnesis`. Para usar esses arquivos diretamente como `--test-data` você deve empacotá-los num array e fornecer também o campo `targets` (por exemplo, o texto de referência que pode estar em `app/scripts/load_data/traces/` ou em outro arquivo de referência).

Exemplo (arquivo: `tests/ionnutri_from_data_to_pass_api.json`):

```json
[
  {
    "inputs": {
      "exam_data": {
        "patient_id": "ASH042514",
        "exam_date": "2025-07-02T00:00:00Z",
        "metabolites": [
          { "name": "Acetilcarnitina", "value": 0.495 },
          { "name": "Alanina", "value": 42.4 },
          { "name": "Lactato", "value": 696.0 }
        ]
      },
      "anamnesis": {
        "anamnesis_type": "ionnutri",
        "patient_id": "ASH042514",
        "objective": "Melhoria de performance no esporte",
        "personal_data": { "age": 28, "gender": "não informado" }
      }
    },
    "targets": "Findings: ...\nRecommendations: ..."
  }
]
```

Comando de execução usando um arquivo real (exemplo PowerShell):

```powershell
python app/scripts/report/prompt_dev.py evaluate --exam-type ionnutri --test-data tests/ionnutri_from_data_to_pass_api.json --output results.json
```

Observações:
- Muitos arquivos em `data_to_pass_api` não incluem um campo `targets` — neste caso você precisa fornecer o texto de referência manualmente ou emparelhar o `exam_data` com um arquivo de referência (por exemplo, arquivos em `app/scripts/load_data/traces/` ou um resumo gerado manualmente).
- Certifique-se de que o número de `predictions` geradas pela estratégia corresponde ao número de casos em `--test-data` (o avaliador exige comprimentos iguais).

#### 5. **Promover Prompts**
O comando `promote` define um alias para uma versão de prompt. Parâmetros esperados: `exam_type`, `section`, `version` e `--alias` (opcional, default `production`).

```bash
# Promover uma seção específica (ex.: 'findings')
python app/scripts/report/prompt_dev.py promote ionnutri findings 1 --alias production
```

## Carregar Prompts no MLflow

Use o comando `register` para registrar prompts individuais no MLflow a partir dos templates presentes em `app/scripts/report/prompts/`.

## Verificar no MLflow UI

Após o registro, acesse a UI do MLflow (por exemplo: `http://localhost:5000`) para visualizar os prompts registrados e suas versões/aliases.

## Workflow de Desenvolvimento

### Fluxo Completo de Desenvolvimento de Prompts
```bash
# 1. Registrar prompts (por seção)
python app/scripts/report/prompt_dev.py register ionnutri findings

# 2. Avaliar performance (todas as estratégias)
python app/scripts/report/prompt_dev.py evaluate --exam-type ionnutri --all-strategies

# 3. Promover melhor versão para produção
python app/scripts/report/prompt_dev.py promote ionnutri findings 1 --alias production
```

### Avaliação de Status

O comando `evaluate` executa as estratégias usando dados de teste e o `MLflowPromptEvaluator` para calcular métricas GenAI. Entre os outputs esperados estão métricas de completude médica, taxa de erro e tamanho médio de predição (quando aplicáveis).

## Gestão de Aliases

- **`@latest`**: Versão mais recente registrada
- **`@staging`**: Versão em teste
- **`@production`**: Versão em produção

## Comandos Rápidos

```bash
# Ver ajuda
python app/scripts/report/prompt_dev.py --help

# Ver status de todos os prompts
python app/scripts/report/prompt_dev.py status

# Registrar um prompt específico (posicional)
python app/scripts/report/prompt_dev.py register ionnutri findings

# Avaliar todas as estratégias
python app/scripts/report/prompt_dev.py evaluate --exam-type ionnutri --all-strategies

# Promover para produção
python app/scripts/report/prompt_dev.py promote ionnutri findings 1 --alias production
```

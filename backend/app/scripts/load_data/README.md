# Processamento de Dados Metabolômicos

Este projeto processa dados de metabolômica clínica e constrói um grafo de conhecimento no Neo4j para análise de metabólitos, vias metabólicas e intervenções.

## Visão Geral

O sistema é composto por scripts que:
- Processam dados de exames de pacientes
- Constroem uma ontologia médica estruturada
- Geram intervalos de referência clínicos
- Carregam tudo em um banco de dados Neo4j

## Estrutura dos Dados

### Arquivos de Entrada (pasta `data/`)
- `Anexo 06B.xlsx`: Dados de exames dos pacientes com concentrações de metabólitos
- `Anexo 4.xlsx`: Ontologia médica protegida por senha (contém metabólitos, vias, sintomas, intervenções)
- `ionnutri_metabolite_ranges.csv`: Intervalos de referência clínicos (scores 1-5)

### Arquivos de Saída (pasta `processed_data/`)
- `patient_score_vidanova.json`: Dados estruturados dos exames Vidanova
- `patient_scores_ionnutri.json`: Dados estruturados dos exames Ionnutri
- `ontology.json`: Ontologia médica processada
- `ontology_with_ranges.json`: Intervalos de referência estruturados

### Dados para API (pasta `data_to_pass_api/`)
- **Arquivos JSON individuais**: Cada arquivo representa um paciente específico
- **Estrutura**: Contém metabólitos e anamnese do paciente
- **Formato**: JSON estruturado com dados clínicos para processamento via API
- **Uso**: Estes arquivos são utilizados para alimentar a API e gerar relatórios personalizados

**Exemplo de estrutura:**
```json
{
  "patient_id": "ASH042514",
  "metabolites": {
    "Glucose": {"value": 85, "unit": "mg/dL", "score": 3},
    "Iron": {"value": 45, "unit": "μg/dL", "score": 2}
  },
  "anamnesis": {
    "symptoms": ["fatigue", "weakness"],
    "medical_history": ["anemia"],
    "current_medications": ["iron_supplements"]
  }
}
```

## Scripts Principais

### 1. `preprocess_tnm.py`
Processa dados de exames de pacientes.

```bash
python preprocess_tnm.py
```

**O que faz:**
- Lê o arquivo Excel com dados dos pacientes
- Normaliza nomes dos metabólitos usando `constants.py`
- Extrai valores numéricos dos resultados
- Gera JSON estruturado com dados dos exames

### 2. `process_ontology.py`
Processa a ontologia médica protegida.

```bash
python process_ontology.py
```

**O que faz:**
- Descriptografa arquivo Excel protegido (senha: "241224")
- Extrai metabólitos, vias metabólicas, sintomas e intervenções
- Cria relacionamentos entre entidades
- Gera estrutura JSON hierárquica

### 3. `synthetic_ranges.py`
Processa intervalos de referência clínicos.

```bash
python synthetic_ranges.py
```

**O que faz:**
- Lê arquivo CSV com intervalos clínicos
- Mapeia scores (1=déficit severo → 5=excesso severo)
- Normaliza nomes dos metabólitos
- Cria nós de referência para o grafo

### 4. `main.py`
Carrega dados processados no Neo4j.

```bash
python main.py
```

**O que faz:**
- Conecta ao banco Neo4j
- Cria constraints no banco
- Carrega arquivos JSON processados
- Constrói o grafo de conhecimento

## Dependências

```bash
pip install pandas openpyxl msoffcrypto-tool python-slugify neo4j
```

### Principais bibliotecas:
- `pandas`: Manipulação de dados
- `openpyxl`: Leitura de arquivos Excel
- `msoffcrypto-tool`: Descriptografia de arquivos protegidos
- `python-slugify`: Geração de IDs limpos
- `neo4j`: Conexão com banco de dados

### 5. Executar processamento
```bash
# Processar dados dos pacientes
python preprocess_tnm.py

# Processar ontologia médica
python process_ontology.py

# Carregar dados no Neo4j
python main.py
```

## Fluxo de Dados

```
1. Dados Brutos (data/) → 2. Processamento (scripts/) → 3. Dados Processados (processed_data/) → 4. Neo4j
                                                                    ↓
                                                            5. Dados para API (data_to_pass_api/)
```

## Estrutura de Diretórios

```
load_data/
├── data/                    # Dados brutos de entrada
├── processed_data/          # Dados processados para Neo4j
├── data_to_pass_api/        # Dados estruturados para API
├── processing/              # Scripts de processamento
├── utils/                   # Tratamento de dados
├── main.py                  # Script principal de carregamento
└── README.md                # Este arquivo
```

## Estrutura do Banco Neo4j

### Nós principais:
- **Metabolite**: Metabólitos com definições e fontes alimentares
- **MetabolicPathway**: Vias metabólicas
- **Manifestation**: Sintomas clínicos (níveis baixos/altos)
- **Intervention**: Intervenções terapêuticas
- **Food**: Condutas alimentares
- **Supplement**: Condutas de suplementação
- **ReferenceRange**: Intervalos de referência clínicos

### Relacionamentos:
- Metabolite → MetabolicPathway
- Metabolite → Evidence
- Metabolite → Manifestation
- Manifestation → Intervention
- Intervention → Food/Supplement
- Metabolite → ReferenceRange

## Utilitários

### `constants.py`
Mapeamento de nomes de metabólitos para padronização entre diferentes fontes de dados.

### `file_handler.py`
Funções para leitura de arquivos (CSV/Excel) e salvamento em JSON.

### `text_processing.py`
Funções para limpeza de texto, extração de valores numéricos e geração de slugs.


## Observações

- O arquivo `Anexo 4.xlsx` está protegido com senha "241224"
- Certifique-se de que o Neo4j está rodando antes de executar `main.py`
- Os scripts devem ser executados na ordem indicada
- Verifique se todos os arquivos de entrada estão na pasta `data/`

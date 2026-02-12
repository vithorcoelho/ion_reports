# Arquitetura do Sistema

## 1. Visão Geral

> "Um sistema especializado que transforma dados nutrimetabólicos normalizados em relatórios personalizados utilizando conhecimento estruturado e modelos de linguagem."

O sistema foi projetado com foco na simplicidade e eficiência, eliminando componentes desnecessários e trabalhando diretamente com dados já normalizados.

```mermaid
%%{init: {'theme': 'default'}}%%
graph TD
    subgraph "Entrada de Dados"
        Input[JSON de Exame TNM<br>e Anamnese do Paciente]
    end
    subgraph "app.api"
        APIEndpoints[API]
    end
    subgraph "app.services"
        TNM[TNMService]
        LLM[LLMService]
    end
    subgraph "app.db"
        KGQuery[Neo4jKnowledgeQuery]
        Neo4j[Neo4jClient]
        KG[(Base de Conhecimento<br>Neo4j)]
    end
    Input --> APIEndpoints
    APIEndpoints --> TNM
    TNM --> KGQuery
    KGQuery --> Neo4j
    Neo4j <--> KG
    TNM --> LLM
    TNM --> APIEndpoints
    classDef input fill:#e6f0ff,stroke:#3366cc,stroke-width:2px
    classDef services fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef knowledge fill:#ffe6cc,stroke:#ff9900,stroke-width:2px
    classDef api fill:#e6ffe6,stroke:#33cc33,stroke-width:2px
    classDef database fill:#e6ccff,stroke:#9933cc,stroke-width:2px
    class Input input
    class TNM,LLM,KGQuery services
    class APIEndpoints api
    class Neo4j database
    class KG knowledge
```

## 2. Componentes do Sistema

### 2.1 Diagramas de Classes por Módulo

#### a) app.schemas

```mermaid
classDiagram
    class TNMExamData {
        +str patient_id
        +datetime exam_date
        +List[Metabolite] metabolites
    }
    class Metabolite {
        +str name
        +float value
        +str unit
    }
    class PatientAnamnesis {
        +str patient_id
        +str objective
        +PersonalData personal_data
        +ContextFactors context_factors
    }
    class PersonalData {
        +int age
        +str gender
        +float weight
        +float height
        +float bmi
    }
    class ContextFactors {
        +List[str] medical_history
        +List[str] intolerances
        +PhysicalActivity physical_activity
        +Sleep sleep
        +AlcoholConsumption alcohol_consumption
        +List[Medication] medications
    }
    class TNMReport {
        +str report_id
        +str patient_id
        +str anamnesis_id
        +str exam_id
        +str version
        +datetime timestamp
        +str summary
        +FindingsSection findings
        +RecommendationsSection recommendations
        +List[DeficiencyItem] deficiencies
        +str general_guidelines
        +List[ExamItem] additional_exams
        +str closing_note
    }
    class TNMResult {
        +List[MetaboliteInfo] metabolite_info
        +List[Manifestation] manifestations
        +List[Intervention] recommended_interventions
        +List[RecommendedFood] foods
        +List[RecommendedSupplement] supplements
        +List[PathwayImpact] pathway_impacts
        +List[ScientificEvidence] scientific_evidence
        +List[Contraindication] contraindications
        +str error
        +from_kg_data(kg_data) TNMResult
        +create_error_result(error_message) TNMResult
    }
    class MetaboliteStatusEnum {
        <<enumeration>>
        DEFICT_SEVERO = 1
        DEFICIT_MODERADO = 2
        NORMAL = 3
        EXCESSO_MODERADO = 4
        EXCESSO_SEVERO = 5
    }

    TNMExamData "1" *-- "many" Metabolite : contém
    PatientAnamnesis "1" *-- "1" PersonalData : contém
    PatientAnamnesis "1" *-- "1" ContextFactors : contém
    TNMReport "1" *-- "1" FindingsSection : contém
    TNMReport "1" *-- "many" DeficiencyItem : contém
    TNMReport "1" *-- "1" RecommendationsSection : contém
    TNMReport "1" *-- "many" ExamItem : contém
```

#### b) app.services

```mermaid
classDiagram
    class TNMService {
        -LLMService llm_service
        -Neo4jKnowledgeQuery knowledge_query
        +async generate_report(TNMExamData, PatientAnamnesis) → TNMReport
        -async _generate_structured_report(exam_data, anamnesis, kg_data) → TNMReport
        -_generate_section_contents(exam_data, anamnesis, kg_data) → Dict
        -_build_findings_section(metabolite_info, findings_data) → FindingsSection
        -_build_recommendations_section(section_contents) → RecommendationsSection
        -_normalize_status(status) → MetaboliteStatusEnum
        -_create_metabolite_status(status_enum) → dict
    }
    class LLMService {
        +str model_name
        +str model_id
        +str api_key
        +OpenAI client
        +call_llm_api(prompt, temperature, max_tokens) → Dict
        +generate_prompt(section, exam_data, anamnesis, kg_data) → str
        -_parse_response(response) → Dict
    }
    TNMService --> LLMService : usa
    TNMService --> app.db.Neo4jKnowledgeQuery : usa
```

#### c) app.db

```mermaid
classDiagram
    class Neo4jClient {
        +AsyncGraphDatabase driver
        +async __enter__() → Neo4jClient
        +async __exit__(exc_type, exc_value, traceback)
        +async close()
        +async verify_connection()
        +async execute_query(query, **params) → List[Dict]
        +session() → AsyncSession
    }
    class Neo4jKnowledgeQuery {
        +Neo4jClient client
        +async execute_unified_query(TNMExamData, PatientAnamnesis) → TNMResult
    }
    class KnowledgeGraphBuilder {
        +Neo4jClient client
        +Dict _type_mapping
        +List _relationship_mappings
        +async load_ontology(file_path) → Dict
        +async create_nodes(json_content, entity_type, node_label) → int
        +async create_relationships(json_content, source_entity, target_entity, relationship_type, relationship_key) → int
        +async create_constraints()
        -_get_type_mapping() → Dict
        -_get_relationship_mappings() → List
    }
    class IDatabaseClient {
        <<interface>>
        +async verify_connection()
        +async execute_query(query, **params)
        +async close()
    }
    class IUnifiedQuery {
        <<interface>>
        +async execute_unified_query(TNMExamData, PatientAnamnesis) → TNMResult
    }
    class IknowledgeGraphBuilder {
        <<interface>>
        +async load_ontology(ontology_file_path) → bool
        +async create_relationships(json_content, source_entity, target_entity, relationship_type, relationship_key) → int
        +async create_nodes(json_content, entity_type, node_label) → int
    }

    Neo4jClient ..|> IDatabaseClient : implementa
    Neo4jKnowledgeQuery ..|> IUnifiedQuery : implementa
    KnowledgeGraphBuilder ..|> IknowledgeGraphBuilder : implementa
    Neo4jKnowledgeQuery --> Neo4jClient : usa
    KnowledgeGraphBuilder --> Neo4jClient : usa
```

#### d) app.api

```mermaid
classDiagram
    class FastAPI {
        +include_router(api_router)
        +get("/health")
    }
    class APIRouter {
        +post("/reports/") → TNMReport
    }
    class Dependencies {
        +get_neo4j_client() → Neo4jClient
        +get_knowledge_query() → Neo4jKnowledgeQuery
        +get_llm_service() → LLMService
        +get_tnm_service() → TNMService
    }

    FastAPI --> APIRouter : inclui
    APIRouter --> Dependencies : usa
    Dependencies --> app.services.TNMService : cria
    Dependencies --> app.db.Neo4jClient : cria
```

### 2.2 Diagrama de Classes de Alto Nível (com Namespaces e Relações)

```mermaid
classDiagram
    %% Namespaces
    namespace app.schemas {
        class TNMExamData
        class PatientAnamnesis
        class TNMReport
        class TNMResult
        class MetaboliteStatusEnum
    }
    namespace app.services {
        class TNMService
        class LLMService
    }
    namespace app.db {
        class Neo4jKnowledgeQuery
        class Neo4jClient
        class KnowledgeGraphBuilder
    }
    namespace app.api {
        class APIRouter
        class Dependencies
    }
    namespace app.core {
        class Settings
        class Logger
    }

    %% Relações principais
    app.services.TNMService --> app.schemas.TNMExamData : entrada
    app.services.TNMService --> app.schemas.PatientAnamnesis : entrada
    app.services.TNMService --> app.schemas.TNMReport : saída
    app.services.TNMService --> app.services.LLMService : usa
    app.services.TNMService --> app.db.Neo4jKnowledgeQuery : usa
    app.db.Neo4jKnowledgeQuery --> app.schemas.TNMResult : retorna
    app.db.Neo4jKnowledgeQuery --> app.db.Neo4jClient : usa
    app.db.KnowledgeGraphBuilder --> app.db.Neo4jClient : usa
    app.api.APIRouter --> app.services.TNMService : usa
    app.api.Dependencies --> app.services.TNMService : cria
    app.api.Dependencies --> app.db.Neo4jClient : cria
    app.services.LLMService --> app.core.Settings : usa
    app.db.Neo4jClient --> app.core.Settings : usa
```

### 2.3 Estrutura de Diretórios

O sistema segue as melhores práticas para FastAPI, com os modelos em `schemas` e serviços em `services`, organizados em namespaces/pacotes:

```
ion-nutri/
│
├── app/                     # Código fonte da aplicação
│   ├── api/                 # Endpoints da API (namespace: app.api)
│   │   ├── __init__.py
│   │   ├── router.py        # Configuração de rotas
│   │   ├── dependencies.py  # Injeção de dependências
│   │   └── endpoints/       # Implementação dos endpoints
│   │       ├── __init__.py
│   │       └── reports.py   # Endpoint principal de relatórios TNM
│   │
│   ├── core/                # Núcleo da aplicação (namespace: app.core)
│   │   ├── __init__.py
│   │   ├── config.py        # Configurações (variáveis de ambiente)
│   │   └── logging.py       # Configuração de logs
│   │
│   ├── db/                  # Acesso ao banco de dados e queries (namespace: app.db)
│   │   ├── __init__.py
│   │   ├── base.py          # Interfaces abstratas
│   │   ├── neo4j_client.py  # Cliente Neo4j
│   │   ├── knowledge_graph_builder.py # Builder do grafo
│   │   └── unified_query.py # Query unificada do grafo
│   │
│   ├── schemas/             # Modelos de dados (Pydantic) (namespace: app.schemas)
│   │   ├── __init__.py
│   │   ├── exam.py          # Modelo do exame TNM
│   │   ├── patient_anamnesis.py # Modelo da anamnese
│   │   ├── report.py        # Modelo do relatório TNM
│   │   ├── status.py        # Enum de status
│   │   └── tnm_result.py    # Modelo do resultado do grafo
│   │
│   ├── services/            # Serviços de negócio (namespace: app.services)
│   │   ├── __init__.py
│   │   ├── tnm_service.py   # Serviço principal TNM
│   │   └── llm_service.py   # Cliente da LLM
│   │
│   ├── utils/               # Utilitários (namespace: app.utils)
│   │   └── utils.py
│   │
│   └── main.py              # Ponto de entrada da aplicação
│
├── tests/                   # Testes automatizados
│   ├── __init__.py
│   ├── conftest.py
│   ├── api/
│   └── services/
│
├── docs/                    # Documentação
│   ├── arquitetura.md
│   ├── development.md
│   └── templates/
│       └── tnm.md
│
├── Dockerfile
├── docker-compose.yml
├── README.md
└── ...
```

## 3. Práticas e Princípios de Desenvolvimento

Para informações detalhadas sobre as práticas e princípios de desenvolvimento utilizados neste projeto, consulte o arquivo [development.md](development.md).

## 4. CHANGELOG

### Consolidação e Materialização da Arquitetura (2025-07-01)

1. **Evolução do Modelo de Dados**:
    - Introdução do `TNMResult` como ponte entre knowledge graph e relatórios
    - Formalização do sistema de classificação de metabólitos com `MetaboliteStatusEnum`
    - Padronização de interfaces para diferentes tipos de dados estruturados (manifestações, intervenções, evidências)

2. **Maturação da Camada de Serviços**:
    - Consolidação do `TNMService` como orquestrador central do fluxo de geração de relatórios
    - Estabelecimento de padrões para integração com LLMs através do `LLMService`
    - Implementação de sistema de seções modulares para relatórios TNM

3. **Aprimoramento da Arquitetura de Dados**:
    - Introdução de sistema de logging estruturado em Markdown para auditoria
    - Padronização de serialização de dados temporais (timestamps, datas)
    - Estabelecimento de configurações centralizadas para classificação de status

4. **Refinamento da Documentação Arquitural**:
    - Reorganização dos diagramas para refletir namespaces reais da implementação
    - Documentação de interfaces abstratas para garantir extensibilidade
    - Detalhamento das relações entre componentes conforme implementação atual

5. **Impactos na Arquitetura**:
    - **Melhoria na Coesão**: Centralização da lógica de geração de relatórios no `TNMService`
    - **Aumento da Flexibilidade**: Sistema modular de seções permite extensões futuras
    - **Padronização de Dados**: Modelos estruturados facilitam integração e manutenção
    - **Auditabilidade**: Sistema de logging permite rastreamento de decisões e resultados

### Mudanças na Arquitetura (2025-05-21)

1. **Consolidação de Serviços**:
    - Unificação do `Neo4jDatabase`, `OntologyBuilder` e `Neo4jKnowledgeGraph` em um único `Neo4jClient`
    - Movimentação da geração de prompts e formatação de relatórios para dentro do `TNMService`
    - Simplificação da interface com LLM para um único serviço `LLMService`

2. **Redução de Camadas de Abstração**:
    - Remoção de interfaces que possuíam apenas uma implementação
    - Simplificação da hierarquia de classes
    - Criação de um fluxo mais direto entre componentes

3. **Simplificação da Estrutura de Diretórios**:
    - Redução do número de arquivos de serviços
    - Organização mais direta do projeto

4. **Motivações para as Mudanças**:
    - Redução da complexidade acidental do sistema
    - Aceleração do desenvolvimento inicial
    - Melhoria da manutenibilidade e compreensão do código
    - Facilitação do onboarding de novos desenvolvedores

5. **Princípios Preservados**:
    - Todos os princípios de Clean Architecture foram mantidos
    - A aderência aos princípios SOLID foi preservada
    - A testabilidade do sistema não foi comprometida

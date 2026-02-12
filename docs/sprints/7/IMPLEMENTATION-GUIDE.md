# Implementation Guide - 3-Week Migration Plan

**Practical roadmap for 1 junior developer + 2 trainees migrating from plugins to Strategy Pattern with MLflow.**

## 3-Week Timeline

### Week 1: Foundation
- **Day 1-3**: Setup MLflow registry/evaluation (Junior)
- **Day 4-5**: Base classes (Matheus) + LLM/KG services (William) - parallel after Task 1

### Week 2: Services Implementation
- **Day 1-3**: Prompt registry (Matheus) + Prompt evaluation (William) - after completing Tasks 2&5
- **Day 4-5**: Strategy implementations (Junior)

### Week 3: Integration & Cleanup
- **Day 1-3**: Integration and coordination (Junior)
- **Day 4**: End-to-end validation
- **Day 5**: Legacy cleanup

## Tasks Distribution

**Task Dependencies:**
- Task 1 → Task 2 & 5 (parallel)
- Task 2 → Task 3
- Task 5 → Task 4
- Tasks 2,3,4,5 → Task 6 → Task 7

### Task 1: MLflow Setup (Junior Developer)
**Goal**: Extend existing MLflow setup for prompt registry/evaluation

**Deliverables**:
```bash
# CREATE: app/scripts/report/prompts/ionnutri/{multistage,onestage}/
# CREATE: app/scripts/report/prompts/vidanova/{multistage,onestage}/
# CREATE: app/scripts/report/prompt_dev.py - Unified development CLI
# VALIDATE: MLflow UI at localhost:5000 with prompt models
```


**Template Structure**:
```
app/scripts/report/prompts/
├── ionnutri/
│   ├── multistage/
│   │   ├── findings.txt
│   │   ├── interventions.txt
│   │   ├── monitoring.txt
│   │   └── markdown.txt
│   └── onestage/
│       ├── complete.txt
│       └── markdown.txt
└── vidanova/
    ├── multistage/
    │   ├── performance.txt
    │   ├── recovery.txt
    │   └── markdown.txt
    └── onestage/
        ├── complete.txt
        └── markdown.txt
```

**Acceptance**:
- [ ] MLflow registry operational with initial templates
- [ ] `prompt_dev.py` loads/registers/evaluates prompts
- [ ] Environment variables configured

### Task 2: Base Architecture (Trainee Matheus)
**Goal**: Create exam configs and base strategy classes

**Deliverables**:
```python
# CREATE: app/domain/exam_configs/base_config.py
# CREATE: app/domain/exam_configs/ionnutri_config.py  # ← metabolite_constants.py
# CREATE: app/domain/exam_configs/vidanova_config.py   # ← vidanova_constants.py
# CREATE: app/services/report/base.py
# CREATE: app/services/report/strategy_factory.py
```

**Migration**:
```python
# app/domain/exam_configs/ionnutri_config.py
class IonNutriConfig(BaseExamConfig):
    # Move entire metabolite_constants.py content here
    METABOLITE_STATUS_CONFIG = {...}  # Exact copy
    STATUS_MAPPING = {...}            # Exact copy
    REQUIRED_SECTIONS = [...] # 12 sections
    SECTION_SCHEMAS = {...}   # 12 Pydantic schemas

    def get_exam_type(self) -> str:
        return "ionnutri"

# app/domain/exam_configs/vidanova_config.py
class VidaNovaConfig(BaseExamConfig):
    # Move entire vidanova_constants.py content here
    SECTION_SCHEMAS = {...}   # 5 Pydantic schemas

    def get_exam_type(self) -> str:
        return "vidanova"
```

**Acceptance**:
- [ ] BaseExamConfig + concrete implementations
- [ ] Constants migrated to appropriate configs
- [ ] StrategyFactory creates combinations
- [ ] Unit tests with >85% coverage

### Task 3: Prompt Registry (Trainee Matheus)
**Goal**: MLflow-backed prompt registry (after completing Task 2)

**Deliverables**:
```python
# CREATE: app/services/llm/prompt_registry.py
```

**Key Implementation**:
```python
class MLflowPromptRegistry(BasePromptRegistry):
    def load_prompt_by_uri(self, prompt_uri: str) -> str:
        # Format: prompts:/ionnutri_multistage_findings@production
        path, alias = prompt_uri[9:].split("@")
        model_version = self.client.get_model_version_by_alias(
            name=f"prompt_{path}", alias=alias
        )
        return self._download_prompt_artifact(model_version.run_id)
```

**Acceptance**:
- [ ] URI-based prompt loading functional
- [ ] MLflow artifact management operational
- [ ] Prompt versioning and aliases working
- [ ] Prompt registration methods
- [ ] Metadata tracking (author, timestamps, version comments, file info)
- [ ] Integration with CLI register command functionality

### Task 4: Prompt Evaluation (Trainee William)
**Goal**: MLflow-based prompt quality evaluation (after completing Task 5)

**Deliverables**:
```python
# CREATE: app/services/llm/prompt_evaluator.py
# UPDATE: app/scripts/report/prompt_dev.py - Add evaluation commands
```

**Key Implementation**:
```python
class MLflowPromptEvaluator(BasePromptEvaluator):
    def evaluate(self, strategy_results: dict, test_data: list) -> dict:
        scorers = [
            mlflow.metrics.genai.answer_correctness(),
            mlflow.metrics.genai.answer_similarity(),
            mlflow.metrics.genai.make_genai_metric(
                name="medical_completeness",
                definition="Medical recommendations completeness",
                grading_prompt="Rate completeness (1-5): diet, supplements, training"
            )
        ]

        results = {}
        for strategy_name, outputs in strategy_results.items():
            eval_result = mlflow.evaluate(
                data=test_data,
                predictions=outputs,
                evaluators=scorers
            )
            results[strategy_name] = {
                "score": eval_result.metrics["aggregate_score"],
                "metrics": eval_result.metrics
            }
        return results
```

**Acceptance**:
- [ ] MLflow GenAI evaluation working
- [ ] Quality metrics for prompt performance
- [ ] Integration with `prompt_dev.py` CLI

### Task 5: LLM & KG Services (Trainee William)
**Goal**: Unified LLM service and KG service bridge

**Deliverables**:
```python
# CREATE: app/services/llm/llm_service.py
# CREATE: app/services/kg/kg_service.py
```

**Key Implementation**:
```python
class OpenRouterLLMService(BaseLLMService):
    def call_llm(self, prompt: str, schema=None, **kwargs) -> str | BaseModel:
        # Unified method: schema=None → str, schema=Model → structured output
        if schema is None:
            return self._call_text_completion(prompt, **kwargs)
        else:
            return self._call_structured(prompt, schema, **kwargs)

class KnowledgeGraphService(BaseKnowledgeGraphService):
    def get_knowledge_data(self, exam_data, anamnesis) -> KGResult:
        # Bridge to existing db/unified_query.py
        # Format results for LLM consumption
```

**Acceptance**:
- [ ] LLM service unified interface working
- [ ] KG service bridges db/ cleanly
- [ ] Services integrate with existing db layer

### Task 6: Strategy Implementation (Junior Developer)
**Goal**: MultiStage and OneStage strategy implementations

**Deliverables**:
```python
# CREATE: app/services/report/multistage_strategy.py
# CREATE: app/services/report/onestage_strategy.py
```

**Key Logic**:
```python
class MultiStageReportStrategy(BaseReportStrategy):
    def execute(self, exam_data, anamnesis, kg_data) -> str:
        sections = self.exam_config.get_section_schemas()
        results, context = [], {...}

        for section, schema in sections.items():
            prompt_uri = f"{self.exam_config.get_exam_type()}_multistage_{section}@{self.alias}"
            prompt = self.prompt_registry.load_prompt_by_uri(prompt_uri)
            result = self.llm_service.call_llm(prompt.format(**context), schema)
            results.append(result)
            context[f"{section}_result"] = result

        return self._generate_markdown(context, results)

class OneStageReportStrategy(BaseReportStrategy):
    def execute(self, exam_data, anamnesis, kg_data) -> str:
        prompt_uri = f"{self.exam_config.get_exam_type()}_onestage_complete@{self.alias}"
        # Single comprehensive processing + direct markdown generation
```

**Acceptance**:
- [ ] Both strategies execute successfully
- [ ] Strategies are exam_type agnostic
- [ ] Uses services from Task 5

### Task 7: Integration (Junior Developer)
**Goal**: Update ReportCoordinator and end-to-end validation

**Deliverables**:
```python
# UPDATE: app/services/report_coordinator.py
# CREATE: strategy_config.yaml
# CREATE: tests/integration/test_full_migration.py
```

**ReportCoordinator Update**:
```python
class ReportCoordinator:
    def generate_report(self, exam_data: ExamData, anamnesis: PatientAnamnesis, exam_type: str) -> str:
        kg_data = self.kg_service.get_knowledge_data(exam_data, anamnesis)
        strategy_type = self.config['strategies'][exam_type]['type']

        strategy = self.strategy_factory.create_strategy(exam_type, strategy_type, {
            "llm": self.llm_service,
            "prompts": self.prompt_registry
        })

        return strategy.execute(exam_data, anamnesis, kg_data)
```

**Configuration**:
```yaml
# strategy_config.yaml
strategies:
  ionnutri:
    type: multistage
  vidanova:
    type: onestage
```

**Acceptance**:
- [ ] End-to-end report generation functional
- [ ] Performance maintained or improved
- [ ] All existing API contracts preserved

## Development Scripts

### prompt_dev.py CLI
```bash
# Status check
uv run python prompt_dev.py status --exam-type ionnutri

# Evaluate strategies
uv run python prompt_dev.py evaluate --exam-type ionnutri --all-strategies
# Output: multistage: 4.235, onestage: 3.981

# Register new prompt version
uv run python prompt_dev.py register --exam-type ionnutri --strategy-type multistage --section findings

# Promote to production
uv run python prompt_dev.py promote --exam-type ionnutri --strategy-type multistage --section findings --version 3

# Evaluate prompt quality
uv run python prompt_dev.py evaluate --exam-type ionnutri
```

### Evaluation Workflow
```python
# app/scripts/prompt_dev.py core logic
def evaluate_strategies(exam_type: str, all_strategies: bool = False):
    """Evaluate prompt performance across strategies."""
    strategies = get_strategies_for_eval(exam_type, all_strategies)
    test_data = load_evaluation_dataset(exam_type)

    strategy_results = {}
    for strategy_name, strategy in strategies:
        results = []
        for test_case in test_data:
            result = strategy.execute(test_case.exam_data, test_case.anamnesis, test_case.kg_data)
            results.append(result)
        strategy_results[strategy_name] = results

    evaluator = MLflowPromptEvaluator()
    metrics = evaluator.evaluate(strategy_results, test_data)

    return metrics  # {"multistage": {"score": 4.235}, "onestage": {"score": 3.981}}
```

### Testing Commands
```bash
# Unit tests
uv run python -m pytest tests/unit/services/ -v

# Integration tests
uv run python -m pytest tests/integration/ -v
```

## Legacy Cleanup

### File Migrations
```bash
# Constants → Exam Configs
app/constants/metabolite_constants.py  → app/domain/exam_configs/ionnutri_config.py
app/constants/vidanova_constants.py    → app/domain/exam_configs/vidanova_config.py

# Validator → Knowledge Graph Builder
app/validators/ontology_data_validator.py → integrated into app/db/knowledge_graph_builder.py
```

### Removals
```bash
# Complete removal
rm -rf app/plugins/
rm -rf app/constants/
rm -rf app/validators/
rm app/utils/markdown_generator.py  # Unused
rm app/utils/template_loader.py     # Unused
```

### Import Updates
```python
# OLD
from app.plugins.ionnutri_plugin import IonNutriPlugin
from app.constants.metabolite_constants import METABOLITE_STATUS_CONFIG

# NEW
from app.services.report.strategy_factory import StrategyFactory
# Configuration injected via exam_config, not imported
```

## Success Criteria

### Functional
- [ ] All existing API endpoints work unchanged
- [ ] Report generation performance maintained (<10% degradation)
- [ ] MLflow prompt registry operational with versioning
- [ ] Prompt quality evaluation functional with MLflow GenAI metrics

### Technical
- [ ] >90% test coverage on new components
- [ ] Type hints throughout (Python 3.12)
- [ ] Zero linting errors
- [ ] Complete plugin system removal

### Operational
- [ ] `prompt_dev.py` workflow documented and validated
- [ ] Team trained on new development process
- [ ] Rollback procedure tested
- [ ] Production deployment ready

## Risk Mitigation

### Technical Risks
- **MLflow integration failure**: Fallback to file-based prompts with same interface
- **Strategy performance issues**: Benchmark against current system continuously
- **Complex refactoring bugs**: Incremental migration with parallel testing

### Timeline Risks
- **Trainee learning curve**: Pair programming sessions, detailed code reviews
- **Scope creep**: Strict INVEST criteria, defer non-essential features
- **Integration complexity**: Daily standups, early integration testing

### Rollback Plan
1. Keep current plugin system until Week 3 validation
2. Feature flags for strategy vs plugin selection
3. Database/MLflow state restoration procedures
4. Immediate fallback to previous commit if critical issues

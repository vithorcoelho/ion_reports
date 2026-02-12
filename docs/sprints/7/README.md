# Sprint 7: N-Layer Architecture with Strategy Pattern

**Migration from plugins to Strategy Pattern with MLflow for 1 junior + 2 trainees team.**

## Documentation

### 🏗️ [Technical Overview](./TECHNICAL-OVERVIEW.md)
**Architecture, patterns, MLflow integration**
- N-Layer structure + Strategy Pattern
- exam_type vs strategy_type separation
- MLflow registry/evaluation integration
- Code structure and implementation details

### 🚀 [Implementation Guide](./IMPLEMENTATION-GUIDE.md)
**3-week roadmap, tasks, development scripts**
- Week-by-week timeline
- 7 practical tasks for small team
- prompt_dev.py CLI workflows
- Success criteria and validation

## Context & Motivation

### Current State → Target State
**From**: Plugin architecture with hardcoded prompts, tight coupling between exam types and processing
**To**: Strategy Pattern with MLflow-managed prompts, clean separation of business config vs processing logic

### Key Benefits
- **Combinatorial Flexibility**: Any `exam_type` (ionnutri/vidanova) can use any `strategy_type` (multistage/onestage)
- **Professional Prompt Management**: MLflow registry with versioning, aliases, rollback capability
- **Reduced Duplication**: Strategies reusable across all exam types
- **Better Testing**: Dependency injection enables mockable, testable components

## Team & Timeline

### **3-Week Sprint Structure**
**Week 1**: Foundation (MLflow setup → Base architecture & Services in parallel)
**Week 2**: Specialization (Prompt services → Strategy implementations)
**Week 3**: Integration (System coordination → Validation → Legacy cleanup)

### **Role Distribution**
- **Junior Developer**: MLflow setup, strategy implementations, final integration
- **Trainee Matheus**: Base classes, exam configs, prompt registry
- **Trainee William**: LLM/KG services, prompt evaluation

### **Task Dependencies**
Task 1 → Tasks 2&5 (parallel) → Tasks 3&4 → Task 6 → Task 7

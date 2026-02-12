# Issues de Refatoração - Distribuição de Tarefas

## 📋 Visão Geral

Este documento distribui as tarefas de refatoração identificadas no `verify.md` entre os desenvolvedores da equipe. Cada issue é priorizada e inclui estimativas de tempo.

## 🎯 **Resumo de Prioridades**

### 🔴 **ALTA PRIORIDADE** (Crítico - Fazer primeiro)
- **ISSUE #1** - Correção de Imports e Nomenclatura
- **ISSUE #4** - Tratamento de Erros e Configuração
- **ISSUE #9** - Refinamento dos Prompts do IonNutri

### 🟡 **MÉDIA PRIORIDADE** (Importante - Fazer em seguida)
- **ISSUE #2** - Documentação e Type Hints
- **ISSUE #3** - Estrutura e Formatação
- **ISSUE #5** - Schemas e Estrutura de Dados
- **ISSUE #8** - Limpeza de Arquivos e Código
- **ISSUE #10** - Conversão de Markdown para PDF

### 🟢 **BAIXA PRIORIDADE** (Desejável - Fazer por último)
- **ISSUE #7** - Padronização de Documentação para Inglês

---

## 🎯 **ISSUE #1 - Correção de Imports e Nomenclatura**
**🔴 PRIORIDADE: ALTA** - *Impacto direto na manutenibilidade e qualidade do código*

### Tarefas:
1. **Corrigir nomenclatura da classe `IknowledgeGraphBuilder`**
   - **Arquivo:** `app/db/base.py:38`
   - **Ação:** Renomear para `IKnowledgeGraphBuilder`
   - **Impacto:** Atualizar todas as referências

2. **Padronizar imports do MLflow**
   - **Arquivos:** `app/main.py:4`, `app/services/llm/llm_service.py:5`, `app/services/kg/kg_service.py:3`, `app/plugins/vidanova_plugin.py:10`, `app/plugins/ionnutri_plugin.py:11`
   - **Ação:** Centralizar imports em módulo de configuração
   - **Benefício:** Reduzir duplicação

3. **Reorganizar ordem de imports**
   - **Arquivo:** `app/main.py:2-16`
   - **Ação:** Seguir padrão PEP 8 (stdlib, third-party, local)

### Critérios de Aceitação:
- [ ] Classe renomeada e todas as referências atualizadas
- [ ] Imports do MLflow centralizados
- [ ] Ordem de imports padronizada
- [ ] Testes passando

---

## 🎯 **ISSUE #2 - Documentação e Type Hints**
**🟡 PRIORIDADE: MÉDIA** - *Melhora a qualidade do código e facilita manutenção*

### Tarefas:
1. **Completar docstrings de métodos abstratos**
   - **Arquivo:** `app/plugins/prompts/base.py:30-48`
   - **Ação:** Expandir docstrings com descrições detalhadas
   - **Padrão:** Formato Google

2. **Adicionar type hints completos**
   - **Arquivo:** `app/plugins/prompts/base.py:26,30,35,40,45`
   - **Ação:** Adicionar type hints para todos os parâmetros
   - **Ferramenta:** Usar `mypy` para validação

3. **Documentar parâmetros de métodos**
   - **Arquivo:** `app/services/report/base.py:21`
   - **Ação:** Adicionar docstring com Args e Returns

### Critérios de Aceitação:
- [ ] Todos os métodos abstratos documentados
- [ ] Type hints completos em todos os parâmetros
- [ ] Documentação de parâmetros adicionada
- [ ] Validação com `mypy` passando

---

## 🎯 **ISSUE #3 - Estrutura e Formatação**
**🟡 PRIORIDADE: MÉDIA** - *Padronização e consistência do código*

### Tarefas:
1. **Corrigir indentação inconsistente**
   - **Arquivo:** `app/services/report/base.py:17`
   - **Ação:** Corrigir indentação do comentário
   - **Ferramenta:** Usar `black` para formatação

2. **Remover espaçamento desnecessário**
   - **Arquivo:** `app/plugins/base.py:11-12`
   - **Ação:** Remover linhas em branco extras

3. **Padronizar formatação geral**
   - **Ação:** Aplicar `black` em todo o projeto
   - **Ferramenta:** Configurar pre-commit hooks

### Critérios de Aceitação:
- [ ] Indentação corrigida
- [ ] Espaçamento padronizado
- [ ] Formatação consistente em todo o projeto
- [ ] Pre-commit hooks configurados

---

## 🎯 **ISSUE #4 - Tratamento de Erros e Configuração**
**🔴 PRIORIDADE: ALTA** - *Melhora robustez e debugging do sistema*

### Tarefas:
1. **Implementar tratamento específico de exceções**
   - **Arquivo:** `app/services/report/onestage_strategy.py:51+`
   - **Ação:** Substituir try-catch genérico por tratamento específico
   - **Benefício:** Melhor debugging e logs

2. **Centralizar configuração de logging**
   - **Arquivos:** Múltiplos
   - **Ação:** Padronizar uso do logger em todos os módulos
   - **Benefício:** Logs consistentes

3. **Centralizar configuração do MLflow**
   - **Arquivos:** Múltiplos
   - **Ação:** Centralizar configuração do MLflow
   - **Benefício:** Configuração única

### Critérios de Aceitação:
- [ ] Tratamento específico de exceções implementado
- [ ] Logging padronizado
- [ ] Configuração do MLflow centralizada
- [ ] Logs mais informativos

---

## 🎯 **ISSUE #5 - Schemas e Estrutura de Dados**
**🟡 PRIORIDADE: MÉDIA** - *Melhora documentação e clareza da API*

### Tarefas:
1. **Melhorar descrições de schemas Pydantic**
   - **Arquivo:** `app/domain/report.py`
   - **Ação:** Adicionar descrições consistentes para todos os campos
   - **Benefício:** Melhor documentação da API

2. **Documentar valores de enum**
   - **Arquivo:** `app/domain/status.py`
   - **Ação:** Adicionar docstrings para valores do enum
   - **Benefício:** Melhor compreensão dos valores

3. **Revisar uso de decorators**
   - **Arquivo:** `app/plugins/prompts/base.py`
   - **Ação:** Revisar uso de `@staticmethod` e `@abstractmethod`
   - **Benefício:** Código mais limpo

### Critérios de Aceitação:
- [ ] Descrições de schemas completas
- [ ] Enums documentados
- [ ] Decorators revisados
- [ ] Documentação da API melhorada

---

## 🎯 **ISSUE #7 - Padronização de Documentação para Inglês**
**🟢 PRIORIDADE: BAIXA** - *Padronização para facilitar colaboração internacional*

### Tarefas por Bloco do Sistema:

#### **Bloco 1: Core System**
- **Arquivos:** `app/core/`, `app/main.py`
- **Ação:** Traduzir docstrings e comentários para inglês


#### **Bloco 2: Database Layer**
- **Arquivos:** `app/db/`, `app/domain/`
- **Ação:** Padronizar documentação de interfaces e modelos
- **Foco:** Classes abstratas e schemas de dados

#### **Bloco 3: Services Layer**
- **Arquivos:** `app/services/`
- **Ação:** Traduzir documentação de serviços e estratégias
- **Foco:** Métodos de negócio e coordenação

#### **Bloco 4: Plugins System**
- **Arquivos:** `app/plugins/`
- **Ação:** Padronizar documentação de plugins e prompts
- **Foco:** Interfaces de plugins e templates

#### **Bloco 5: API Layer**
- **Arquivos:** `app/api/`, `app/schemas/`
- **Ação:** Traduzir documentação de endpoints e schemas
- **Foco:** Documentação da API REST

#### **Bloco 6: Scripts and Utils**
- **Arquivos:** `app/scripts/`, `app/validators/`
- **Ação:** Padronizar comentários em scripts de processamento
- **Foco:** Documentação de utilitários e validações

### Critérios de Aceitação:
- [ ] Todas as docstrings em inglês
- [ ] Comentários de código em inglês
- [ ] Documentação de APIs em inglês
- [ ] READMEs e documentação técnica em inglês
- [ ] Mensagens de log em inglês
- [ ] Nomes de variáveis e funções em inglês (quando aplicável)

---

## 🎯 **ISSUE #8 - Limpeza de Arquivos e Código**
**🟡 PRIORIDADE: MÉDIA** - *Reduz complexidade e melhora organização do projeto*

### Tarefas:
1. **Identificar e remover arquivos não utilizados**
   - **Ação:** Auditar todo o projeto para encontrar arquivos órfãos
   - **Ferramenta:** Usar análise estática para detectar imports não utilizados
   - **Benefício:** Reduzir tamanho do projeto e confusão

2. **Remover demos e exemplos desnecessários**
   - **Ação:** Identificar e remover arquivos de demonstração
   - **Critério:** Manter apenas código de produção
   - **Benefício:** Projeto mais limpo e focado

3. **Limpar dependências não utilizadas**
   - **Ação:** Revisar requirements.txt e remover pacotes não utilizados
   - **Ferramenta:** Usar `pip-autoremove` ou análise manual
   - **Benefício:** Reduzir tamanho e vulnerabilidades

### Critérios de Aceitação:
- [ ] Arquivos não utilizados identificados e removidos
- [ ] Demos e exemplos removidos
- [ ] Dependências não utilizadas removidas
- [ ] Projeto mais enxuto e organizado

---

## 🎯 **ISSUE #9 - Refinamento dos Prompts do IonNutri**
**🔴 PRIORIDADE: ALTA** - *Impacto direto na qualidade dos relatórios gerados*

### Tarefas:
1. **Analisar padrão atual dos relatórios do IonNutri**
   - **Ação:** Estudar estrutura e formato dos relatórios existentes
   - **Objetivo:** Entender o padrão esperado pelos usuários

2. **Refinar prompts para alinhar com o padrão**
   - **Arquivos:** `app/plugins/ionnutri_plugin.py`, `app/plugins/prompts/`
   - **Ação:** Ajustar templates de prompts para gerar relatórios no formato correto
   - **Benefício:** Relatórios mais consistentes e profissionais

3. **Testar e validar novos prompts**
   - **Ação:** Executar testes com dados reais
   - **Critério:** Verificar se os relatórios gerados seguem o padrão esperado

### Critérios de Aceitação:
- [ ] Padrão dos relatórios analisado e documentado
- [ ] Prompts refinados para gerar relatórios no formato correto
- [ ] Testes executados e validados
- [ ] Relatórios gerados seguem o padrão do IonNutri

---

## 🎯 **ISSUE #10 - Conversão de Markdown para PDF**
**🟡 PRIORIDADE: MÉDIA** - *Nova funcionalidade para melhorar experiência do usuário*

### Tarefas:
1. **Implementar funcionalidade de conversão MD para PDF**
   - **Ação:** Adicionar biblioteca de conversão (ex: `markdown2pdf`, `weasyprint`)
   - **Arquivo:** Novo módulo em `app/services/`
   - **Benefício:** Relatórios em formato PDF para melhor distribuição

2. **Configurar template de PDF**
   - **Ação:** Definir layout, fontes e estilos para o PDF
   - **Objetivo:** PDFs profissionais e bem formatados

3. **Integrar conversão no fluxo de geração de relatórios**
   - **Ação:** Adicionar opção de exportar relatórios em PDF
   - **API:** Endpoint para download de PDF
   - **Benefício:** Usuários podem baixar relatórios em PDF

### Critérios de Aceitação:
- [ ] Funcionalidade de conversão MD para PDF implementada
- [ ] Template de PDF configurado e testado
- [ ] Integração no fluxo de geração de relatórios
- [ ] Endpoint de download de PDF funcionando
- [ ] PDFs gerados com formatação adequada

---

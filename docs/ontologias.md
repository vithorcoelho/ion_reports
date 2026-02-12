# Ontologia do Conhecimento Nutri-Metabólico

## 1. Visão Geral

Esta ontologia define a estrutura conceitual do conhecimento nutri-metabólico para interpretação dos testes TNM (Teste Nutrimetabólico) e geração de recomendações personalizadas. Ela mapeia as relações entre metabólitos, vias metabólicas, manifestações clínicas e intervenções nutricionais, criando uma base científica sólida para a personalização de condutas nutricionais.

## 2. Entidades Principais

### 2.1 Metabólito

Representa uma molécula participante nos processos metabólicos que é medida no teste TNM.

**Tipos**:
- **Metabólito Exclusivo**: Metabólitos analisados apenas pela IonNutri (28 exclusivos)
- **Metabólito Comum**: Metabólitos analisados por outros testes metabólicos também

**Atributos**:
- **Identificadores**: código, nome
- **Parâmetros de medição**: unidade de medida, faixa de referência (mínimo e máximo)
- **Características bioquímicas**: processos bioquímicos, cofatores necessários
- **Fatores causais**: causas de níveis baixos, causas de níveis altos
- **Nutrição**: fontes alimentares, cofatores nutricionais

**Exemplo**: 1-Estearoil-lisofosfatidilcolina [HDL] - Molécula fosfolipídica componente do HDL, envolvida no transporte reverso de colesterol e sinalização celular.

### 2.2 Via Metabólica

Representa um conjunto de reações bioquímicas relacionadas que constituem um processo metabólico específico.

**Tipos**:
- **Ciclo Bioquímico**: Processos cíclicos como o Ciclo de Krebs
- **Via Reguladora**: Vias envolvidas na regulação metabólica
- **Via de Sinalização**: Vias envolvidas em processos de comunicação celular

**Atributos**:
- **Identificadores**: nome, grupo funcional
- **Características**: função biológica, importância clínica
- **Requisitos**: cofatores necessários
- **Contexto**: processos precedentes, processos subsequentes

**Exemplo**: Imunometabolismo - Ricas em Ômega 9 e Ômega 3 - Conjunto de adaptações no metabolismo celular que ocorre em células imunes para otimizar a função imunológica.

### 2.3 Manifestação

Representa um sintoma, sinal ou condição clínica associada a alterações nos níveis de metabólitos.

**Tipos**:
- **Sintoma de Nível Alto**: Manifestação associada a níveis elevados de um metabólito
- **Sintoma de Nível Baixo**: Manifestação associada a níveis reduzidos de um metabólito

**Atributos**:
- **Descrição**: descrição da manifestação, mecanismo fisiológico
- **Gravidade**: potencial de gravidade, cronicidade
- **Contexto clínico**: sistema afetado, comorbidades associadas

**Exemplo**: Comprometimento da função do HDL e do transporte reverso de colesterol - Uma manifestação de níveis baixos de 1-Estearoil-lisofosfatidilcolina que pode contribuir para o desenvolvimento de doenças cardiovasculares.

### 2.4 Intervenção Nutricional

Representa uma abordagem terapêutica nutricional para corrigir desequilíbrios metabólicos.

**Tipos**:
- **Intervenção para Nível Alto**: Destinada a normalizar níveis elevados
- **Intervenção para Nível Baixo**: Destinada a normalizar níveis reduzidos
- **Conduta Alimentar**: Baseada em alimentos e padrões alimentares
- **Conduta de Suplementação**: Baseada em suplementos nutricionais

**Atributos**:
- **Descrição**: tipo, descrição detalhada
- **Aplicação**: duração recomendada, resultados esperados
- **Considerações clínicas**: contraindicações, avisos e precauções
- **Priorização**: prioridade clínica (alta, média, baixa)

**Exemplo**: Aumento do consumo de fontes de colina e ácidos graxos essenciais - Uma intervenção alimentar para níveis baixos de 1-Estearoil-lisofosfatidilcolina, incluindo consumo de gema de ovo, peixes gordurosos e oleaginosas.

### 2.5 Alimento

Representa um alimento ou grupo alimentar recomendado como parte de uma intervenção nutricional.

**Tipos**:
- **Carboidrato Complexo**: Alimentos ricos em carboidratos complexos
- **Proteína Vegetal**: Fontes de proteínas de origem vegetal
- **Proteína Animal**: Fontes de proteínas de origem animal
- **Gordura Saudável**: Alimentos ricos em gorduras benéficas
- **Fitoquímico**: Alimentos ricos em compostos bioativos vegetais

**Atributos**:
- **Identificação**: nome, grupo alimentar
- **Características nutricionais**: nutrientes principais, porção recomendada
- **Prescrição**: frequência de consumo recomendada, alternativas equivalentes
- **Considerações clínicas**: potencial alergênico, contraindicações

**Exemplo**: Gema de ovo - Fonte de colina, fosfatidilcolina, vitamina B12 e vitamina D, recomendada em porção de 1 unidade, 3-4 vezes por semana para níveis baixos de 1-Estearoil-lisofosfatidilcolina.

### 2.6 Suplemento

Representa um suplemento nutricional recomendado como parte de uma intervenção.

**Tipos**:
- **Vitamina**: Suplementos vitamínicos
- **Mineral**: Suplementos minerais
- **Aminoácido**: Suplementos de aminoácidos
- **Ácido Graxo**: Suplementos de ácidos graxos essenciais
- **Enzima**: Suplementos enzimáticos
- **Fitoquímico**: Compostos bioativos isolados de plantas

**Atributos**:
- **Identificação**: nome, composição ativa
- **Dosagem**: dosagem recomendada (mínima e máxima), unidade de dosagem
- **Administração**: forma padronizada, tempo de tratamento
- **Farmacologia**: mecanismo de ação, biodisponibilidade
- **Segurança**: interações medicamentosas, contraindicações

**Exemplo**: Ômega-3 (EPA/DHA) - Suplemento de ácidos graxos poliinsaturados com dosagem recomendada de 1000-3000mg diários, com efeitos anti-inflamatórios e cardioprotetores, recomendado para níveis baixos de 1-Estearoil-lisofosfatidilcolina.

### 2.7 Fator Contextual

Representa uma condição ou circunstância do paciente que pode influenciar a interpretação dos resultados ou a escolha das intervenções.

**Tipos**:
- **Indicador Antropométrico**: Medidas como peso, altura, IMC
- **Histórico Clínico**: Doenças prévias ou atuais
- **Hábito de Vida**: Estilo de vida, atividade física, sono
- **Medicação Atual**: Medicamentos em uso
- **Cirurgias Prévias**: Intervenções cirúrgicas realizadas

**Atributos**:
- **Identificação**: nome, categoria
- **Relevância**: impacto metabólico, considerações clínicas
- **Dados**: fonte na anamnese, relevância clínica

**Exemplo**: Uso de inibidores da bomba de prótons (como Omeprazol) - Medicação que pode reduzir a absorção de diversas vitaminas e minerais, interferindo na função de enzimas essenciais para o metabolismo de macronutrientes.

### 2.8 Perfil Metabólico

Representa um padrão característico de alterações em múltiplos metabólitos que sugere um estado metabólico específico.

**Tipos**:
- **Desequilíbrio Leve**: Alterações de impacto limitado
- **Desequilíbrio Moderado**: Alterações de impacto intermediário
- **Desequilíbrio Grave**: Alterações de alto impacto

**Atributos**:
- **Identificação**: nome, descrição
- **Características**: padrões característicos, vias afetadas
- **Marcadores**: metabólitos alterados
- **Abordagem**: abordagem terapêutica geral

**Exemplo**: Perfil Inflamatório Cardiovascular - Padrão de desequilíbrios caracterizado por alterações em metabólitos relacionados ao metabolismo lipídico e inflamação sistêmica, incluindo níveis baixos de 1-Estearoil-lisofosfatidilcolina e alterações em marcadores inflamatórios.

### 2.9 Evidência Científica

Representa uma fonte de conhecimento científico que fundamenta as relações entre metabólitos, manifestações e intervenções.

**Tipos**:
- **Estudo Clínico**: Pesquisa clínica original
- **Revisão Sistemática**: Síntese de múltiplos estudos
- **Consenso Científico**: Diretrizes baseadas em consenso de especialistas

**Atributos**:
- **Referência**: título, autores, publicação, ano
- **Identificação**: DOI, URL da publicação
- **Conteúdo**: tipo de estudo, principais conclusões
- **Qualidade**: nível de evidência

**Exemplo**: "The Fluid Aspect of the Mediterranean Diet in the Prevention and Management of Cardiovascular Disease and Diabetes: The Role of Polyphenol Content in Moderate Consumption of Wine and Olive Oil" - Revisão sistemática publicada em Nutrients (2019) que fundamenta intervenções alimentares para melhorar o perfil lipídico.

## 3. Relações Ontológicas

### 3.1 Relações entre Metabólitos e Vias Metabólicas

- **Participa Em**: Metabólito → Via Metabólica
  - *Significado*: Um metabólito é parte de uma via metabólica específica
  - *Exemplo*: 1-Estearoil-lisofosfatidilcolina participa na via do Imunometabolismo

- **Influencia**: Metabólito → Metabólito
  - *Significado*: Alterações em um metabólito podem afetar os níveis de outro
  - *Exemplo*: Níveis de L-carnitina influenciam os níveis de Acetil-L-carnitina

### 3.2 Relações entre Metabólitos e Manifestações

- **Níveis Baixos Causam**: Metabólito → Sintoma de Nível Baixo
  - *Significado*: Níveis reduzidos de um metabólito podem causar determinados sintomas
  - *Exemplo*: Níveis baixos de 1-Estearoil-lisofosfatidilcolina causam comprometimento da função do HDL

- **Níveis Altos Causam**: Metabólito → Sintoma de Nível Alto
  - *Significado*: Níveis elevados de um metabólito podem causar determinados sintomas
  - *Exemplo*: Níveis altos de 1-Estearoil-lisofosfatidilcolina causam aumento da ativação inflamatória sistêmica

### 3.3 Relações entre Manifestações e Intervenções

- **Tratada Por**: Manifestação → Intervenção Nutricional
  - *Significado*: Uma manifestação clínica pode ser tratada por uma intervenção específica
  - *Exemplo*: Comprometimento da função do HDL é tratado por aumento do consumo de fontes de colina

### 3.4 Relações entre Intervenções e Alimentos/Suplementos

- **Inclui**: Intervenção Nutricional → Alimento / Suplemento
  - *Significado*: Uma intervenção recomenda determinados alimentos ou suplementos
  - *Propriedades*: quantidade, frequência, prioridade
  - *Exemplo*: A intervenção "Aumento do consumo de fontes de colina" inclui "Gema de ovo" (1 unidade, 3-4x por semana)

### 3.5 Relações com Fatores Contextuais

- **Contraindicada Para**: Intervenção Nutricional → Fator Contextual
  - *Significado*: Uma intervenção não é recomendada em presença de determinado fator
  - *Exemplo*: Suplementação de Ômega-3 em altas doses é contraindicada para pacientes com distúrbios de coagulação

- **Afeta**: Fator Contextual → Metabólito
  - *Significado*: Um fator contextual pode influenciar os níveis de um metabólito
  - *Propriedades*: mecanismo
  - *Exemplo*: Uso de Omeprazol afeta a absorção de nutrientes, influenciando diversos metabólitos

### 3.6 Relações com Perfil Metabólico

- **Associada A**: Via Metabólica → Perfil Metabólico
  - *Significado*: Uma via metabólica está associada a um padrão metabólico específico
  - *Exemplo*: A via do Imunometabolismo está associada ao Perfil Inflamatório Cardiovascular

- **Caracterizado Por**: Perfil Metabólico → Metabólito
  - *Significado*: Um perfil metabólico é caracterizado por alterações em metabólitos específicos
  - *Propriedades*: importância (primário, secundário)
  - *Exemplo*: O Perfil Inflamatório Cardiovascular é caracterizado por níveis baixos de 1-Estearoil-lisofosfatidilcolina

### 3.7 Relações com Evidências Científicas

- **Evidenciado Por**: Metabólito / Intervenção → Evidência Científica
  - *Significado*: O conhecimento sobre um metabólito ou intervenção é baseado em evidências científicas
  - *Exemplo*: A relação entre 1-Estearoil-lisofosfatidilcolina e saúde cardiovascular é evidenciada por estudos específicos

## 4. Padrões Semânticos

### 4.1 Padrão de Diagnóstico

Estrutura para identificar desequilíbrios metabólicos a partir de resultados de exames:

```
SE Metabólito.valor < Metabólito.faixaReferênciaMin ENTÃO
    Estado = "Desequilíbrio Baixo"
    Sintomas = Metabólito → níveis_baixos_causam → Manifestação
    Intervenções = Sintomas → tratada_por → Intervenção
```

### 4.2 Padrão de Recomendação Personalizada

Estrutura para gerar recomendações considerando fatores contextuais:

```
PARA CADA Intervenção EM Intervenções
    SE NÃO EXISTE (Intervenção → contraindicada_para → FatorContextual)
    ONDE FatorContextual EM Anamnese DO Paciente ENTÃO
        RecomendaçõesVálidas += Intervenção
```

### 4.3 Padrão de Identificação de Perfil

Estrutura para reconhecer padrões metabólicos complexos:

```
SE EXISTEM Múltiplos Metabólito COM Desequilíbrio E
   EXISTE PerfilMetabólico ONDE
      PARA TODOS Metabólito EM PerfilMetabólico.metabólitosCaracterísticos
         Metabólito TEM Desequilíbrio
   ENTÃO
      PerfilIdentificado = PerfilMetabólico
      RecomendaçãoGeral = PerfilMetabólico.abordagemTerapêuticaGeral
```

## 5. Aplicação ao Caso TNM

### 5.1 Processo de Interpretação Ontológica

O processo de interpretação dos resultados do teste TNM usando esta ontologia segue o fluxo:

1. **Identificação de Desequilíbrios**: Comparação dos valores dos 57 metabólitos com suas faixas de referência
2. **Mapeamento de Manifestações**: Identificação das manifestações clínicas associadas a cada desequilíbrio
3. **Contextualização**: Consideração dos fatores contextuais da anamnese do paciente
4. **Padrões Complexos**: Identificação de perfis metabólicos a partir de múltiplos desequilíbrios
5. **Recomendações Personalizadas**: Geração de intervenções nutricionais específicas
6. **Adaptação Contextual**: Ajuste das recomendações com base nos fatores contextuais

### 5.2 Categorização Nutricional

O relatório TNM classifica as recomendações em três grandes categorias:

1. **Energéticos**: Recomendações relacionadas ao metabolismo energético e vias como a glicólise e o ciclo do ácido cítrico
2. **Construtores**: Recomendações ligadas ao metabolismo proteico, aminoácidos e estruturas celulares
3. **Reguladores**: Recomendações focadas em cofatores, antioxidantes e moduladores metabólicos

### 5.3 Extensibilidade

Esta ontologia foi projetada para ser extensível, permitindo:

1. **Adição de Novos Metabólitos**: Inclusão de novos biomarcadores conforme avanços tecnológicos
2. **Refinamento de Relações**: Atualização das relações entre entidades com base em novas evidências científicas
3. **Expansão de Intervenções**: Incorporação de novas abordagens terapêuticas nutricionais
4. **Integração com Outras Ontologias**: Possibilidade de integração com ontologias biomédicas mais amplas

## 6. Considerações Finais

Esta ontologia do conhecimento nutri-metabólico proporciona uma estrutura conceitual abrangente que captura:

1. A complexidade das interações metabólicas
2. A relação entre desequilíbrios metabólicos e manifestações clínicas
3. O embasamento científico para intervenções nutricionais personalizadas
4. A contextualização com base em fatores individuais do paciente

Este modelo ontológico constitui o fundamento conceitual para a automação inteligente dos relatórios TNM, garantindo recomendações nutricionais personalizadas e cientificamente embasadas.

## 7. Implementação Programática

### 7.1 Representação em JSON para Grafos de Conhecimento

Para implementar programaticamente esta ontologia em sistemas de bancos de dados de grafos (como Neo4j), propõe-se o seguinte formato JSON:

```json
{
  "metabolites": [
    {
      "id": "metabolito-1",
      "name": "1-ESTEAROIL-LISOFOSFATIDILCOLINA [HDL]",
      "definition": "O 1-estearoil-lisofosfatidilcolina (1-SLPC) é uma molécula que faz parte dos fosfolipídios...",
      "measurement_unit": "mmol/L",
      "reference_range_min": 0.8,
      "reference_range_max": 1.2,
      "food_sources": [
        "Gema de ovo",
        "Oleaginosas",
        "Peixes"
      ],
      "metabolic_pathway": "via-1"
    }
  ],
  "metabolic_pathways": [
    {
      "id": "via-1",
      "name": "Imunometabolismo - Ricas em Ômega 9 e Ômega 3",
      "definition": "O imunometabolismo envolve a forma como as células do sistema imunológico...",
      "biological_function": "Regulação do metabolismo celular em células imunes",
      "clinical_importance": "Regula respostas imunológicas e processos inflamatórios"
    }
  ],
  "manifestations": [
    {
      "id": "manifestacao-baixo-1",
      "description": "Comprometimento da função do HDL e do transporte reverso de colesterol",
      "type": "LowLevel",
      "physiological_mechanism": "Redução da eficiência na remoção de colesterol das células periféricas",
      "severity": "Moderada",
      "affected_system": "Cardiovascular",
      "metabolite": "metabolito-1"
    },
    {
      "id": "manifestacao-alto-1",
      "description": "Aumento da ativação inflamatória sistêmica",
      "type": "HighLevel",
      "metabolite": "metabolito-1"
    }
  ],
  "interventions": [
    {
      "id": "intervencao-baixo-1",
      "type": "LowLevel",
      "description": "Aumento do consumo de fontes de colina",
      "recommended_duration": "3 meses",
      "expected_results": "Melhora do perfil lipídico e função do HDL",
      "contraindications": ["Histórico de câncer de próstata avançado"],
      "priority": "high",
      "manifestation": "manifestacao-baixo-1"
    }
  ],
  "foods": [
    {
      "id": "alimento-1",
      "name": "Gema de ovo",
      "food_group": "Proteína Animal",
      "main_nutrients": ["Colina", "Vitamina B12"],
      "recommended_portion": "1 unidade",
      "consumption_frequency": "3-4 vezes por semana",
      "alternatives": ["Lecitina de soja"],
      "allergenic_potential": true
    }
  ],
  "supplements": [
    {
      "id": "suplemento-1",
      "name": "Ômega-3 (EPA/DHA)",
      "active_composition": "Ácidos graxos poliinsaturados EPA e DHA",
      "minimum_dosage": 1000,
      "maximum_dosage": 3000,
      "dosage_unit": "mg",
      "administration_form": "Cápsulas",
      "action_mechanism": "Anti-inflamatório e cardioprotetor",
      "drug_interactions": ["Anticoagulantes", "Anti-plaquetários"],
      "contraindications": ["Distúrbios de coagulação"],
      "intervention": "intervencao-baixo-1"
    }
  ],
  "contextual_factors": [
    {
      "id": "fator-1",
      "name": "Composição corporal",
      "category": "Indicador Antropométrico",
      "metabolic_impact": "Alteração no metabolismo lipídico",
      "anamnesis_source": "Avaliação antropométrica",
      "clinical_relevance": "Alta",
      "affected_metabolites": ["metabolito-1"]
    }
  ],
  "metabolic_profiles": [
    {
      "id": "perfil-1",
      "name": "Perfil Inflamatório Cardiovascular",
      "description": "Padrão de desequilíbrios caracterizado por alterações em metabólitos relacionados ao metabolismo lipídico e inflamação sistêmica",
      "general_therapeutic_approach": "Dieta anti-inflamatória com ênfase em ômega-3 e antioxidantes",
      "severity": "Moderado",
      "associated_pathways": ["via-1"],
      "characteristic_metabolites": [
        {"id": "metabolito-1", "importance": "primary"}
      ]
    }
  ],
  "scientific_evidence": [
    {
      "id": "evidencia-1",
      "title": "The Fluid Aspect of the Mediterranean Diet...",
      "authors": "Ditano-Vázquez, P., Torres-Peña, J. D., Galeano-Valle, F., et al.",
      "publication": "Nutrients",
      "volume": "11(11)",
      "pages": "2833",
      "year": "2019",
      "doi": "https://doi.org/10.3390/nu11112833",
      "study_type": "Revisão sistemática",
      "evidence_level": "Alto",
      "metabolite": "metabolito-1"
    }
  ]
}
```

### 7.2 Mapeamento Entre JSON e Relações Ontológicas

O formato JSON acima define implicitamente as relações entre as entidades através de referências de chaves estrangeiras:

1. **Participação em Via Metabólica**:
   - Mapeamento: `metabolite.metabolic_pathway` → id da via metabólica
   - Relação: `Metabolite` → `PARTICIPATES_IN` → `MetabolicPathway`

2. **Causação de Manifestações**:
   - Mapeamento: `manifestation.metabolite` + `manifestation.type`
   - Relação: Se type="LowLevel": `Metabolite` → `LOW_LEVELS_CAUSE` → `Manifestation`
   - Relação: Se type="HighLevel": `Metabolite` → `HIGH_LEVELS_CAUSE` → `Manifestation`

3. **Tratamento de Manifestações**:
   - Mapeamento: `intervention.manifestation`
   - Relação: `Manifestation` → `TREATED_BY` → `Intervention`

4. **Inclusão de Alimentos/Suplementos**:
   - Mapeamento: `supplement.intervention`
   - Relação: `Intervention` → `INCLUDES` → `Supplement`

5. **Afetação por Fatores Contextuais**:
   - Mapeamento: `contextual_factor.affected_metabolites`
   - Relação: `ContextualFactor` → `AFFECTS` → `Metabolite`

6. **Caracterização de Perfis**:
   - Mapeamento: `metabolic_profile.characteristic_metabolites`
   - Relação: `MetabolicProfile` → `CHARACTERIZED_BY` → `Metabolite` (com propriedade `importance`)

7. **Associação com Vias**:
   - Mapeamento: `metabolic_profile.associated_pathways`
   - Relação: `MetabolicPathway` → `ASSOCIATED_WITH` → `MetabolicProfile`

8. **Evidenciação Científica**:
   - Mapeamento: `scientific_evidence.metabolite`
   - Relação: `Metabolite` → `EVIDENCED_BY` → `ScientificEvidence`

### 7.3 Implementação em Neo4j

Para implementar esta estrutura em Neo4j, pode-se utilizar a biblioteca APOC para carregar os dados JSON e criar o grafo:

```cypher
CALL apoc.load.json('file:///path/to/ontology.json') YIELD value

// Create metabolite nodes
UNWIND value.metabolites AS metabolite
MERGE (m:Metabolite {id: metabolite.id})
SET m += apoc.map.clean(metabolite, ['metabolic_pathway', 'id'], [])

// Create metabolic pathway nodes
UNWIND value.metabolic_pathways AS pathway
MERGE (v:MetabolicPathway {id: pathway.id})
SET v += apoc.map.clean(pathway, ['id'], [])

// Link metabolites and pathways
UNWIND value.metabolites AS metabolite
MATCH (m:Metabolite {id: metabolite.id})
MATCH (v:MetabolicPathway {id: metabolite.metabolic_pathway})
MERGE (m)-[:PARTICIPATES_IN]->(v)

// Continue with creation of other entities and relationships...
```

### 7.4 Extensibilidade do Modelo de Dados

Este modelo de dados JSON foi projetado para ser:

1. **Flexible**: Permite adicionar novos atributos a qualquer entidade
2. **Incremental**: Permite a adição de novos tipos de entidades (nós) ou relações
3. **Compatible**: Segue as convenções do Neo4j e outras bases de grafos
4. **Traceable**: Mantém IDs consistentes para referência cruzada entre entidades

Para estender o modelo, basta adicionar novos campos às estruturas existentes ou criar novas coleções de entidades, mantendo o padrão de referenciamento para estabelecer as relações adequadas no grafo de conhecimento.

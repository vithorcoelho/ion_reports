"""IonNutri-specific prompt templates and configurations.

This module contains prompt templates, configurations, and utilities specifically
designed for the IonNutri plugin to generate comprehensive nutritional medical reports.
"""

import json
from pathlib import Path

from pydantic import BaseModel

from app.core.logging import logger
from app.domain.kg_result import KGResult
from app.plugins.prompts.base import PromptInterface
from app.plugins.prompts.prompt_utils import PromptConfig, safe_encode
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis


def pydantic_to_dict(obj):
    """Convert Pydantic models to dictionaries recursively.

    Args:
        obj: The object to convert (can be BaseModel, list, dict, or primitive).

    Returns:
        dict | list | Any: Converted object with Pydantic models as dictionaries.

    """
    if isinstance(obj, BaseModel):
        return obj.model_dump()
    elif isinstance(obj, list):
        return [pydantic_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: pydantic_to_dict(v) for k, v in obj.items()}
    else:
        return obj


BASE_SYSTEM_IONNUTRI_PROMPT = (
    "Você é um especialista em medicina nutricional com foco em interpretação de exames nutrimetabolômicos (TNM).\n"
    "Siga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada."
)

PROMPT_IONNUTRI_CONFIGS: dict[str, PromptConfig] = {
    "findings": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Analise os dados metabólicos e descreva os principais achados clínicos relevantes para o paciente.",
    ),
    "deficiencies": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Liste e explique as deficiências nutricionais identificadas, correlacionando com os achados laboratoriais.",
    ),
    "nutrition": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Sugira recomendações nutricionais personalizadas para correção das deficiências encontradas.

        **PRIORIDADE ABSOLUTA:** Use EXCLUSIVAMENTE os alimentos recomendados pelo knowledge graph. NÃO invente ou liste alimentos que não estejam nas recomendações do KG.

        Organize as recomendações em categorias DISTINTAS e SEM SOBREPOSIÇÃO:

        1. **Energéticos** - APENAS CARBOIDRATOS do KG:
           Exemplos de categorização: tubérculos (batata doce, inhame, mandioquinha, cará), cereais integrais (arroz integral, quinoa, aveia), tapioca e farinhas
           Liste entre 4-5 alimentos

        2. **Construtores** - APENAS PROTEÍNAS do KG:
           Exemplos de categorização: carnes magras, peixes, ovos, leguminosas (lentilha, grão-de-bico, feijões), proteínas vegetais (tofu, tempeh), lácteos, cogumelos
           Liste entre 8-10 alimentos

        3. **Reguladores** - FRUTAS, VERDURAS e LEGUMES do KG:
           Exemplos de categorização: frutas diversas (frutas vermelhas, cítricas, banana, maçã), verduras (espinafre, couve, rúcula, alface), legumes/vegetais (brócolis, cenoura, abobrinha, pimentão)
           Liste entre 4-5 alimentos

        4. **Energéticas e Construtoras** (Gorduras) - APENAS GORDURAS do KG:
           Exemplos de categorização: óleos (azeite de oliva, óleo de coco), oleaginosas (castanhas, nozes, amêndoas), sementes (chia, linhaça, abóbora, gergelim), pastas (manteiga de amendoim, tahine), abacate
           Liste entre 6-10 alimentos

        ATENÇÃO - Regras de Categorização:
        - NÃO repita alimentos entre categorias
        - Salmão e ovos vão em "Construtores", NÃO em "Energéticos"
        - Amêndoas e abacate vão em "Energéticas e Construtoras", NÃO em outras seções
        - APENAS use alimentos que estejam nas recomendações do knowledge graph

        Para cada alimento RECOMENDADO PELO KG, forneça:
        - Nome do alimento e nutrientes principais entre parênteses
        - Quantidade sugerida (em gramas ou unidades)
        - Frequência recomendada""",
    ),
    "lifestyle": PromptConfig(
        context_sections=["patient_data"],
        objective="""Forneça orientações de bem-estar e estilo de vida focadas em:
        - Qualidade do sono
        - Controle de estresse
        - Estratégias de recuperação (se atleta)
        - Hidratação adequada
        - Outros hábitos relevantes ao perfil do paciente

        Use formato de lista com tópicos claros e diretos.""",
    ),
    "supplements": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Sugira suplementações necessárias baseadas nos dados metabólicos e deficiências identificadas.

        PRIORIZE os suplementos recomendados pelo knowledge graph.

        Para cada suplemento, forneça:
        - Nome do suplemento
        - Dose sugerida (com unidade de medida)
        - Objetivo/justificativa clara relacionada aos achados metabólicos

        Organize em formato de tabela ou lista estruturada.""",
    ),
    "summary": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Crie um relatório TNM narrativo em formato de prosa corrida, dividido em parágrafos bem estruturados:

        INICIE o texto com a frase:
        "O paciente X apresenta..."

        DESENVOLVA o conteúdo abordando os seguintes pontos DE FORMA INTEGRADA (sem tópicos ou listas):

        1. **Panorama geral dos desequilíbrios metabólicos**: Descreva brevemente os principais achados, como:
           - Alterações em processos epigenéticos (metilação, acetilação)
           - Saúde intestinal (disbiose, SIBO)
           - Disfunção mitocondrial
           - Estresse oxidativo
           - Inflamação crônica de baixo grau

        2. **Comparação evolutiva** (se houver exames anteriores): Destaque melhoras ou pioras em relação a exames anteriores, mencionando possíveis causas dessas variações (ajustes na dieta, suplementação, treinamento, etc.)

        3. **Carências nutricionais**: Descreva insuficiências de vitaminas do complexo B e minerais (selênio, cobre, zinco, manganês), relacionando-as a:
           - Sintomas clínicos
           - Contextos fisiológicos (alta demanda metabólica, má absorção intestinal, uso de medicamentos, estresse oxidativo elevado)

        4. **Consequências metabólicas**: Explique como esses desequilíbrios impactam:
           - Processos energéticos celulares
           - Cognição e clareza mental
           - Imunidade
           - Recuperação muscular (se aplicável)
           - Performance global

        5. **Conclusão**: Finalize reforçando a importância de intervenções personalizadas:
           - Ajustes alimentares
           - Suplementação direcionada
           - Mudanças de estilo de vida
           - Objetivo: restaurar equilíbrio metabólico, promover longevidade e otimizar desempenho físico e mental

        REQUISITOS DE FORMATO:
        - Use linguagem técnica, mas compreensível
        - Mantenha tom empático e humanizado
        - Texto fluido com parágrafos bem conectados
        - NÃO use listas ou bullet points
        - NÃO use markdown além de parágrafos normais
        - Conecte as ideias de forma natural e coesa""",
    ),
    "guidelines": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Forneça diretrizes clínicas baseadas nos achados e deficiências.",
    ),
    "exams": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Liste exames complementares recomendados e justifique cada um.",
    ),
    "markdown_report": PromptConfig(
        context_sections=[],
        system_prompt="""Você é um especialista em medicina nutricional e nutrimetabolômica responsável por redigir relatórios clínicos da IonNutri.
    Seu papel é elaborar um relatório TNM completo, coeso e profissional, em formato markdown.
    O texto deve ter fluidez, coerência clínica, linguagem técnica e tom humanizado.""",
        objective="""# OBJETIVO
    Crie um relatório TNM completo em formato markdown, utilizando os dados estruturados fornecidos no CONTEXTO ADICIONAL abaixo.

    **Use EXATAMENTE a seguinte estrutura:**


    # IONNUTRI | NUTRIÇÃO DE PRECISÃO LTDA

    **Paciente:** [Busque em patient_id do contexto]
    **Data de Nascimento:** [Busque em birth_date do contexto]
    **Peso:** [Busque em anamnesis.personal_data.weight do contexto]kg
    **Altura:** [Busque em anamnesis.personal_data.height do contexto]m

    ---

    ## RELATÓRIO TNM

    [Use o conteúdo de `summary.content` como texto principal do relatório TNM - deve ser uma narrativa fluida em parágrafos, sem listas]

    ---

    ## RECOMENDAÇÃO NUTRICIONAL

    ### Reguladores
    [Liste as recomendações de frutas, legumes e verduras de `recommendations.nutritional.regulators` com formato:
    - Nome do alimento (nutrientes importantes): quantidade - frequência]

    ### Energéticos e Construtores

    [Liste EXATAMENTE 4 (quatro) fontes de gorduras boas de `recommendations.nutritional.fats`, utilizando o formato:
    - Nome do alimento: quantidade - frequência]
    [Liste EXATAMENTE 4 (quatro) recomendações de alimentos energéticos (carboidratos), preferencialmente livre de glúten, de `recommendations.nutritional.energetics`, utilizando o formato:
    - Nome do alimento (nutrientes): quantidade - frequência]
    [Liste EXATAMENTE 4 (quatro) recomendações de proteínas de `recommendations.nutritional.constructors`, priorizando carnes magras e preparações saudáveis (assado, grelhado ou cozido), utilizando o formato:
    - Nome do alimento: quantidade - frequência]]

    ### Observações Gerais
    [Adicione orientações gerais sobre hidratação, mastigação e outros hábitos alimentares]

    ---

    ## SUPLEMENTAÇÃO SUGERIDA

    [Crie uma tabela com 3 colunas: Suplemento | Dose Sugerida | Objetivo
    Liste cada suplemento de `recommendations.supplements` com suas respectivas informações]

    ---

    ## BEM-ESTAR E MELHORIA DA PERFORMANCE

    [Liste as recomendações de bem-estar de `recommendations.lifestyle` em formato de bullet points]

    > Seguir adequadamente a orientação nutricional reduz a propensão ao risco de várias doenças, incluindo obesidade, depressão, diabetes tipo II, hipertensão, câncer, Alzheimer, Parkinson e outras.

    ---

    **IONNUTRI**
    Rua Apiacás, 247, sobreloja - Perdizes
    05017-020 - São Paulo - SP
    Telefone: (11) 95655-5210
    """,
    ),
    "energetics": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Sugira APENAS alimentos fontes de CARBOIDRATOS adequados ao perfil metabólico do paciente.

        **PRIORIDADE MÁXIMA:** Use EXCLUSIVAMENTE os alimentos recomendados pelo knowledge graph que sejam carboidratos.

        Exemplos de categorização de carboidratos (use APENAS como referência para identificar se um alimento do KG é carboidrato):
        - Tubérculos: batata doce, inhame, mandioquinha, cará, batata inglesa
        - Cereais integrais: arroz integral, quinoa, aveia
        - Farinhas e tapioca

        REGRAS IMPORTANTES:
        - NÃO liste alimentos que não estejam recomendados pelo knowledge graph
        - NÃO inclua proteínas (carnes, ovos, peixes, leguminosas)
        - NÃO inclua gorduras (oleaginosas, óleos, abacate)
        - NÃO inclua vegetais (esses vão na seção "Reguladores")
        - Liste entre 3-4 alimentos, priorizando os mais relevantes para o perfil do paciente

        Para cada alimento RECOMENDADO PELO KG, forneça:
        - Nome do alimento e nutrientes principais entre parênteses (se relevante)
        - Quantidade sugerida (em gramas ou medidas caseiras como "1 xícara", "1 unidade média")
        - Frequência recomendada (ex: "4-5x na semana", "diariamente")""",
    ),
    "constructors": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Sugira alimentos construtores (fontes de PROTEÍNAS) adequados ao perfil metabólico do paciente.

        **PRIORIDADE MÁXIMA:** Use EXCLUSIVAMENTE os alimentos recomendados pelo knowledge graph que sejam fontes de proteína.

        Exemplos de categorização de proteínas (use APENAS como referência para identificar se um alimento do KG é proteína):
        - Carnes magras: frango, peru, carne bovina magra
        - Peixes: salmão, sardinha, tilápia, truta, pescada
        - Ovos
        - Leguminosas: lentilha, grão-de-bico, feijões, moyashi
        - Proteínas vegetais: tofu, tempeh, edamame, natto
        - Lácteos: iogurte natural, queijos
        - Cogumelos: shitake, shimeji, portobelo

        REGRAS IMPORTANTES:
        - NÃO liste alimentos que não estejam recomendados pelo knowledge graph
        - Liste entre 3-4 alimentos, priorizando os mais relevantes para o perfil do paciente
        - Varie entre fontes animais e vegetais conforme apropriado

        Para cada alimento RECOMENDADO PELO KG, forneça:
        - Nome do alimento e nutrientes principais entre parênteses
        - Quantidade sugerida (em gramas ou unidades)
        - Frequência recomendada""",
    ),
    "regulators": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Sugira alimentos reguladores (fontes de VITAMINAS e MINERAIS) adequados ao perfil metabólico do paciente.

        **PRIORIDADE MÁXIMA:** Use EXCLUSIVAMENTE os alimentos recomendados pelo knowledge graph que sejam frutas, verduras ou legumes.

        Exemplos de categorização (use APENAS como referência para identificar se um alimento do KG é regulador):
        - Frutas: frutas vermelhas (morango, framboesa, mirtilo), cítricas (laranja, limão), banana, maçã, pera, manga, uvas, kiwi, etc.
        - Verduras: espinafre, couve, rúcula, alface, acelga, agrião, etc.
        - Legumes/Vegetais: brócolis, couve-flor, cenoura, abobrinha, pimentão, tomate, beterraba, aspargos, alcachofra, etc.

        REGRAS IMPORTANTES:
        - NÃO liste alimentos que não estejam recomendados pelo knowledge graph
        - Liste entre 4-5 alimentos, priorizando os mais relevantes para as deficiências identificadas
        - Varie entre frutas, verduras e legumes

        Para cada alimento RECOMENDADO PELO KG, forneça:
        - Nome do alimento e nutrientes principais entre parênteses
        - Quantidade sugerida (em gramas ou medidas caseiras)
        - Frequência recomendada""",
    ),
    "fats": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Liste APENAS fontes de GORDURAS SAUDÁVEIS para o paciente.

        **PRIORIDADE MÁXIMA:** Use EXCLUSIVAMENTE os alimentos recomendados pelo knowledge graph que sejam fontes de gorduras saudáveis.

        Exemplos de categorização de gorduras (use APENAS como referência para identificar se um alimento do KG é gordura):
        - Óleos: azeite de oliva extra virgem, óleo de coco, óleo de prímula
        - Oleaginosas: castanhas do pará, nozes, amêndoas, castanhas de caju, macadâmia
        - Sementes: chia, linhaça, abóbora, gergelim, girassol
        - Pastas: manteiga de amendoim, manteiga de amêndoa, tahine (pasta de gergelim)
        - Abacate (única exceção que é uma fruta mas é fonte de gordura)

        REGRAS IMPORTANTES:
        - NÃO liste alimentos que não estejam recomendados pelo knowledge graph
        - NÃO inclua peixes (use a seção "Construtores" para isso, mesmo que contenham ômega-3)
        - NÃO inclua carboidratos ou proteínas
        - Liste entre 3-4 alimentos, priorizando os mais relevantes para o perfil do paciente

        Para cada alimento RECOMENDADO PELO KG, forneça:
        - Nome do alimento
        - Quantidade sugerida (em gramas ou medidas caseiras como "1 colher de sopa", "30g")
        - Frequência recomendada""",
    ),
    "foods": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Sugira alimentos recomendados de acordo com o perfil metabólico do paciente.",
    ),
}

"""
IonNutriPrompts - Geração de prompts configuráveis para o pipeline TNM.

Seções de contexto disponíveis:
- patient_data: Dados do paciente (id, idade, gênero, peso, altura, IMC, atividade física, histórico médico, medicações, intolerâncias, objetivo clínico, sono, estresse)
- metabolic_data: Dados metabólicos (alterações, vias afetadas, manifestações)

Exemplo de uso:
    prompts = IonNutriPrompts()
    system_prompt, user_prompt = prompts.get_findings_prompt(exam_data, anamnesis, kg_data)
    # system_prompt: instrução de sistema para o LLM
    # user_prompt: prompt do usuário com contexto estruturado

Para adicionar novos prompts, basta incluir uma entrada em PROMPT_IONNUTRI_CONFIGS.
"""


class IonNutriPrompts(PromptInterface):
    """Classe para geração de prompts configuráveis do IonNutri.

    Seções de contexto disponíveis:
    - patient_data: Dados do paciente
    - metabolic_data: Dados metabólicos

    Exemplos de uso:
        system_prompt, user_prompt = self.get_findings_prompt(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self.get_nutrition_prompt(exam_data, anamnesis, kg_data, section_name="nutrition")
    """

    @staticmethod
    def _read_ionnutri_template() -> str:
        """Lê o arquivo de template do relatório TNM."""
        try:
            template_path = Path("app/assets/ion_nutri_report.md")
            if template_path.exists():
                return template_path.read_text(encoding="utf-8")
            else:
                return "# Template IonNutri Padrão\n\n1. Relatório TNM\n2. Recomendações Nutricionais\n"
        except Exception as e:
            logger.warning(f"Error reading IonNutri template content: {str(e)}")
            return "Template IonNutri Padrão não disponível."

    @staticmethod
    def _build_context_section(section_name: str, data: dict) -> str:
        if section_name == "patient_data":
            patient = data.get("patient", {})
            return (
                f"# DADOS DO PACIENTE\n"
                f"ID: {patient.get('id', '')}\n"
                f"Idade: {patient.get('idade', '')}\n"
                f"Gênero: {patient.get('gênero', '')}\n"
                f"Peso: {patient.get('peso', '')} kg\n"
                f"Altura: {patient.get('altura', '')} m\n"
                f"IMC: {patient.get('imc', '')}\n"
                f"Atividade física: {patient.get('atividade_física', '')}\n"
                f"Histórico médico: {patient.get('histórico_médico', '')}\n"
                f"Medicações: {', '.join(patient.get('medicações', []))}\n"
                f"Intolerâncias: {patient.get('intolerâncias', '')}\n"
                f"Objetivo clínico: {patient.get('objetivo_clínico', '')}\n"
                f"Qualidade do sono: {patient.get('qualidade_sono', '')}\n"
                f"Horas de sono: {patient.get('horas_sono', '')}\n"
                f"Nível de estresse: {patient.get('nível_estresse', '')}\n"
            )

        elif section_name == "metabolic_data":
            metabolic = data.get("metabolic", {})
            return (
                f"# DADOS METABÓLICOS\n"
                f"Alterações: {metabolic.get('altered_metabs', '')}\n"
                f"Vias afetadas: {metabolic.get('pathways', '')}\n"
                f"Manifestações: {metabolic.get('manifestations', '')}\n"
                f"Suplementos recomendados pelo KG: {metabolic.get('kg_supplements', '')}\n"
                f"Alimentos recomendados pelo KG: {metabolic.get('kg_foods', '')}\n"
            )

        elif section_name == "tnm_template":
            return (
                f"# TEMPLATE TNM (SIGA RIGOROSAMENTE)\n{data.get('tnm_template', '')}"
            )

        return ""

    @staticmethod
    def _generate_prompt(
        prompt_type: str, data: dict, context: dict | None = None
    ) -> tuple[str, str]:
        if prompt_type not in PROMPT_IONNUTRI_CONFIGS:
            raise ValueError(f"Unknown prompt type: {prompt_type}")
        config = PROMPT_IONNUTRI_CONFIGS[prompt_type]

        # Construir contexto
        context_sections = [
            IonNutriPrompts._build_context_section(section, data)
            for section in config.context_sections
        ]

        # Adicionar contexto adicional se necessário
        if context:
            formatted_context = json.dumps(context, indent=2, ensure_ascii=False)
            context_sections.append(f"# CONTEXTO ADICIONAL\n{formatted_context}")

        user_prompt = "\n\n".join(context_sections) + f"\n\n{config.objective}"
        system_prompt = config.system_prompt or BASE_SYSTEM_IONNUTRI_PROMPT

        return system_prompt, user_prompt

    def _prepare_data(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> dict:
        """Prepara dados no formato esperado pelas seções de contexto."""
        patient_data = {
            "id": exam_data.patient_id,
            "idade": anamnesis.personal_data.age,
            "gênero": anamnesis.personal_data.gender,
            "peso": anamnesis.personal_data.weight,
            "altura": anamnesis.personal_data.height,
            "imc": anamnesis.personal_data.bmi,
            "atividade_física": anamnesis.context_factors.physical_activity.intensity,
            "histórico_médico": anamnesis.context_factors.medical_history,
            "medicações": (
                [
                    m.name if hasattr(m, "name") else str(m)
                    for m in anamnesis.context_factors.medications
                ]
                if anamnesis.context_factors.medications
                else []
            ),
            "intolerâncias": anamnesis.context_factors.intolerances,
            "objetivo_clínico": anamnesis.objective,
            "qualidade_sono": anamnesis.context_factors.sleep.quality,
            "horas_sono": anamnesis.context_factors.sleep.hours,
            "nível_estresse": anamnesis.context_factors.stress_level,
        }

        metabolic_data = {
            "altered_metabs": ", ".join(
                [f"{m.name} ({m.value} - {m.status})" for m in kg_data.metabolite_info]
            ),
            "pathways": (
                ", ".join([p.name for p in kg_data.pathway_impacts])
                if kg_data.pathway_impacts
                else "Nenhuma via afetada detectada"
            ),
            "manifestations": (
                ", ".join([m.description for m in kg_data.manifestations])
                if kg_data.manifestations
                else "Nenhuma manifestação registrada"
            ),
            "kg_supplements": ", ".join(
                [f"{s.name} (para {s.metabolite})" for s in kg_data.supplements]
            )
            if kg_data.supplements
            else "Nenhum suplemento recomendado pelo knowledge graph",
            "kg_foods": ", ".join(
                [f"{f.name} (para {f.metabolite})" for f in kg_data.foods]
            )
            if kg_data.foods
            else "Nenhum alimento recomendado pelo knowledge graph",
        }

        return {"patient": patient_data, "metabolic": metabolic_data}

    def get_findings_prompt(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> tuple[str, str]:
        """Get findings prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("findings", data)
        return system_prompt, safe_encode(user_prompt)

    def get_deficiencies_prompt(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> tuple[str, str]:
        """Get deficiencies prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("deficiencies", data)
        return system_prompt, safe_encode(user_prompt)

    def get_nutrition_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        section_name: str = "nutrition",
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Get nutrition prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt(section_name, data, context)
        return system_prompt, safe_encode(user_prompt)

    def get_lifestyle_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Get lifestyle prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("lifestyle", data, context)
        return system_prompt, safe_encode(user_prompt)

    def get_supplements_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Get supplements prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("supplements", data, context)
        return system_prompt, safe_encode(user_prompt)

    def get_summary_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Get summary prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("summary", data, context)
        return system_prompt, safe_encode(user_prompt)

    def get_guidelines_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict,
    ) -> tuple[str, str]:
        """Get guidelines prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("guidelines", data, context)
        return system_prompt, safe_encode(user_prompt)

    def get_exams_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict,
    ) -> tuple[str, str]:
        """Get exams prompt for IonNutri report."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, user_prompt = self._generate_prompt("exams", data, context)
        return system_prompt, safe_encode(user_prompt)

    def get_markdown_report_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        final_report_structured_data: dict,
    ) -> tuple[str, str]:
        """Get markdown report prompt for IonNutri report."""
        from datetime import datetime

        # Calculate approximate birth_date from age
        current_year = datetime.now().year
        birth_year = current_year - anamnesis.personal_data.age
        birth_date = f"{birth_year}-01-01"  # Approximate to January 1st

        # Read the TNM template and add our data
        data = {"tnm_template": IonNutriPrompts._read_ionnutri_template()}

        # Include patient data in the context for the markdown report
        context = {
            "final_report": final_report_structured_data,
            "patient_id": exam_data.patient_id,
            "birth_date": birth_date,
            "anamnesis": {
                "personal_data": {
                    "weight": anamnesis.personal_data.weight,
                    "height": anamnesis.personal_data.height,
                    "age": anamnesis.personal_data.age,
                }
            },
        }

        system_prompt, user_prompt = self._generate_prompt(
            "markdown_report", data, context
        )
        return system_prompt, safe_encode(user_prompt)

"""VidaNova-specific prompt templates and configurations."""

import json
from pathlib import Path

from app.core.logging import logger
from app.domain.kg_result import KGResult
from app.plugins.prompts.base import PromptInterface
from app.plugins.prompts.prompt_utils import PromptConfig, safe_encode
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis

BASE_SYSTEM_PROMPT = (
    "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\n"
    "Siga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
)

PROMPT_CONFIGS = {
    "findings": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Analise os dados metabólicos e descreva os principais achados clínicos relevantes para performance e fitness.",
    ),
    "supplements": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Sugira suplementações focadas em performance física, energia e recuperação muscular baseadas nos dados metabólicos.

        PRIORIZE os suplementos recomendados pelo knowledge graph

        Baseie as recomendações nos dados metabólicos, deficiências identificadas e suplementos recomendados pelo knowledge graph.""",
    ),
    "summary": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Crie um resumo em formato de prosa narrativa, dividido em 4 parágrafos:
        1) Visão geral com dados relevantes do perfil clínico, hábitos e contexto, utilizando tom impessoal (ex: "observa-se", "nota-se", "considerando-se").
        2) Interpretação sobre o laudo metabólico e achados principais, focando nas alterações identificadas e seus impactos, sem detalhar intervenções específicas.
        3) Diretrizes gerais de intervenção integrando alimentação, suplementação e treino de forma contextualizada, evitando detalhamentos que serão abordados em seções posteriores.
        4) Conclusão destacando o objetivo estabelecido e a importância da abordagem integrada para os resultados esperados.

        Mantenha tom impessoal e orientado ao leitor. Contextualize sempre o objetivo clínico identificado. Evite antecipar detalhes específicos de condutas que serão desenvolvidos nas próximas seções. Não use listas ou markdown; mantenha texto contínuo em parágrafos claros e bem estruturados.""",
    ),
    "diet_suggestions": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="""Crie sugestões alimentares baseadas EXCLUSIVAMENTE no tipo de dieta informado na anamnese do paciente.

        PRIORIZE os alimentos recomendados pelo knowledge graph

        Se o paciente indicou 'Como de tudo, sem restrições específicas (onívora)', foque apenas em sugestões para dieta onívora/carnívora. Se indicou outro tipo específico, foque apenas nesse tipo. Ignore completamente os outros tipos de dieta não mencionados na anamnese.

        Para cada sugestão alimentar, forneça também uma justificativa clara, relacionando-a aos achados metabólicos ou deficiências (ex.: “Alimento X devido à alteração Y”), mas sem rigidez — múltiplas relações podem existir.

        Formate cada recomendação como um item de lista com '-' para melhor organização.""",
    ),
    "training": PromptConfig(
        context_sections=["patient_data", "metabolic_data"],
        objective="Forneça recomendações de treino priorizando força e ganho de massa magra.",
    ),
    "markdown_report": PromptConfig(
        context_sections=[],
        system_prompt="""Você é um especialista em comunicação médica e formatação de relatórios de performance (Vida Nova) em markdown.
    Sua tarefa é usar os dados estruturados de um paciente para criar um relatório claro, profissional e focado em performance, seguindo uma estrutura pré-definida.
    A linguagem deve ser técnica, mas acessível. O output deve ser unicamente o relatório em markdown.""",
        objective="""# OBJETIVO
    Crie um relatório de performance em formato markdown, utilizando os dados do JSON fornecido em "CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)".

    **Use EXATAMENTE a seguinte estrutura e títulos:**


    # RELATÓRIO FINAL - Vida Nova

    (Cri um texto introdutório de `summary.content` do JSON como o texto principal aqui)

    ---

    ## Sugestão Alimentar
    (Use o conteúdo da seção `diet_suggestions` para criar uma visão consolidada e direta das recomendações alimentares, formatando cada recomendação como um item de lista simples com "-" para melhor legibilidade)

    ---

    ## Suplementação Sugerida
    (Liste cada suplemento da seção `supplements`, formatando com nome em negrito e os demais campos como tópicos)

    ---

    ## Dica de Treino
    (Use o conteúdo da seção `training` para descrever as recomendações, o que evitar e o foco)
    """,
    ),
}


class VidaNovaPrompts(PromptInterface):
    """Classe de gerenciamento de prompts do plugin VidaNova."""

    @staticmethod
    def _read_vidanova_template() -> str:
        """Lê o arquivo de template do relatório Vida Nova."""
        try:
            template_path = Path("app/assets/vida_nova_report.md")
            if template_path.exists():
                return template_path.read_text(encoding="utf-8")
            else:
                return "# Template Vida Nova Padrão\n\n1. Análise de Performance\n2. Recomendações\n"
        except Exception as e:
            logger.warning(f"Error reading Vida Nova template content: {str(e)}")
            return "Template Vida Nova Padrão não disponível."

    def _prepare_data(
        self, exam_data: TNMExamData, anamnesis: PatientAnamnesis, kg_data: KGResult
    ) -> dict:
        """Prepara os dados para a geração dos prompts."""
        patient_data = {
            "id": exam_data.patient_id,
            "idade": anamnesis.personal_data.age,
            "gênero": anamnesis.personal_data.gender,
            "peso": anamnesis.personal_data.weight,
            "altura": anamnesis.personal_data.height,
            "imc": anamnesis.personal_data.bmi,
            "atividade_física": anamnesis.context_factors.physical_activity.intensity,
            "objetivo_clínico": anamnesis.objective,
        }

        if hasattr(anamnesis, "diet_type"):
            patient_data["tipo_dieta"] = anamnesis.diet_type
        if hasattr(anamnesis, "energy_level"):
            patient_data["nível_energia"] = anamnesis.energy_level
        if hasattr(anamnesis, "muscle_gain_goal"):
            patient_data["objetivo_massa_muscular"] = anamnesis.muscle_gain_goal
        metabolic_data = {
            "altered_metabs": ", ".join(
                [f"{m.name} ({m.value})" for m in kg_data.metabolite_info]
            ),
            "pathways": ", ".join([p.name for p in kg_data.pathway_impacts])
            if kg_data.pathway_impacts
            else "Nenhuma via afetada detectada",
            "manifestations": ", ".join([m.description for m in kg_data.manifestations])
            if kg_data.manifestations
            else "Nenhuma manifestação registrada",
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

    @staticmethod
    def _build_context_section(section_name: str, data: dict) -> str:
        """Constrói a seção de contexto para os prompts."""
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
                f"Tipo de dieta: {patient.get('tipo_dieta', '')}\n"
                f"Nível de energia: {patient.get('nível_energia', '')}\n"
                f"Objetivo massa muscular: {patient.get('objetivo_massa_muscular', '')}\n"
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

        elif section_name == "vidanova_template":
            return f"# TEMPLATE VIDA NOVA (SIGA RIGOROSAMENTE)\n{data.get('vidanova_template', '')}"

        return (
            f"- Exames: {data.get('exam_data', '')}\n"
            f"- Anamnese: {data.get('anamnesis', '')}\n"
            f"- Achados do grafo de conhecimento: {data.get('kg_data', '')}"
        )

    @staticmethod
    def _generate_prompt(
        prompt_type: str, data: dict, context: dict | None = None
    ) -> tuple[str, str]:
        """Gera um prompt para o tipo especificado."""
        config = PROMPT_CONFIGS.get(prompt_type)
        if not config:
            raise ValueError(f"Prompt type '{prompt_type}' not found in configuration.")

        context_sections = [
            VidaNovaPrompts._build_context_section(section, data)
            for section in config.context_sections
        ]
        if context:
            formatted_context = json.dumps(context, indent=2, ensure_ascii=False)
            context_sections.append(
                f"# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{formatted_context}"
            )

        user_prompt = "\n\n".join(context_sections) + f"\n\n{config.objective}"
        system_prompt = config.system_prompt or BASE_SYSTEM_PROMPT

        return system_prompt, user_prompt

    def get_findings_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Generate the prompt for analysis of clinical findings."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, prompt = VidaNovaPrompts._generate_prompt(
            "findings", data, context
        )
        return system_prompt, safe_encode(prompt)

    def get_supplements_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Generate the prompt for completion."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, prompt = VidaNovaPrompts._generate_prompt(
            "supplements", data, context
        )
        return system_prompt, safe_encode(prompt)

    def get_diet_suggestions_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Generate and returns the system prompt and  prompt for diet suggestions."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, prompt = VidaNovaPrompts._generate_prompt(
            "diet_suggestions", data, context
        )
        return system_prompt, safe_encode(prompt)

    def get_training_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Generate and returns the system prompt and  prompt for workout suggestions."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, prompt = VidaNovaPrompts._generate_prompt(
            "training", data, context
        )
        return system_prompt, safe_encode(prompt)

    def get_summary_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        context: dict | None = None,
    ) -> tuple[str, str]:
        """Generate and returns the system prompt and the  prompt for the exam summary."""
        data = self._prepare_data(exam_data, anamnesis, kg_data)
        system_prompt, prompt = VidaNovaPrompts._generate_prompt(
            "summary", data, context
        )
        return system_prompt, safe_encode(prompt)

    def get_markdown_report_prompt(
        self,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
        final_report_structured_data: dict,
    ) -> tuple[str, str]:
        """Generate and returns the system prompt and the encoded prompt for the final Markdown report."""
        data = {"vidanova_template": VidaNovaPrompts._read_vidanova_template()}

        system_prompt, user_prompt = VidaNovaPrompts._generate_prompt(
            "markdown_report", data, {"final_report": final_report_structured_data}
        )
        return system_prompt, safe_encode(user_prompt)

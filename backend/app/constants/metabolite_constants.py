from app.domain.report import (
    DeficiencyRecommendationSectionWrapper,
    ExamsRecommendationSectionWrapper,
    FindingsSection,
    FoodRecommendationSectionWrapper,
    GeneralGuidelinesContent,
    LifestyleRecommendationSectionWrapper,
    MarkdownReport,
    SummaryContent,
    SupplementRecommendationSectionWrapper,
)
from app.domain.status import MetaboliteStatusEnum

# Configuração de status para metabólitos
METABOLITE_STATUS_CONFIG = {
    MetaboliteStatusEnum.DEFICIT_SEVERO: {
        "cor": "Vermelho",
        "classificacao": "Muito abaixo do Mínimo da Faixa de Referência",
        "score": 1,
        "analise": "Muito desequilibrado",
    },
    MetaboliteStatusEnum.DEFICIT_MODERADO: {
        "cor": "Amarelo",
        "classificacao": "Abaixo do Mínimo da Referência e Dentro do Limite de Alerta",
        "score": 2,
        "analise": "Desequilíbrio",
    },
    MetaboliteStatusEnum.NORMAL: {
        "cor": "Verde",
        "classificacao": "Dentro da Faixa de Referência",
        "score": 3,
        "analise": "Níveis dentro da faixa de referência considerada adequada.",
    },
    MetaboliteStatusEnum.EXCESSO_MODERADO: {
        "cor": "Amarelo",
        "classificacao": "Acima do Máximo da Referência e Dentro do Limite de Alerta",
        "score": 4,
        "analise": "Desequilíbrio",
    },
    MetaboliteStatusEnum.EXCESSO_SEVERO: {
        "cor": "Vermelho",
        "classificacao": "Muito acima do Máximo da Faixa de Referência",
        "score": 5,
        "analise": "Muito desequilibrado",
    },
}

# Mapeamento de status com variarições de entradas
STATUS_MAPPING = {
    "deficit_severo": MetaboliteStatusEnum.DEFICIT_SEVERO,
    "deficit_moderado": MetaboliteStatusEnum.DEFICIT_MODERADO,
    "normal": MetaboliteStatusEnum.NORMAL,
    "excesso_moderado": MetaboliteStatusEnum.EXCESSO_MODERADO,
    "excesso_severo": MetaboliteStatusEnum.EXCESSO_SEVERO,
}

# Constante para seções obrigatórias do relatório
REQUIRED_SECTIONS = [
    "summary",
    "findings",
    "energetics",
    "constructors",
    "regulators",
    "fats",
    "lifestyle",
    "supplements",
    "foods",
    "deficiencies",
    "guidelines",
    "exams",
]

# Seções para schemas Pydantic esperados do LLM
SECTION_SCHEMAS = {
    "summary": SummaryContent,
    "findings": FindingsSection,
    "energetics": FoodRecommendationSectionWrapper,
    "constructors": FoodRecommendationSectionWrapper,
    "regulators": FoodRecommendationSectionWrapper,
    "fats": FoodRecommendationSectionWrapper,
    "lifestyle": LifestyleRecommendationSectionWrapper,
    "supplements": SupplementRecommendationSectionWrapper,
    "foods": FoodRecommendationSectionWrapper,
    "deficiencies": DeficiencyRecommendationSectionWrapper,
    "guidelines": GeneralGuidelinesContent,
    "exams": ExamsRecommendationSectionWrapper,
    "markdown_report": MarkdownReport,
}

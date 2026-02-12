"""Exam configuration for IonNutri exams."""

from typing import Any

from pydantic import BaseModel

from app.domain.exam_configs.base_config import BaseExamConfig
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


class IonNutriConfig(BaseExamConfig):
    """# Configuração de status para metabólitos."""

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

    def get_exam_type(self) -> str:
        """Return exam type."""
        return "ionnutri"

    def get_section_schemas(self) -> dict[str, type[BaseModel]]:
        """Get section schemas for this exam type."""
        return self.SECTION_SCHEMAS.copy()

    def get_formatting_config(self) -> dict[str, Any]:
        """Get formatting rules for IonNutri reports."""
        return {
            "style": "Técnico-científico com linguagem acessível",
            "headers": "Use ## para seções principais e ### para subseções",
            "format": "Markdown com listas • e **negrito** para destaques",
        }

    def get_complete_report_schema(self):
        """Get complete report schema for single-pass generation."""
        return MarkdownReport

    def get_status_mapping(self) -> dict[str, Any]:
        """Get mapping from Ionnutri."""
        return self.STATUS_MAPPING

"""Unit tests for Pydantic schemas and data validation."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from app.domain.report import (
    FindingItem,
    FindingsSection,
    FoodItem,
    IonNutriReport,
    LifestyleItem,
    NutritionalRecs,
    RecommendationsSection,
    SummaryContent,
    SupplementItem,
)
from app.schemas.exam import Metabolite
from app.schemas.patient_anamnesis import (
    AlcoholConsumption,
    PersonalData,
    PhysicalActivity,
    Sleep,
)


def test_metabolite_very_small_value():
    """Testa comportamento com valor numérico muito pequeno."""
    small_value = 0.0000001
    metabolite = Metabolite(name="Teste", value=small_value)
    assert metabolite.value == small_value


def test_metabolite_very_large_value():
    """Testa comportamento com valor numérico muito grande."""
    large_value = 1e10
    metabolite = Metabolite(name="Teste", value=large_value)
    assert metabolite.value == large_value


def test_metabolite_minimum_name_length():
    """Testa comportamento com nome de um caractere (mínimo permitido)."""
    metabolite = Metabolite(name="X", value=1.0)
    assert metabolite.name == "X"


@pytest.mark.parametrize(
    "model_class,valid_data,field,invalid_value,expected_error",
    [
        # PersonalData validações
        (
            PersonalData,
            {"age": 34, "gender": "M", "weight": 70.5, "height": 1.75},
            "age",
            -1,
            "greater than or equal",
        ),
        (
            PersonalData,
            {"age": 34, "gender": "M", "weight": 70.5, "height": 1.75},
            "weight",
            0,
            "greater than",
        ),
        # PhysicalActivity validações
        (
            PhysicalActivity,
            {"frequency": "3", "type": "Aeróbica", "intensity": "Moderada"},
            "frequency",
            None,
            "string_type",
        ),
        # Sleep validações
        (
            Sleep,
            {"quality": "Boa", "hours": 7, "issues": ["Ronco"]},
            "hours",
            -1.0,
            "greater than",
        ),
    ],
)
def test_model_validation_parametrized(
    model_class, valid_data, field, invalid_value, expected_error
):
    """Testa múltiplos cenários de validação com parametrização."""
    # Copia os dados válidos e substitui com valor inválido
    test_data = valid_data.copy()
    test_data[field] = invalid_value

    # Valida que o erro é lançado
    with pytest.raises(ValidationError) as excinfo:
        model_class(**test_data)

    # Valida que o erro contém o campo e a mensagem esperada
    error_str = str(excinfo.value)
    assert field in error_str
    assert expected_error in error_str


def test_nutritional_recs_validation():
    """Testa validação do schema NutritionalRecs."""
    # Criar FoodItem válido para teste
    valid_food = FoodItem(name="Teste", quantity="100g", frequency="1x ao dia")

    # Criar NutritionalRecs com listas vazias (deve ser válido)
    nutritional_recs = NutritionalRecs(
        energetics=[valid_food],
        constructors=[valid_food],
        regulators=[valid_food],
        fats=[valid_food],
    )

    assert len(nutritional_recs.energetics) == 1
    assert len(nutritional_recs.constructors) == 1
    assert len(nutritional_recs.regulators) == 1
    assert len(nutritional_recs.fats) == 1


def test_alcohol_consumption_frequency_coerces_int_to_str():
    """Some payloads send alcohol frequency as an int; accept and coerce to str."""
    alcohol = AlcoholConsumption(frequency=1, amount="1 a 2 vezes na semana")
    assert alcohol.frequency == "1"


def test_report_timestamp():
    """Testa que o timestamp do relatório usa a data atual (dia, mês e ano)."""
    # Criar relatório mínimo válido
    report = IonNutriReport(
        report_id="REP123",
        patient_id="P413",
        anamnesis_id="ANA-P413",
        exam_id="EXM-P413",
        version="1.0",
        timestamp=datetime.now(),
        summary=SummaryContent(content="Teste timestamp"),
        findings=FindingsSection(
            items=[
                FindingItem(
                    status="normal",
                    description="Teste",
                    metabolite="Teste",
                    implications=["Teste"],
                )
            ],
            conclusion="Teste",
        ),
        recommendations=RecommendationsSection(
            nutritional=NutritionalRecs(
                energetics=[
                    FoodItem(name="Carboidrato", quantity="100g", frequency="1x ao dia")
                ],
                constructors=[
                    FoodItem(name="Proteína", quantity="100g", frequency="1x ao dia")
                ],
                regulators=[
                    FoodItem(name="Vegetal", quantity="100g", frequency="1x ao dia")
                ],
                fats=[FoodItem(name="Gordura", quantity="100g", frequency="1x ao dia")],
            ),
            lifestyle=[
                LifestyleItem(
                    category="Teste",
                    description="Teste",
                    rationale="Teste",
                )
            ],
            supplements=[
                SupplementItem(
                    name="Teste",
                    dosage="Teste",
                    frequency="Teste",
                    purpose="Teste",
                )
            ],
        ),
        deficiencies=[],
        general_guidelines="Teste",
        additional_exams=[],
    )

    # Obter data atual
    today = datetime.now()

    # Verificar apenas ano, mês e dia
    assert report.timestamp.year == today.year
    assert report.timestamp.month == today.month
    assert report.timestamp.day == today.day

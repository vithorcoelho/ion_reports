"""Test configuration and fixtures for plugin tests.

This module provides specific fixtures and configuration for plugin tests,
including mock data for VidaNova and IonNutri plugins.
"""

from datetime import date
from decimal import Decimal

import pytest

from app.domain.kg_result import KGResult
from app.plugins.ionnutri_plugin import IonNutriPlugin
from app.schemas.exam import Metabolite, TNMExamData
from app.schemas.patient_anamnesis import (
    AlcoholConsumption,
    ContextFactors,
    Medication,
    PatientAnamnesis,
    PersonalData,
    PhysicalActivity,
    Sleep,
)


@pytest.fixture
def mock_llm_service(mocker):
    """Mock do serviço LLM que retorna uma resposta padrão para todos os prompts."""
    mock_service = mocker.Mock()
    mock_service.call_llm.return_value = {
        "content": {"items": [], "content": "texto simulado"}
    }
    return mock_service


@pytest.fixture
def plugin(mock_llm_service_configured):
    """Instância do plugin com dependência LLM mockada."""
    return IonNutriPlugin(mock_llm_service_configured)


@pytest.fixture
def sample_exam_data_novavida():
    """Fixture that returns a sample TNMExamData object with dummy metabolites."""
    return TNMExamData(
        patient_id="PAC123",
        exam_date=date.today(),
        metabolites=[
            Metabolite(
                name="Creatina",
                value=Decimal("1.2"),
                reference_range="0.6-1.3",
                status="normal",
            )
        ],
    )


@pytest.fixture
def sample_anamnesis_vida_novavida():
    """Fixture that returns a sample PatientAnamnesis with fitness-related data."""
    return PatientAnamnesis(
        patient_id="PAC123",
        date=date.today(),
        objective="Melhorar desempenho físico",
        personal_data=PersonalData(
            age=28, gender="M", weight=75.0, height=1.80, bmi=23.1
        ),
        context_factors=ContextFactors(
            medical_history=["nenhum"],
            intolerances=[],
            physical_activity=PhysicalActivity(
                type="musculação", frequency="5", intensity="alta"
            ),
            sleep=Sleep(quality="boa", hours=7, issues=[]),
            alcohol_consumption=AlcoholConsumption(frequency="0", amount=""),
            medications=[Medication(name="Nenhum", frequency="", dosage=None)],
            stress_level="baixo",
        ),
    )


@pytest.fixture
def sample_kg_result():
    """Fixture that returns an empty KGResult (no findings)."""
    return KGResult(
        metabolite_info=[],
        manifestations=[],
        recommended_interventions=[],
        foods=[],
        supplements=[],
        pathway_impacts=[],
    )

"""Module defining schemas related to patient anamnesis."""

from typing import Annotated, Literal

from pydantic import BaseModel, Discriminator, Field, field_validator


class PersonalData(BaseModel):
    """Model representing patient personal data.

    Attributes:
        age (int): Patient age in years.
        gender (str): Patient gender.
        weight (float): Patient weight in kg.
        height (float): Patient height in meters.
        bmi (float): Body Mass Index (BMI) of the patient.

    """

    age: int = Field(..., ge=0, description="Idade do paciente em anos")
    gender: str = Field(..., description="Gênero do paciente")
    weight: float = Field(..., gt=0, description="Peso do paciente em kg")
    height: float = Field(..., gt=0, description="Altura do paciente em metros")
    bmi: float | None = Field(
        None, description="Índice de Massa Corporal (IMC) do paciente"
    )


class PhysicalActivity(BaseModel):
    """Model representing patient physical activity data.

    Attributes:
        frequency (str): Frequency of physical activity per week (can be numeric or "não informado").
        type (str): Type of physical activity (aerobic, anaerobic, etc.).
        intensity (str): Intensity of physical activity (light, moderate, intense).

    """

    frequency: str = Field(..., description="Frequência da atividade física por semana")
    type: str = Field(
        ..., description="Tipo de atividade física (aeróbica, anaeróbica, etc.)"
    )
    intensity: str = Field(
        ..., description="Intensidade da atividade física (leve, moderada, intensa)"
    )

    @field_validator("frequency", mode="before")
    @classmethod
    def _coerce_frequency_to_str(cls, v):
        # Some JSON sources use numbers for frequency (e.g., 2) while the schema
        # expects a human-readable string. Accept both.
        if v is None:
            return v
        return str(v)


class Sleep(BaseModel):
    """Model representing patient sleep data.

    Attributes:
        quality (str): Sleep quality (good, average, poor).
        hours (float): Hours of sleep per night.
        issues (list[str]): Sleep-related problems.

    """

    quality: str = Field(..., description="Qualidade do sono (boa, média, ruim)")
    hours: float = Field(..., gt=0, description="Horas de sono por noite")
    issues: list[str] = Field(..., description="Problemas relacionados ao sono")


class AlcoholConsumption(BaseModel):
    """Model representing patient alcohol consumption data.

    Attributes:
        frequency (str): Frequency of alcohol consumption per week (can be numeric or "não informado").
        amount (str): Amount of alcohol consumed.

    """

    frequency: str = Field(
        ..., description="Frequência do consumo de álcool por semana"
    )
    amount: str = Field(..., description="Quantidade de álcool consumida")

    @field_validator("frequency", mode="before")
    @classmethod
    def _coerce_frequency_to_str(cls, v):
        # Some payloads (e.g., arquivos_json/ion_nutri/*.json) provide frequency as
        # an integer option index. Coerce it to string to keep the API permissive.
        if v is None:
            return v
        return str(v)


class Medication(BaseModel):
    """Model representing patient medications.

    Attributes:
        name (str): Medication name.
        frequency (str): Medication usage frequency.
        dosage (str | None): Medication dosage.

    """

    name: str = Field(..., description="Nome do medicamento")
    frequency: str = Field(..., description="Frequência de uso do medicamento")
    dosage: str | None = Field(..., description="Dosagem do medicamento")


class ContextFactors(BaseModel):
    """Model representing patient contextual factors.

    Attributes:
        medical_history (list[str]): Patient medical history.
        intolerances (list[str]): Patient intolerances.
        physical_activity (PhysicalActivity): Physical activity data.
        sleep (Sleep): Sleep data.
        alcohol_consumption (AlcoholConsumption): Alcohol consumption data.
        medications (list[Medication]): List of patient medications.
        stress_level (str): Patient stress level.

    """

    medical_history: list[str] = Field(..., description="Histórico médico do paciente")
    intolerances: list[str] = Field(..., description="Intolerâncias do paciente")
    physical_activity: PhysicalActivity = Field(
        ..., description="Dados de atividade física do paciente"
    )
    sleep: Sleep = Field(..., description="Dados de sono do paciente")
    alcohol_consumption: AlcoholConsumption = Field(
        ..., description="Dados de consumo de álcool do paciente"
    )
    medications: list[Medication] = Field(
        ..., description="Lista de medicamentos do paciente"
    )
    stress_level: str = Field(..., description="Nível de estresse do paciente")


class PatientAnamnesis(BaseModel):
    """Base model for common fields across all anamnesis types.

    Attributes:
        patient_id (str): Patient identifier.
        objective (str): Patient objective or goal.
        personal_data (PersonalData): Patient personal data.
        context_factors (ContextFactors): Patient contextual factors.

    """

    patient_id: str = Field(..., description="ID do paciente")
    objective: str = Field(..., description="Objetivo do paciente")
    personal_data: PersonalData = Field(..., description="Dados pessoais do paciente")
    context_factors: ContextFactors = Field(
        ..., description="Fatores contextuais do paciente"
    )


class IonNutriAnamnesis(PatientAnamnesis):
    """Specific anamnesis model for 'ionnutri' type.

    Includes all fields from PatientAnamnesis plus specific fields
    for IonNutri assessments.

    Attributes:
        anamnesis_type (Literal["ionnutri"]): Anamnesis type identifier.

    """

    anamnesis_type: Literal["ionnutri"] = "ionnutri"
    family_history: dict = Field(..., description="Histórico familiar")
    environmental_exposure: dict = Field(..., description="Exposições ambientais")
    # ... outros campos específicos


class VidaNovaAnamnesis(PatientAnamnesis):
    """Modelo de anamnese específica para o tipo 'vidanova'.

    Inclui todos os campos da BaseAnamnesis e seus campos específicos.
    """

    anamnesis_type: Literal["vidanova"] = "vidanova"
    diet_type: str = Field(..., description="Tipo de dieta")
    energy_level: str = Field(..., description="Nível de energia")
    muscle_gain_goal: str = Field(..., description="Objetivo de ganho muscular")
    nutritionist_plan: str = Field(
        ..., description="Segue plano alimentar orientado por nutricionista"
    )
    difficulty_muscle_gain: str = Field(
        ..., description="Sente dificuldade em ganhar massa muscular"
    )


AnamnesisUnion = Annotated[
    IonNutriAnamnesis | VidaNovaAnamnesis, Discriminator("anamnesis_type")
]

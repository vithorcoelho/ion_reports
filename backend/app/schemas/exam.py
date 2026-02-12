"""Medical examination data schemas.

This module defines Pydantic models for representing medical examination data,
particularly TNM (nutrimetabolomic) exam results including metabolite measurements
and related metadata.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class Metabolite(BaseModel):
    """Model representing a metabolite measurement.

    Attributes:
        name (str): Name of the metabolite.
        value (float): Measured value of the metabolite.

    """

    name: str = Field(..., min_length=1, description="Nome do metabólito")
    value: float = Field(..., gt=0, description="Valor do metabólito")


class TNMExamData(BaseModel):
    """Model representing TNM (nutrimetabolomic) examination data.

    Attributes:
        patient_id (str): Patient identifier.
        exam_date (datetime): Date when the examination was performed.
        metabolites (list[Metabolite]): List of metabolite measurements.

    """

    patient_id: str = Field(..., description="ID do paciente")
    exam_date: datetime = Field(..., description="Data do exame")
    metabolites: list[Metabolite] = Field(
        ..., min_length=1, description="Lista de metabólitos"
    )

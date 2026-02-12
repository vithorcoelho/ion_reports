from enum import Enum


class MetaboliteStatusEnum(Enum):
    """Enum to represent the classification system for metabolite status."""

    DEFICIT_SEVERO = 1  # VAB
    DEFICIT_MODERADO = 2  # AAB
    NORMAL = 3  # E
    EXCESSO_MODERADO = 4  # AAC
    EXCESSO_SEVERO = 5  # VAC

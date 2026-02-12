"""Base definitions for exam configuration interfaces."""

from app.domain.exam_configs.base_config import BaseExamConfig
from app.domain.exam_configs.ionnutri_config import IonNutriConfig
from app.domain.exam_configs.vidanova_config import VidaNovaConfig

EXAM_CONFIGS: dict[str, BaseExamConfig] = {
    "ionnutri": IonNutriConfig(),
    "vidanova": VidaNovaConfig(),
}

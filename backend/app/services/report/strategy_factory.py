"""Factory for creating report strategies based on exam type and strategy type."""

from app.domain.exam_configs.ionnutri_config import IonNutriConfig
from app.domain.exam_configs.vidanova_config import VidaNovaConfig
from app.services.report.multistage_strategy import MultiStageReportStrategy
from app.services.report.onestage_strategy import OneStageReportStrategy


class StrategyFactory:
    """Factory for creating report generation strategies."""

    def __init__(self):
        """Initialize strategy factory."""
        self.exam_configs = {"ionnutri": IonNutriConfig(), "vidanova": VidaNovaConfig()}
        self.strategy_classes = {
            "multistage": MultiStageReportStrategy,
            "onestage": OneStageReportStrategy,
        }

    def create_strategy(self, exam_type: str, strategy_type: str, services: dict):
        """Create a report strategy instance."""
        exam_config = self.exam_configs[exam_type]
        strategy_class = self.strategy_classes[strategy_type]
        return strategy_class(exam_config=exam_config, services=services)

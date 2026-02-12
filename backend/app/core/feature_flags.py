"""Feature flags for functionality control."""

from functools import lru_cache

from pydantic_settings import BaseSettings


class FeatureFlags(BaseSettings):
    """Feature flags for functionality control."""

    # Report Generation Mode
    # True = Strategy Pattern, False = Plugins (default)
    use_strategy_pattern: bool = False

    class Config:
        """Configuration for FeatureFlags."""

        env_file = ".env"
        env_prefix = "FEATURE_"
        case_sensitive = False
        extra = "allow"  # Allow extra environment variables


@lru_cache
def get_feature_flags() -> FeatureFlags:
    """Singleton for feature flags (cached)."""
    return FeatureFlags()

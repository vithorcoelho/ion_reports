import os
import tomllib
from datetime import datetime
from pathlib import Path
from typing import Any


class VersionInfo:
    """Handles version information for the application."""

    def __init__(self):
        self._version: str | None = None
        self._build_info: dict[str, Any] = {}
        self._load_version_info()

    def _load_version_info(self) -> None:
        """Load version information from pyproject.toml and environment variables."""
        try:
            # Try to read from pyproject.toml
            project_root = Path(__file__).parent.parent.parent
            pyproject_path = project_root / "pyproject.toml"

            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    pyproject_data = tomllib.load(f)
                    self._version = pyproject_data.get("project", {}).get("version")
        except Exception:
            # Fallback to hardcoded version if pyproject.toml is not accessible
            self._version = "0.1.0"

        # Allow version override via environment variable
        env_version = os.getenv("APP_VERSION")
        if env_version:
            self._version = env_version

        # Build additional metadata
        self._build_info = {
            "version": self._version,
            "build_time": os.getenv("BUILD_TIME", datetime.now().isoformat()),
            "git_commit": os.getenv("GIT_COMMIT", "unknown"),
            "git_branch": os.getenv("GIT_BRANCH", "unknown"),
            "build_number": os.getenv("BUILD_NUMBER", "local"),
            "environment": os.getenv("ENVIRONMENT", "development"),
        }

    @property
    def version(self) -> str:
        """Get the application version."""
        return self._version or "unknown"

    @property
    def build_info(self) -> dict[str, Any]:
        """Get complete build information."""
        return self._build_info.copy()

    def to_dict(self) -> dict[str, Any]:
        """Return version info as dictionary."""
        return self.build_info


# Global version instance
version_info = VersionInfo()


def get_version() -> str:
    """Get the current application version."""
    return version_info.version


def get_build_info() -> dict[str, Any]:
    """Get complete build information."""
    return version_info.build_info

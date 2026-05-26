"""Runtime configuration for the AI Abuse Intelligence Lab."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Small immutable configuration object loaded from environment variables."""

    environment: str = "development"
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> AppConfig:
        """Build configuration from process environment variables."""

        return cls(
            environment=os.getenv("AI_ABUSE_INTEL_ENV", "development"),
            log_level=os.getenv("AI_ABUSE_INTEL_LOG_LEVEL", "INFO"),
        )

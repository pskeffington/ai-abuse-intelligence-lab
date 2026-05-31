"""Small analysis pipeline for combining independent findings."""

from __future__ import annotations

from dataclasses import dataclass

from ai_abuse_intel_lab.analysis.burst import BurstSignalAnalyzer
from ai_abuse_intel_lab.analysis.coordination import CoordinationSignalAnalyzer
from ai_abuse_intel_lab.models import AbuseEvent, Finding


@dataclass(frozen=True)
class AnalysisPipelineConfig:
    """Configuration for the baseline analysis pipeline."""

    repeated_minimum_count: int = 2
    timing_window_minutes: int = 10
    timing_minimum_count: int = 3


class AnalysisPipeline:
    """Run baseline analyzers and return a combined finding list."""

    def __init__(self, config: AnalysisPipelineConfig | None = None) -> None:
        self.config = config or AnalysisPipelineConfig()

    def run(self, events: list[AbuseEvent]) -> list[Finding]:
        """Run all baseline analyzers in a stable order."""

        repeated_analyzer = CoordinationSignalAnalyzer(
            minimum_count=self.config.repeated_minimum_count
        )
        timing_analyzer = BurstSignalAnalyzer(
            window_minutes=self.config.timing_window_minutes,
            minimum_count=self.config.timing_minimum_count,
        )

        findings: list[Finding] = []
        findings.extend(repeated_analyzer.analyze(events))
        findings.extend(timing_analyzer.analyze(events))
        return findings

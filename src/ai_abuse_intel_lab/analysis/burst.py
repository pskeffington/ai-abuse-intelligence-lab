"""Time-window burst detection for normalized events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

from ai_abuse_intel_lab.models import AbuseEvent, ConfidenceLevel, Finding


@dataclass(frozen=True)
class BurstWindow:
    """Detected event concentration inside a fixed time window."""

    start_event_id: str
    start_iso: str
    end_iso: str
    event_count: int
    event_ids: tuple[str, ...]


class BurstSignalAnalyzer:
    """Detect concentrated activity within a rolling time window."""

    def __init__(self, window_minutes: int = 10, minimum_count: int = 3) -> None:
        if window_minutes < 1:
            raise ValueError("window_minutes must be at least 1")
        if minimum_count < 2:
            raise ValueError("minimum_count must be at least 2")
        self.window = timedelta(minutes=window_minutes)
        self.minimum_count = minimum_count

    def detect_windows(self, events: list[AbuseEvent]) -> list[BurstWindow]:
        """Return non-duplicate burst windows from sorted events."""

        ordered_events = sorted(events, key=lambda event: event.observed_at)
        windows: list[BurstWindow] = []
        seen_event_sets: set[tuple[str, ...]] = set()

        for index, start_event in enumerate(ordered_events):
            window_end = start_event.observed_at + self.window
            events_in_window = [
                event
                for event in ordered_events[index:]
                if start_event.observed_at <= event.observed_at <= window_end
            ]
            if len(events_in_window) < self.minimum_count:
                continue

            event_ids = tuple(event.event_id for event in events_in_window)
            if event_ids in seen_event_sets:
                continue
            seen_event_sets.add(event_ids)
            windows.append(
                BurstWindow(
                    start_event_id=start_event.event_id,
                    start_iso=start_event.observed_at.isoformat(),
                    end_iso=events_in_window[-1].observed_at.isoformat(),
                    event_count=len(events_in_window),
                    event_ids=event_ids,
                )
            )

        return windows

    def analyze(self, events: list[AbuseEvent]) -> list[Finding]:
        """Return analyst findings for detected burst windows."""

        findings: list[Finding] = []
        for window in self.detect_windows(events):
            findings.append(
                Finding(
                    title="Event burst detected",
                    summary=(
                        f"{window.event_count} events occurred between "
                        f"{window.start_iso} and {window.end_iso}."
                    ),
                    confidence=ConfidenceLevel.LOW,
                    related_event_ids=list(window.event_ids),
                    tags=["burst", "timing"],
                )
            )
        return findings

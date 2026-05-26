"""CSV ingestion for first-run sample data and local analyst exports."""

from __future__ import annotations

from collections.abc import Hashable
from datetime import datetime
from pathlib import Path

import pandas as pd

from ai_abuse_intel_lab.models import AbuseEvent, Actor, Artifact, EventType, SourceRef


class CsvEventLoader:
    """Load normalized abuse events from a CSV file."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[AbuseEvent]:
        """Read the CSV file and return validated event objects."""

        frame = pd.read_csv(self.path)
        rows = [self._normalize_row(row) for row in frame.to_dict(orient="records")]
        return [self._row_to_event(row) for row in rows]

    def _row_to_event(self, row: dict[str, object]) -> AbuseEvent:
        """Convert a flat row into a normalized event."""

        source = SourceRef(name=str(row.get("source_name", "local_csv")))
        actor = Actor(
            handle=self._optional_str(row.get("actor_handle")),
            platform=self._optional_str(row.get("platform")),
        )
        artifact = Artifact(
            artifact_type=str(row.get("artifact_type", "text")),
            value=str(row.get("artifact_value", "")),
        )
        tags = [tag.strip() for tag in str(row.get("tags", "")).split(";") if tag.strip()]

        return AbuseEvent(
            event_type=EventType(str(row.get("event_type", EventType.CONTENT_POST.value))),
            observed_at=datetime.fromisoformat(str(row["observed_at"])),
            source=source,
            actor=actor,
            artifact=artifact,
            tags=tags,
            narrative=str(row.get("narrative", "")),
        )

    @staticmethod
    def _normalize_row(row: dict[Hashable, object]) -> dict[str, object]:
        """Convert pandas row dictionaries to string-keyed dictionaries."""

        return {str(key): value for key, value in row.items()}

    @staticmethod
    def _optional_str(value: object) -> str | None:
        """Return a stripped string or None for empty CSV values."""

        if value is None:
            return None
        text = str(value).strip()
        return text or None

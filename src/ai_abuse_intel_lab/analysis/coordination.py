"""Simple coordination-signal analysis primitives."""

from __future__ import annotations

from collections import Counter

from ai_abuse_intel_lab.models import AbuseEvent, ConfidenceLevel, Finding


class CoordinationSignalAnalyzer:
    """Detect repeated tags and actors across a batch of events."""

    def __init__(self, minimum_count: int = 2) -> None:
        if minimum_count < 2:
            raise ValueError("minimum_count must be at least 2")
        self.minimum_count = minimum_count

    def analyze(self, events: list[AbuseEvent]) -> list[Finding]:
        """Return findings for repeated tags and actor handles."""

        findings: list[Finding] = []
        findings.extend(self._tag_findings(events))
        findings.extend(self._actor_findings(events))
        return findings

    def _tag_findings(self, events: list[AbuseEvent]) -> list[Finding]:
        tag_counts = Counter(tag for event in events for tag in event.tags)
        return [
            Finding(
                title=f"Repeated tag: {tag}",
                summary=f"Tag '{tag}' appears in {count} events.",
                confidence=ConfidenceLevel.LOW,
                related_event_ids=[event.event_id for event in events if tag in event.tags],
                tags=["coordination", "repetition", tag],
            )
            for tag, count in tag_counts.items()
            if count >= self.minimum_count
        ]

    def _actor_findings(self, events: list[AbuseEvent]) -> list[Finding]:
        handles = [event.actor.handle for event in events if event.actor and event.actor.handle]
        actor_counts = Counter(handles)
        return [
            Finding(
                title=f"Repeated actor: {handle}",
                summary=f"Actor '{handle}' appears in {count} events.",
                confidence=ConfidenceLevel.LOW,
                related_event_ids=[
                    event.event_id
                    for event in events
                    if event.actor and event.actor.handle == handle
                ],
                tags=["coordination", "actor", handle],
            )
            for handle, count in actor_counts.items()
            if count >= self.minimum_count
        ]

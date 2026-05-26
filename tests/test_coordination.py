from datetime import UTC, datetime

from ai_abuse_intel_lab.analysis import CoordinationSignalAnalyzer
from ai_abuse_intel_lab.models import AbuseEvent, Actor, EventType, SourceRef


def test_coordination_analyzer_finds_repeated_tags_and_actor() -> None:
    source = SourceRef(name="test")
    events = [
        AbuseEvent(
            event_type=EventType.CONTENT_POST,
            observed_at=datetime.now(UTC),
            source=source,
            actor=Actor(handle="@alpha", platform="example"),
            tags=["shared"],
        ),
        AbuseEvent(
            event_type=EventType.CONTENT_POST,
            observed_at=datetime.now(UTC),
            source=source,
            actor=Actor(handle="@alpha", platform="example"),
            tags=["shared"],
        ),
    ]

    findings = CoordinationSignalAnalyzer().analyze(events)

    titles = {finding.title for finding in findings}
    assert "Repeated tag: shared" in titles
    assert "Repeated actor: @alpha" in titles

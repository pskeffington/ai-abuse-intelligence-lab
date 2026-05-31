from pathlib import Path

from ai_abuse_intel_lab.analysis import BurstSignalAnalyzer
from ai_abuse_intel_lab.ingestion import CsvEventLoader


def test_burst_signal_analyzer_detects_sample_time_cluster() -> None:
    events = CsvEventLoader(Path("examples/sample_events.csv")).load()
    analyzer = BurstSignalAnalyzer(window_minutes=5, minimum_count=3)

    windows = analyzer.detect_windows(events)
    findings = analyzer.analyze(events)

    assert len(windows) == 1
    assert windows[0].event_count == 3
    assert len(findings) == 1
    assert findings[0].title == "Event burst detected"
    assert findings[0].related_event_ids == list(windows[0].event_ids)


def test_burst_signal_analyzer_rejects_invalid_parameters() -> None:
    try:
        BurstSignalAnalyzer(window_minutes=0)
    except ValueError as exc:
        assert "window_minutes" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid window")

    try:
        BurstSignalAnalyzer(minimum_count=1)
    except ValueError as exc:
        assert "minimum_count" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid minimum_count")

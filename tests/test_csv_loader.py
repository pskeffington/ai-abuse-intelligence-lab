from pathlib import Path

from ai_abuse_intel_lab.ingestion import CsvEventLoader


def test_csv_loader_reads_sample_events() -> None:
    events = CsvEventLoader(Path("examples/sample_events.csv")).load()

    assert len(events) == 3
    assert events[0].source.name == "synthetic_sample"
    assert "claim-a" in events[0].tags

import json
from pathlib import Path

from ai_abuse_intel_lab.analysis import AnalysisPipeline, AnalysisPipelineConfig
from ai_abuse_intel_lab.ingestion import CsvEventLoader
from ai_abuse_intel_lab.reporting import JsonFindingReporter


def test_json_finding_reporter_renders_machine_readable_payload() -> None:
    events = CsvEventLoader(Path("examples/sample_events.csv")).load()
    findings = AnalysisPipeline(
        AnalysisPipelineConfig(
            repeated_minimum_count=2,
            timing_window_minutes=5,
            timing_minimum_count=3,
        )
    ).run(events)

    rendered = JsonFindingReporter().render(findings)
    payload = json.loads(rendered)

    assert payload["finding_count"] == 4
    assert len(payload["findings"]) == 4
    assert payload["findings"][0]["title"] == "Repeated tag: claim-a"

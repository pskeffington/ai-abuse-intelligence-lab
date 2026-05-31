from pathlib import Path

from ai_abuse_intel_lab.analysis import AnalysisPipeline, AnalysisPipelineConfig
from ai_abuse_intel_lab.ingestion import CsvEventLoader


def test_analysis_pipeline_combines_repeated_and_timing_findings() -> None:
    events = CsvEventLoader(Path("examples/sample_events.csv")).load()
    pipeline = AnalysisPipeline(
        AnalysisPipelineConfig(
            repeated_minimum_count=2,
            timing_window_minutes=5,
            timing_minimum_count=3,
        )
    )

    findings = pipeline.run(events)
    titles = [finding.title for finding in findings]

    assert "Repeated tag: claim-a" in titles
    assert "Repeated tag: synthetic" in titles
    assert "Repeated actor: @alpha" in titles
    assert "Event burst detected" in titles

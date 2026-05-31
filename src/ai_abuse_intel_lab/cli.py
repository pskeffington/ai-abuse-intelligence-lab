"""Command line interface for the AI Abuse Intelligence Lab."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from ai_abuse_intel_lab.analysis import (
    AnalysisPipeline,
    AnalysisPipelineConfig,
    BurstSignalAnalyzer,
    CoordinationSignalAnalyzer,
    EventGraphBuilder,
)
from ai_abuse_intel_lab.config import AppConfig
from ai_abuse_intel_lab.ingestion import CsvEventLoader
from ai_abuse_intel_lab.reporting import MarkdownFindingReporter

app = typer.Typer(help="Defensive AI abuse intelligence analysis toolkit.")
console = Console()


@app.command()
def info() -> None:
    """Print runtime configuration."""

    config = AppConfig.from_env()
    console.print(f"Environment: {config.environment}")
    console.print(f"Log level: {config.log_level}")


@app.command()
def report(
    path: Path,
    repeated_minimum_count: int = 2,
    timing_window_minutes: int = 10,
    timing_minimum_count: int = 3,
) -> None:
    """Load a CSV file and print the combined baseline report."""

    events = CsvEventLoader(path).load()
    pipeline = AnalysisPipeline(
        AnalysisPipelineConfig(
            repeated_minimum_count=repeated_minimum_count,
            timing_window_minutes=timing_window_minutes,
            timing_minimum_count=timing_minimum_count,
        )
    )
    findings = pipeline.run(events)
    reporter = MarkdownFindingReporter()
    console.print(reporter.render(findings))


@app.command()
def analyze_csv(path: Path, minimum_count: int = 2) -> None:
    """Load a CSV file, run repeated-signal analysis, and print Markdown findings."""

    loader = CsvEventLoader(path)
    events = loader.load()
    analyzer = CoordinationSignalAnalyzer(minimum_count=minimum_count)
    findings = analyzer.analyze(events)
    reporter = MarkdownFindingReporter()
    console.print(reporter.render(findings))


@app.command()
def burst_report(path: Path, window_minutes: int = 10, minimum_count: int = 3) -> None:
    """Load a CSV file and print timing findings."""

    events = CsvEventLoader(path).load()
    analyzer = BurstSignalAnalyzer(window_minutes=window_minutes, minimum_count=minimum_count)
    findings = analyzer.analyze(events)
    reporter = MarkdownFindingReporter()
    console.print(reporter.render(findings))


@app.command()
def graph_summary(path: Path) -> None:
    """Load a CSV file and print actor-artifact-event graph metrics."""

    events = CsvEventLoader(path).load()
    builder = EventGraphBuilder()
    graph = builder.build(events)
    summary = builder.summarize(graph)

    console.print("# Graph Summary")
    console.print(f"Nodes: {summary.node_count}")
    console.print(f"Edges: {summary.edge_count}")
    console.print(f"Connected components: {summary.connected_component_count}")
    console.print(f"Largest component size: {summary.largest_component_size}")


if __name__ == "__main__":
    app()

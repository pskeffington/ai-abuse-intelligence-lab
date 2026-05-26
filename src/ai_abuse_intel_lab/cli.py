"""Command line interface for the AI Abuse Intelligence Lab."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from ai_abuse_intel_lab.analysis import CoordinationSignalAnalyzer
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
def analyze_csv(path: Path, minimum_count: int = 2) -> None:
    """Load a CSV file, run baseline analysis, and print Markdown findings."""

    loader = CsvEventLoader(path)
    events = loader.load()
    analyzer = CoordinationSignalAnalyzer(minimum_count=minimum_count)
    findings = analyzer.analyze(events)
    reporter = MarkdownFindingReporter()
    console.print(reporter.render(findings))


if __name__ == "__main__":
    app()

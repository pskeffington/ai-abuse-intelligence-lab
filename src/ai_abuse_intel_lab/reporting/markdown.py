"""Markdown reporting helpers for analyst-facing findings."""

from __future__ import annotations

from ai_abuse_intel_lab.models import Finding


class MarkdownFindingReporter:
    """Render findings into compact Markdown."""

    def render(self, findings: list[Finding]) -> str:
        """Render a complete Markdown report."""

        if not findings:
            return "# Findings\n\nNo findings generated.\n"

        sections = ["# Findings", ""]
        for finding in findings:
            sections.extend(
                [
                    f"## {finding.title}",
                    "",
                    finding.summary,
                    "",
                    f"Confidence: {finding.confidence.value}",
                    f"Related events: {len(finding.related_event_ids)}",
                    "",
                ]
            )
        return "\n".join(sections)

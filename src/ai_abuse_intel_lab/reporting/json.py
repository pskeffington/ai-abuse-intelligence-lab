"""JSON reporting helpers for findings."""

from __future__ import annotations

import json
from typing import Any

from ai_abuse_intel_lab.models import Finding


class JsonFindingReporter:
    """Render findings into deterministic JSON."""

    def render(self, findings: list[Finding]) -> str:
        """Render findings as a JSON document."""

        payload: dict[str, Any] = {
            "finding_count": len(findings),
            "findings": [finding.model_dump(mode="json") for finding in findings],
        }
        return json.dumps(payload, indent=2, sort_keys=True)

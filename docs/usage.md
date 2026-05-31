# Usage

This project currently supports local CSV-based analysis using synthetic or authorized event data.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## Run quality checks

```bash
ruff check .
mypy src
pytest
```

## Generate a combined report

Markdown output:

```bash
python -m ai_abuse_intel_lab report examples/sample_events.csv --timing-window-minutes 5 --timing-minimum-count 3
```

JSON output:

```bash
python -m ai_abuse_intel_lab report examples/sample_events.csv --timing-window-minutes 5 --timing-minimum-count 3 --output-format json
```

## Run individual analyzers

Repeated-signal findings:

```bash
python -m ai_abuse_intel_lab analyze-csv examples/sample_events.csv
```

Timing findings:

```bash
python -m ai_abuse_intel_lab burst-report examples/sample_events.csv --window-minutes 5 --minimum-count 3
```

Graph metrics:

```bash
python -m ai_abuse_intel_lab graph-summary examples/sample_events.csv
```

## Interpretation

Outputs are review signals. They are not attribution claims, intent findings, or proof of coordinated behavior. Findings should be reviewed with source context, provenance, and independent corroboration.

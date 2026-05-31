# Examples

This directory contains synthetic fixtures for development, tests, and documentation.

## Files

- `sample_events.csv`: small synthetic event dataset used by unit tests and CLI examples.

## Run examples

Combined Markdown report:

```bash
python -m ai_abuse_intel_lab report examples/sample_events.csv --timing-window-minutes 5 --timing-minimum-count 3
```

Combined JSON report:

```bash
python -m ai_abuse_intel_lab report examples/sample_events.csv --timing-window-minutes 5 --timing-minimum-count 3 --output-format json
```

Graph summary:

```bash
python -m ai_abuse_intel_lab graph-summary examples/sample_events.csv
```

## Fixture policy

Examples should remain synthetic, minimal, and safe to publish. Do not add real private platform data, secrets, credentials, cookies, private messages, or sensitive investigative notes.

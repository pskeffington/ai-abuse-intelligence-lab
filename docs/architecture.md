# Architecture

The lab is organized around small object-oriented components with narrow responsibilities.

## Layers

### Domain models

`ai_abuse_intel_lab.models` defines the typed objects shared by the system:

- `SourceRef` stores provenance.
- `Actor` stores observed entity metadata.
- `Artifact` stores content or technical objects.
- `AbuseEvent` stores normalized observations.
- `Finding` stores analyst-facing assessments.

### Ingestion

Ingestion classes translate external files or feeds into validated domain objects. The first adapter is `CsvEventLoader`, which supports local CSV files for reproducible development.

### Analysis

Analysis classes consume normalized events and return findings. The first analyzer is intentionally simple and detects repeated tags and actor handles.

### Reporting

Reporting classes render findings for analysts. The first reporter emits Markdown.

## Near-term design targets

- Keep every detector as a small class with one clear purpose.
- Preserve source provenance on every event.
- Separate collection, normalization, analysis, and reporting.
- Avoid storing sensitive raw data in the repository.
- Prefer reproducible fixtures and synthetic examples for tests.

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

Analysis classes consume normalized events and return findings. Current analysis components include:

- `CoordinationSignalAnalyzer`, which detects repeated tags and actor handles.
- `BurstSignalAnalyzer`, which detects concentrated timing inside a rolling window.
- `EventGraphBuilder`, which builds an actor-artifact-event graph and returns compact graph metrics.

### Reporting

Reporting classes render findings for analysts. The first reporter emits Markdown.

## Timing model

The timing detector sorts events by observation time, evaluates rolling windows, and emits low-confidence review findings when at least a configured number of events occur inside the configured window.

## Graph model

The event graph is undirected and connects each event node to any observed actor, artifact, and tag nodes. This keeps graph construction simple while allowing later metrics such as centrality, shared artifacts, common tags, and connected components.

Node identifiers use stable prefixes:

- `event:<event_id>`
- `actor:<handle>`
- `artifact:<artifact_value>`
- `tag:<tag>`

## Near-term design targets

- Keep every detector as a small class with one clear purpose.
- Preserve source provenance on every event.
- Separate collection, normalization, analysis, and reporting.
- Avoid storing sensitive raw data in the repository.
- Prefer reproducible fixtures and synthetic examples for tests.

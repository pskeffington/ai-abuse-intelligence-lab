# Methods

The current release provides a minimal, reproducible analysis baseline for structured event data.

## Event normalization

Input rows are converted into typed `AbuseEvent` objects. Each event may include source metadata, an observed actor, an artifact, tags, a timestamp, and a narrative note.

## Repeated-signal analysis

`CoordinationSignalAnalyzer` counts repeated tags and actor handles across a batch of events. If a tag or actor reaches the configured minimum count, the analyzer emits a low-confidence finding.

Repeated values are treated as review indicators only. They may reflect ordinary repetition, data collection bias, duplicate records, platform norms, or shared external events.

## Timing analysis

`BurstSignalAnalyzer` sorts events by timestamp and evaluates rolling time windows. If at least the configured number of events occur within a window, the analyzer emits a low-confidence timing finding.

Timing concentration is a review indicator only. It does not establish intent, automation, or coordination.

## Graph construction

`EventGraphBuilder` creates an undirected graph that connects event nodes to actor, artifact, and tag nodes. The first graph summary reports node count, edge count, connected component count, and largest component size.

## Combined pipeline

`AnalysisPipeline` runs the repeated-signal analyzer and timing analyzer in a stable order and returns a combined list of findings. Findings can be rendered as Markdown for human review or JSON for downstream tooling.

## Confidence

Initial findings use conservative confidence labels. Current analyzers produce low-confidence review signals unless later evidence and methods justify stronger assessment logic.

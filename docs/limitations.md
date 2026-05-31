# Limitations

This project generates structured review signals from normalized event data. It does not make final determinations about identity, intent, attribution, or harm.

## Current limitations

- CSV ingestion is the only supported input path.
- Current analysis methods are intentionally simple.
- Repeated tags or actor handles may reflect duplicates, collection bias, ordinary platform behavior, or analyst preprocessing choices.
- Timing concentration may reflect news cycles, scheduled events, sampling windows, or other benign causes.
- Graph metrics are descriptive and do not establish causation.
- Confidence labels are conservative and should not be treated as final analytic judgments.

## False positives

False positives are expected. Findings should be reviewed with source context, provenance, and independent corroboration.

## False negatives

The absence of findings does not imply the absence of abuse, manipulation, or coordinated behavior. The current methods only evaluate narrow signals present in the supplied data.

## Human review requirement

Analyst review is required before using any finding in a report, escalation, publication, or operational decision.

## Data quality

Input quality strongly affects output quality. Missing timestamps, inconsistent tags, duplicate rows, and mixed source contexts can distort results.

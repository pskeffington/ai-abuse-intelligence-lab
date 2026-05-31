# Data Schema

The first release supports CSV input with one row per normalized event.

## Required columns

| Column | Type | Description |
| --- | --- | --- |
| `observed_at` | ISO 8601 datetime | Timestamp for the observation. Time zone offsets are recommended. |
| `event_type` | string | One of the supported event type values. |
| `source_name` | string | Name of the dataset, source, or collection context. |

## Optional columns

| Column | Type | Description |
| --- | --- | --- |
| `actor_handle` | string | Observed handle or actor label. Use redacted or synthetic values when appropriate. |
| `platform` | string | Platform, system, or collection context. |
| `artifact_type` | string | Type of artifact, such as `text`, `url`, `media`, or `hash`. |
| `artifact_value` | string | Artifact value or redacted artifact label. |
| `tags` | semicolon-delimited string | Analyst or preprocessing tags, such as `claim-a;synthetic`. |
| `narrative` | string | Short observation note. |

## Supported event types

Current event type values are defined in `EventType`:

| Value | Meaning |
| --- | --- |
| `content_post` | Content or post observation. |
| `account_action` | Account-level action. |
| `coordination_signal` | Review signal from analysis or analyst tagging. |
| `model_output` | Model-generated output observation. |
| `platform_report` | Platform or moderation report. |
| `external_reference` | External supporting reference. |

## Example

```csv
observed_at,event_type,source_name,actor_handle,platform,artifact_type,artifact_value,tags,narrative
2026-05-01T12:00:00+00:00,content_post,synthetic_sample,@alpha,example,text,Repeated claim A,claim-a;synthetic,Sample defensive test event.
```

## Data handling

Prefer synthetic examples for tests and documentation. Do not commit raw private data, credentials, cookies, tokens, private messages, or sensitive investigative notes.

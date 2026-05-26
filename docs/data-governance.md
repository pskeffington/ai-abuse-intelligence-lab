# Data Governance

This repository should be safe for public defensive research. Treat raw platform data, personal data, credentials, private messages, and sensitive investigative notes as out of scope for version control.

## Data handling rules

- Use synthetic fixtures for examples and tests.
- Keep raw data in local ignored directories such as `data/raw/` or `data/sensitive/`.
- Strip direct identifiers whenever possible before analysis.
- Preserve provenance fields for every observation.
- Record uncertainty and confidence rather than overstating conclusions.
- Do not commit secrets, tokens, cookies, API keys, private exports, or account-level data.

## Analyst notes

Analyst notes should distinguish between observation, inference, and assessment. A repeated tag or actor is a signal for review, not a final attribution.

## Prohibited project uses

Do not add workflows intended to support impersonation, evasion, harassment, credential misuse, unauthorized access, or automated platform manipulation.

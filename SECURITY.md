# Security Policy

## Supported versions

The project is pre-release. Security fixes are applied to the `main` branch until versioned releases begin.

## Reporting a vulnerability

Please report suspected security issues privately to:

Paul Skeffington  
paulskeffington@gmail.com

Do not open public issues containing secrets, private data, exploit details, personal data, or sensitive platform evidence.

## Scope

In scope:

- vulnerabilities in repository code
- unsafe handling of local data
- accidental exposure of secrets in examples or documentation
- dependency or packaging issues that affect normal defensive use

Out of scope:

- requests to build offensive automation
- account abuse, evasion, impersonation, credential misuse, or unauthorized access workflows
- requests to process private data without authorization

## Data handling reminder

Do not commit raw private datasets, credentials, cookies, tokens, private exports, or sensitive investigative notes. Use ignored local paths such as `data/raw/`, `data/sensitive/`, or `reports/private/` for local-only work.

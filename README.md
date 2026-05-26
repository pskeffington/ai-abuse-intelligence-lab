# AI Abuse Intelligence Lab

Applied intelligence lab for detecting AI-enabled platform abuse, coordinated misuse, synthetic identity patterns, and adversarial behavior using Python, graph analysis, anomaly detection, and analyst-style reporting.

Author: Paul Skeffington, MS, MPH  
Dartmouth College  
GitHub: @pskeffington-github  
Public contact: paulskeffington@gmail.com

## Mission

This repository is a defensive research and analysis workspace. It is designed to help analysts collect, normalize, analyze, and report on AI-enabled abuse indicators while preserving provenance, reproducibility, and ethical guardrails.

The initial scaffold emphasizes small, object-oriented components:

- ingestion adapters for safe local datasets and future APIs
- normalized domain models for actors, events, artifacts, claims, and relationships
- analysis modules for anomaly detection, graph structure, and coordination signals
- reporting utilities for analyst notes and evidence summaries
- governance documents for responsible handling of sensitive abuse data

## Repository layout

```text
.
├── .github/workflows/ci.yml
├── docs/
│   ├── architecture.md
│   ├── data-governance.md
│   └── research-roadmap.md
├── examples/
│   └── sample_events.csv
├── src/ai_abuse_intel_lab/
│   ├── analysis/
│   ├── ingestion/
│   ├── reporting/
│   ├── config.py
│   ├── models.py
│   └── cli.py
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
└── pyproject.toml
```

## First local run

```bash
git clone https://github.com/pskeffington/ai-abuse-intelligence-lab.git
cd ai-abuse-intelligence-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
python -m ai_abuse_intel_lab --help
pytest
```

## Current status

This is a first-run scaffold. The current modules are intentionally minimal and are meant to establish clean boundaries before analysis logic becomes more complex.

## Safety posture

This project is for defensive research, abuse detection, platform integrity, and intelligence-style reporting. Do not add code that enables impersonation, evasion, automated abuse, account creation, credential theft, harassment, doxxing, or unauthorized platform access.

# Contributing

Thank you for considering a contribution.

This project is a defensive research toolkit. Contributions should improve reproducibility, documentation, analysis quality, test coverage, packaging, or safe analyst workflows.

## Development setup

```bash
git clone https://github.com/pskeffington/ai-abuse-intelligence-lab.git
cd ai-abuse-intelligence-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## Quality checks

Run all checks before opening a pull request:

```bash
ruff check .
mypy src
pytest
```

## Contribution guidelines

- Keep components small and object-oriented.
- Add tests for new behavior.
- Prefer synthetic fixtures over real platform data.
- Preserve provenance fields when adding ingestion or analysis features.
- Clearly separate observations, review signals, and analyst assessments.
- Avoid broad claims of attribution or intent.

## Not accepted

Do not contribute code or documentation intended for impersonation, evasion, harassment, credential misuse, unauthorized access, automated platform manipulation, or processing private data without authorization.

# Idempotency Audit

![Idempotency Audit cover](assets/readme-cover.svg)

> Check mutating API specs for idempotency and retry safety

![stack](https://img.shields.io/badge/stack-Python-b45309?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-be185d?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-4b5563?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-2563eb?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | idempotency review |
| Command | `idempotency-audit` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-idempotency` | high | mutating endpoint lacks idempotency |
| `unsafe-retry` | medium | retries are allowed without safety language |
| `post-create` | low | mutating POST endpoint detected |

## Try it locally

```bash
python -m pip install -e ".[dev]"
idempotency-audit examples/sample.txt
idempotency-audit examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m idempotency_audit --help
```

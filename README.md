# Idempotency Audit

> A small command-line review pass for idempotency review.

![Idempotency Audit cover](assets/readme-cover.svg)

Check mutating API specs for idempotency and retry safety. I keep it small because this kind of check is most useful when it can run beside the work, not after the work has already shipped.

## Signals in plain English

- `missing-idempotency` (high): mutating endpoint lacks idempotency. Fix: Require an idempotency key or documented dedupe behavior..
- `unsafe-retry` (medium): retries are allowed without safety language. Fix: Define retry semantics and duplicate handling..
- `post-create` (low): mutating POST endpoint detected. Fix: Check whether the endpoint needs idempotency guarantees..

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/idempotency-audit.git
cd idempotency-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
idempotency-audit examples/sample.txt
idempotency-audit examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m idempotency_audit --help
```

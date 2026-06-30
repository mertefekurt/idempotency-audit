# idempotency-audit

**Operator Note.** Check mutating API specs for idempotency and retry safety.

## Why This Exists

Payment, provisioning, and workflow APIs can duplicate work under retries. This CLI flags contracts that omit idempotency guarantees.

## Inputs

`idempotency-audit` accepts API endpoint notes, OpenAPI snippets, or review text in text, JSON, JSONL, or CSV form.

## Example Run

```bash
python -m pip install -e ".[dev]"
idempotency-audit examples/sample.txt
idempotency-audit examples/sample.txt --json --fail-on medium
```

## Report Format

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-idempotency` | high | mutating endpoint lacks idempotency |
| `unsafe-retry` | medium | retries are allowed without safety language |
| `post-create` | low | mutating POST endpoint detected |

## Tests

```bash
ruff check .
pytest
python -m idempotency_audit --help
```

License: MIT

### Example Input

```text
POST /charges creates payment retry allowed idempotency missing
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the idempotency-audit policy surface explicit.

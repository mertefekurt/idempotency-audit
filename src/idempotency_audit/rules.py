from __future__ import annotations

from idempotency_audit.models import Rule

PROJECT_NAME = 'idempotency-audit'
SUMMARY = 'Check mutating API specs for idempotency and retry safety.'
SAMPLE_RISK = 'POST /charges creates payment retry allowed idempotency missing'
SAMPLE_CLEAN = 'POST /charges idempotency-key required retry-safe duplicate returns previous result'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='missing-idempotency',
        severity='high',
        pattern='\\bidempotency\\s*(key)?\\s*(missing|none|required false)\\b',
        message='mutating endpoint lacks idempotency',
        recommendation='Require an idempotency key or documented dedupe behavior.',
    ),
    Rule(
        code='unsafe-retry',
        severity='medium',
        pattern='\\bretry allowed\\b(?!.*retry-safe)',
        message='retries are allowed without safety language',
        recommendation='Define retry semantics and duplicate handling.',
    ),
    Rule(
        code='post-create',
        severity='low',
        pattern='\\bPOST\\b.{0,80}\\b(create|creates|provision|charge)\\b',
        message='mutating POST endpoint detected',
        recommendation='Check whether the endpoint needs idempotency guarantees.',
    ),
)

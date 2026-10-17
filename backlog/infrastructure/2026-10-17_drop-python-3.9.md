---
id: "2026-10-17_drop-python-3.9"
title: "Drop Python 3.9 support; keep unpinned Poetry in CI"
status: "Completed"
priority: "High"
created: "2026-10-17"
last_updated: "2026-10-17"
category: "infrastructure"
related_cips: []
owner: "Neil D. Lawrence"
dependencies: []
tags:
- backlog
- ci
- python
- poetry
- eol
---

# Task: Drop Python 3.9 support; keep unpinned Poetry in CI

## Description

CI on `main` fails before pytest runs: `snok/install-poetry` with `version: latest` installs Poetry 2.5.x, which requires Python ≥3.10. The test matrix still includes 3.9, so that job aborts at “Install Poetry” and fail-fast cancels the rest.

Python 3.9 reached end-of-life in October 2025. Rather than pin Poetry to an older release that still installs on 3.9, drop 3.9 from the supported and tested set and keep Poetry on `latest`.

## Acceptance Criteria

- [x] CI test matrix no longer includes Python 3.9
- [x] `pyproject.toml` requires `python = ">=3.10"` and classifiers match (3.10+)
- [x] Workflows keep `version: latest` for Poetry (no pin)
- [x] Tests still pass on the remaining matrix versions

## Implementation Notes

- Touch `.github/workflows/tests.yml` matrix: `["3.10", "3.11", "3.12"]` (optionally add 3.13 later).
- Update `[tool.poetry.dependencies] python` and PyPI classifiers in `pyproject.toml`.
- `publish.yml` / `release.yml` already use Python 3.11; leave Poetry as `latest`.
- Do not pin Poetry as a workaround for 3.9.

## Related

- CIP: none (ops / support-matrix change)
- Trigger: failing Tests workflow on recent `main` pushes (Poetry 2.5.1 install on 3.9)
- Alternative rejected: pin Poetry to 2.2.1

## Progress Updates

### 2026-10-17

Task created and completed: matrix is `3.10`–`3.12`, `python = ">=3.10"`, classifiers updated, Poetry left on `latest` in tests/publish/release workflows.

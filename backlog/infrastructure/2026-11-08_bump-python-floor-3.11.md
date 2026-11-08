---
id: "2026-11-08_bump-python-floor-3.11"
title: "Bump supported Python floor from 3.10 to 3.11"
status: "Proposed"
priority: "Medium"
created: "2026-11-08"
last_updated: "2026-11-08"
category: "infrastructure"
related_cips: []
owner: "Neil D. Lawrence"
dependencies: []
tags:
- backlog
- ci
- python
- support-matrix
- eol
---

# Task: Bump Python floor to 3.11

## Description

ods currently declares `python = ">=3.10"` and CI-tests `3.10`, `3.11`,
and `3.12`. After the Python 3.9 drop (`2026-10-17_drop-python-3.9`),
3.10 is the oldest supported line. Raising the floor to 3.11 simplifies
the matrix, aligns with publish/release already using 3.11, and tracks
where neighbouring tooling (Poetry ecosystem, lynguine CI) is heading.

This is independent of running live dataset downloads once; keep that
work on its own backlog item.

## Acceptance Criteria

- [ ] `pyproject.toml` requires `python = ">=3.11"`
- [ ] PyPI classifiers drop 3.10 and list 3.11+ (add 3.13 only if CI
      covers it)
- [ ] `.github/workflows/tests.yml` matrix no longer includes 3.10
- [ ] Docs / README that mention 3.10 as minimum are updated
- [ ] Tests still pass on the remaining matrix

## Implementation Notes

- Mirror the process used for dropping 3.9: matrix + Poetry constraint +
  classifiers in one PR; leave Poetry on `latest`.
- Coordinate with `2026-11-08_ci-live-dataset-downloads-once` only for
  merge order (either can land first).
- No CIP: support-matrix / ops change.

## Related

- CIP: none
- Prior: `2026-10-17_drop-python-3.9`
- Sibling: `2026-11-08_ci-live-dataset-downloads-once`

## Progress Updates

### 2026-11-08

Task created (Proposed). To land on `main` with or after ods#7.

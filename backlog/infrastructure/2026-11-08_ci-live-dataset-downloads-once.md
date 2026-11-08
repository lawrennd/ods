---
id: "2026-11-08_ci-live-dataset-downloads-once"
title: "CI: run live dataset URL downloads on one Python only"
status: "Proposed"
priority: "High"
created: "2026-11-08"
last_updated: "2026-11-08"
category: "infrastructure"
related_cips: []
owner: "Neil D. Lawrence"
dependencies: []
tags:
- backlog
- ci
- datasets
- network
- flake
---

# Task: CI live dataset downloads once

## Description

The Tests workflow matrix runs the full pods dataset dimension suite on
every Python version (`3.10`, `3.11`, `3.12`). Each job downloads every
mirrored dataset from the network. That multiplies wall time and flake
surface (transient GitHub / `datasets_mirror` 5xx) without testing
version-specific loader behaviour — the loaders are effectively
version-agnostic once imports succeed.

Triggered by PR #7 CI: an early `xw_pen` fetch hit HTTP 504 on one matrix
cell while the same dataset later passed on another job. A later run failed
on `pmlr` (HTTP 503 from `proceedings.mlr.press`) while downloading many
volumes — `pmlr` defaults to `volumes="all"`, so the auto dimension sweep
is especially brittle.

Keep multi-version coverage for cheap tests (imports, `access_tests`,
mocked paths). Run the live network dimension suite on a single matrix
cell only.

## Acceptance Criteria

- [ ] Live `pods/testing/datasets_tests` dimension downloads run on
      **one** CI Python version only (document which, e.g. 3.12)
- [ ] Remaining matrix cells still run non-network / mocked tests (or an
      explicit subset that does not re-fetch all datasets)
- [ ] Workflow docs or comments state why live downloads are single-cell
- [ ] PR / main CI no longer triple-fetches the full catalogue on every push

## Implementation Notes

- Prefer pytest markers (e.g. `@pytest.mark.network`) plus
  `pytest -m "not network"` on secondary matrix cells, or a dedicated
  job that only runs network tests once.
- Optional: cache `ods_data_cache` between jobs via Actions cache if a
  second cell still needs a smoke download.
- `publish.yml` also runs full pytest on 3.11 before release — decide
  whether release should keep a full live pass (reasonable) or share the
  same marker split.
- No CIP: ops / CI change only (same class as the Python 3.9 drop).

## Related

- CIP: none
- Trigger: https://github.com/lawrennd/ods/actions/runs/42477991590
  (`xw_pen` 504 on matrix); discussion after ods#7
- Sibling: `2026-11-08_bump-python-floor-3.11` (separate; do not couple)

## Progress Updates

### 2026-11-08

Task created (Proposed). To land on `main` with or after ods#7.

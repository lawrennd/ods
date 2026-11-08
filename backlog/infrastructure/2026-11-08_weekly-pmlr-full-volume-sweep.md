---
id: "2026-11-08_weekly-pmlr-full-volume-sweep"
title: "Scheduled weekly full pmlr volumes=all download check"
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
- datasets
- pmlr
- schedule
- network
---

# Task: Weekly full pmlr volume sweep

## Description

`pods.datasets.pmlr` defaults to `volumes="all"` and downloads every
Proceedings of Machine Learning Research citeproc YAML from
`proceedings.mlr.press`. That full sweep is **purposeful**: a newly
published volume can break path layout or YAML shape, and only the
complete pull catches it.

It is too heavy and flake-prone for every PR / matrix cell (transient
503s already failed ods#7 CI). PR CI should keep a single-volume (or
small fixed list) smoke test. Move the full sweep to a **scheduled**
GitHub Actions workflow that runs about weekly on `main`, on one Python
version.

## Acceptance Criteria

- [ ] `.github/workflows/` includes a scheduled job (e.g. weekly cron)
      that runs `pods.datasets.pmlr(volumes="all")` (or the existing
      dimension helper with that default) on one Python version
- [ ] Workflow is `workflow_dispatch`-triggerable for ad-hoc runs
- [ ] PR / push Tests workflow does **not** reintroduce
      `volumes="all"` in the auto dimension sweep
- [ ] Failure mode is visible (failed Actions run; optional issue
      notification) without blocking unrelated PRs
- [ ] Short comment in the workflow and/or
      `pods/testing/datasets_tests.py` points at this split of duties

## Implementation Notes

- Suggested cron: weekly off-peak (e.g. Sunday UTC).
- Reuse authorize override / non-interactive prompt patterns already
  used in dimension tests.
- Optional later: retry on HTTP 5xx; mirror recent volumes into
  `datasets_mirror` so the weekly job is less dependent on
  `proceedings.mlr.press` uptime.
- Complements
  `2026-11-08_ci-live-dataset-downloads-once` (matrix / once-per-push
  policy) but is specific to pmlr’s multi-volume hammer.
- No CIP: ops / CI schedule only.

## Related

- CIP: none
- Sibling: `2026-11-08_ci-live-dataset-downloads-once`
- Trigger: ods#7 CI failure on `test_pmlr_dimensions` (HTTP 503 while
  fetching many volumes); full sweep removed from PR auto tests in
  favour of `test_pmlr_dimensions_single_volume`

## Progress Updates

### 2026-11-08

Task created (Proposed) on `main` after ods#7 merge.

---
id: "2026-11-08_cip0003-data-resources-remote-type"
title: "CIP-0003: remote.type data_resources catalogue expand"
status: "In Progress"
priority: "High"
created: "2026-11-08"
last_updated: "2026-11-08"
category: "features"
related_cips: ["0003"]
owner: "Neil D. Lawrence"
dependencies: []
tags:
- backlog
- features
- lynguine
- download
- cip0003
- remote
---

# Task: CIP-0003 remote.type data_resources

## Description

Implement `remote.type: data_resources` in lynguine `materialise()` (on the
CIP-0009 materialise branch): load a **local** pods catalogue JSON, look up
`remote.name`, fetch `urls`×`files` (and dirs/suffices) into the item
`directory`, with licence authorize and cache skip.

## Acceptance Criteria

- [x] `materialise` dispatches `data_resources` without requiring `remote.url`
- [x] Missing catalogue path fails with a message to materialise catalogue first
- [x] Unknown dataset name fails loudly
- [x] Cache skip unless `refresh: true`
- [x] Unit tests with fixture catalogue (no live network)

## Implementation Notes

Lives in `lynguine/access/download.py` alongside CIP-0009 url/github.
ods CIP-0003 owns the product story; lynguine owns the hook.
Lynguine delivery: https://github.com/lawrennd/lynguine/pull/76

## Related

- CIP: 0003 (ods)
- lynguine CIP-0009 / lynguine#20 / lynguine#76

## Progress Updates

### 2026-11-08

Implemented on `cip0009-config-driven-remote-materialise` worktree; tests added.
PR opened as lynguine#76.

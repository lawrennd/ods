---
id: "2026-11-08_cip0003-bmi-steps-two-stage-demo"
title: "CIP-0003: two-stage bmi_steps catalogue demo"
status: "Completed"
priority: "High"
created: "2026-11-08"
last_updated: "2026-11-08"
category: "features"
related_cips: ["0003"]
owner: "Neil D. Lawrence"
dependencies:
- "2026-11-08_cip0003-data-resources-remote-type"
tags:
- backlog
- features
- demo
- cip0003
- pods
---

# Task: CIP-0003 two-stage bmi_steps demo

## Description

Add an interface YAML (or notebook) that (1) materialises
`pods/data_resources.json` via `remote.type: url`, then (2) materialises
`bmi_steps` via `remote.type: data_resources` and reads the CSV. Document
and cross-link lynguine#20 / CIP-0003.

## Acceptance Criteria

- [x] Demo config checked into ods (`examples/bmi_steps_lynguine_flow.yml`)
- [x] Stage A and Stage B are separate remote blocks
- [x] CIP-0003 progress notes point at the demo
- [ ] Comment or link on lynguine#20 when ready

## Related

- CIP: 0003
- lynguine#76

## Progress Updates

### 2026-11-08

Demo YAML added. `from_flow` pre-materialises `cache:` remotes before
`input:` so the two-stage config works in one pass.

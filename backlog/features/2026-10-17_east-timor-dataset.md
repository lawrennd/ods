---
id: "2026-10-17_east-timor-dataset"
title: "Add East Timor language-regions dataset to pods"
status: "Ready"
priority: "High"
created: "2026-10-17"
last_updated: "2026-10-17"
category: "features"
related_cips: []
owner: "Neil D. Lawrence"
dependencies: []
tags:
- backlog
- datasets
- pods
- gpss
---

# Task: Add East Timor language-regions dataset to pods

## Description

GPSS lecture `non-gaussian-likelihoods` (and older GPy / GPRS labs) load East Timor binary language-region data from a local pickle or a dead Sheffield staffwww URL (`M.Zwiessele/gpss/lab2/EastTimor.pickle`, now 403). The data is not available through `pods`, so CI and fresh clones fail unless a local copy is present.

This task adds a first-class `pods.datasets.east_timor` (name TBD) that downloads from `datasets_mirror`, matching other teaching datasets.

## Acceptance Criteria

- [ ] `EastTimor2.pickle` is published under `lawrennd/datasets_mirror/east_timor/` (done locally; push mirror when ready)
- [ ] `pods/data_resources.yml` lists the dataset with mirror URL, citation, and file entry
- [ ] `pods.datasets.east_timor` (or agreed name) returns `X`, `Y`/`y`, and `polygons` (or documents how polygons are exposed)
- [ ] Snippet `_gp/includes/non-gaussian-gps.md` loads via `pods.datasets…` instead of hard-coded path/URL
- [ ] GPSS notebook smoke / CI can run the East Timor cell without vendoring the pickle in `gpss`

## Implementation Notes

### Data shape (verified from extant pickle)

- Tuple `(X, y, polygons)`
- `X`: `(67, 2)` float64 — longitude/latitude
- `y`: `(67, 1)` int64 — binary labels `{0, 1}`
- `polygons`: 67 lists of polygon vertices for map visualisation
- MD5: `16db10d067706fa3f03633408a8d201c`
- Size: ~4.0 MiB

### Provenance / regeneration

- Historical host: Max Zwiessele staffwww path (offline).
- No generation script found in `ods`, `gpss`, `snippets`, or lab notebook trees.
- Identical pickle copies exist in gpss, SheffieldML lab trees, and `mlprojects/gplvm/tex/oxford14/`.
- Prefer mirroring the teaching artifact now; optionally later regenerate from GIS/language-map sources *de novo* if those materials can be recovered (document license and citation when doing so).

### Suggested API sketch

```python
def east_timor(data_set="east_timor"):
    if not access.data_available(data_set):
        access.download_data(data_set)
    path = os.path.join(access.DATAPATH, data_set, "EastTimor2.pickle")
    with open(path, "rb") as f:
        try:
            X, y, polygons = pickle.load(f, encoding="latin1")
        except TypeError:
            X, y, polygons = pickle.load(f)
    return access.data_details_return(
        {"X": X, "Y": y, "polygons": polygons, "info": "..."},
        data_set,
    )
```

Follow existing patterns in `olympic_marathon_men` / `robot_wireless` for `data_resources.yml` URL pointing at:

`https://github.com/lawrennd/datasets_mirror/raw/main/east_timor/`

## Related

- CIP: none yet (small feature; CIP only if API debate warrants it)
- Downstream: `lawrennd/snippets/_gp/includes/non-gaussian-gps.md`, `mlatcl/gpss` notebook smoke CI
- Mirror: `~/lawrennd/datasets_mirror/east_timor/`
- Dead URL: `http://staffwww.dcs.shef.ac.uk/people/M.Zwiessele/gpss/lab2/EastTimor.pickle`

## Progress Updates

### 2026-10-17

- Task created after GPSS CI smoke failures (East Timor 403).
- Confirmed data is not in current pods dataset list.
- Mirrored `EastTimor2.pickle` into `datasets_mirror/east_timor/` with README provenance (local; awaiting push).
- Regeneration *de novo* deferred: no source GIS/script located; mirror preserves the historical teaching file.

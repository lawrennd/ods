---
id: "2026-10-17_east-timor-dataset"
title: "Add East Timor language-regions dataset to pods"
status: "In Progress"
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

This task adds a first-class `pods.datasets.east_timor` that downloads from `datasets_mirror`, matching other teaching datasets.

## Acceptance Criteria

- [x] `EastTimor2.pickle` is published under `lawrennd/datasets_mirror/east_timor/`
- [ ] `pods/data_resources.yml` (and `.json`) lists the dataset with mirror URL, citation, and file entry
- [ ] `pods.datasets.east_timor` returns `X`, `Y`, and `polygons`
- [x] Snippet `_gp/includes/non-gaussian-gps.md` loads via `pods.datasets.east_timor()` (done; assumes pods API below)
- [ ] GPSS notebook smoke / CI can run the East Timor cell without vendoring the pickle in `gpss` (after pods release + notebook rebuild)

## Implementation Notes

### Data shape (verified from extant pickle)

- Tuple `(X, y, polygons)`
- `X`: `(67, 2)` float64 — longitude/latitude
- `y`: `(67, 1)` int64 — binary labels `{0, 1}`
- `polygons`: 67 lists of polygon vertices for map visualisation
- MD5: `16db10d067706fa3f03633408a8d201c`
- Size: 4196387 bytes (~4.0 MiB)

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

Mirror URL pattern (as for `olympic_marathon_men` / `robot_wireless`):

`https://github.com/lawrennd/datasets_mirror/raw/main/east_timor/`

### Provenance research (2026-10-17)

**Decision: mirror the teaching pickle; do not recreate from the web as a drop-in replacement.**

Findings:

1. **Only public host** for this file was Max Zwiessele’s Sheffield staffwww URL (now 403). GPSS / GPy labs still point there. No other repository publishes `EastTimor.pickle` / `EastTimor2.pickle`.
2. **Teaching text** describes “binary observations of the language that is spoken in different regions of East-Timor.” No map citation, license, generation script, or label semantics (e.g. which family is `0` vs `1`) appear in labs, snippets, or notebooks.
3. **AISTATS 2014** (Andrade-Pacheco, Hensman, Zwiessele, Lawrence, *Hybrid Discriminative-Generative Approach with Gaussian Processes*) does **not** document or cite this dataset.
4. **Identical local copies** exist in `mlatcl/gpss`, SheffieldML GPRS/GPSS lab trees, and `mlprojects/gplvm/tex/oxford14/` — all teaching redistributions of the same artifact (MD5 above).
5. **Open modern Timor language polygons** exist but are **not** this dataset:
   - [Glottography / Edwards 2020 Meto ranges](https://github.com/Glottography/edwards2020metathesis) (CC-BY-4.0) — multi-language ranges for Timor / Meto varieties; cite Edwards 2020 + the Glottography release DOI if used.
   - Broader Glottography / Atlas of the World’s Languages digitizations — global language areas, not 67 binary admin-style regions.
   - Williams-van Klinken & Williams (2015) census mother-tongue maps — PDF maps, not ready polygons.
   - Ethnologue / World Language Mapping System — proprietary / paywalled.
6. **Recreating from those sources** would produce a *new* multi-class (or differently partitioned) dataset with different region count and labels. Useful as a future optional dataset with proper CC-BY credit; **not** a substitute for the GPSS notebook’s expected `(X, y, polygons)` teaching file.

**Credit for pods / mirror:**

- Packaging for GPSS / GPy labs: Max Zwiessele (historical host).
- Upstream GIS / linguistic map source: **unknown / undocumented** — state this explicitly in `citation` / `details`.
- Optional future regenerable dataset: credit Edwards (2020) and Glottography under CC-BY-4.0 (separate from this task).

## Related

- CIP: none yet (small feature; CIP only if API debate warrants it)
- Downstream: `lawrennd/snippets/_gp/includes/non-gaussian-gps.md`, `mlatcl/gpss` notebook smoke CI
- Mirror: `~/lawrennd/datasets_mirror/east_timor/` (pushed to `lawrennd/datasets_mirror`)
- Dead URL: `http://staffwww.dcs.shef.ac.uk/people/M.Zwiessele/gpss/lab2/EastTimor.pickle`
- GPSS lecture: https://mlatcl.github.io/gpss/lectures/07-non-gaussian-likelihoods.html

## Progress Updates

### 2026-10-17

- Task created after GPSS CI smoke failures (East Timor 403).
- Confirmed data is not in current pods dataset list.
- Mirrored `EastTimor2.pickle` into `datasets_mirror/east_timor/` with README provenance; pushed to GitHub.
- Provenance web research completed: keep teaching mirror; defer *de novo* regeneration; document credit guidance above.
- Updated `snippets/_gp/includes/non-gaussian-gps.md` to load via `pods.datasets.east_timor()` returning `X`, `Y`, `polygons` (pods upload still pending).

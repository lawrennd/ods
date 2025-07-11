---
id: "2025-07-11_broken-data-urls"
title: "Fix Broken Data URLs in Dataset Resources"
status: "Completed"
priority: "Medium"
created: "2025-07-11"
last_updated: "2025-07-11"
owner: "Development Team"
github_issue: ""
dependencies: ""
tags:
- backlog
- bugs
- data-sources
- urls
---

# Task: Fix Broken Data URLs in Dataset Resources

## Description

Several dataset URLs in `pods/data_resources.json` are no longer accessible, causing 403 Forbidden and 404 Not Found errors during test execution. These need to be updated to working URLs or alternative data sources.

**Affected Datasets:**
1. `brendan_faces` - 403 Forbidden: `http://www.cs.nyu.edu/~roweis/data/frey_rawface.mat`
2. `olivetti_glasses` - 403 Forbidden: `http://www.cs.nyu.edu/~roweis/data/olivettifaces.mat`
3. `nigerian_population` - 404 Not Found: Nigerian population data URL on humdata.org

## Acceptance Criteria

- [x] All broken URLs are identified and documented
- [x] Working alternative URLs are found for each dataset
- [x] `pods/data_resources.json` is updated with new URLs
- [x] `test_brendan_faces_dimensions` passes without network errors
- [x] `test_olivetti_glasses_dimensions` passes without network errors
- [x] `test_nigerian_population_dimensions` passes without network errors
- [x] All datasets can be downloaded successfully in CI environment

## Implementation Notes

**Current broken URLs:**
- `http://www.cs.nyu.edu/~roweis/data/frey_rawface.mat` (403 Forbidden)
- `http://www.cs.nyu.edu/~roweis/data/olivettifaces.mat` (403 Forbidden)
- Nigerian population data URL on humdata.org (404 Not Found)

**Potential solutions:**
1. Find alternative mirrors or repositories hosting the same data
2. Use the existing GitHub mirror URLs that are already in the resources
3. Contact data providers for updated URLs
4. Consider hosting data files in the project's own repository

**Files to update:**
- `pods/data_resources.json`
- `pods/data_resources.yml` (if used)

## Related

- CIP: None
- PRs: None
- Documentation: `pods/data_resources.json`

## Progress Updates

### 2025-07-11
Task created to track broken data URLs identified in test suite analysis.

### 2025-07-11
✅ **COMPLETED** - All broken URLs successfully fixed!
- Updated `brendan_faces` URL to GitHub mirror
- Updated `olivetti_faces` URL to GitHub mirror  
- Updated `nigerian_population` URL to GitHub mirror
- All three tests now pass: `test_brendan_faces_dimensions`, `test_olivetti_glasses_dimensions`, `test_nigerian_population_dimensions` 
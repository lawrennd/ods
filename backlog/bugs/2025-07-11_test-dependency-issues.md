---
id: "2025-07-11_test-dependency-issues"
title: "Fix Missing Dependencies in Test Suite"
status: "Ready"
priority: "High"
created: "2025-07-11"
last_updated: "2025-07-11"
owner: "Development Team"
github_issue: ""
dependencies: ""
tags:
- backlog
- bugs
- testing
- dependencies
---

# Task: Fix Missing Dependencies in Test Suite

## Description

Several tests are failing due to missing Python package dependencies that are required for specific dataset functionality. The dependencies are defined in `pyproject.toml` under the `all-datasets` extra but may not be properly installed in the CI environment.

**Affected Tests:**
1. `test_airline_delay_dimensions` - Missing `pytables` for HDF5 file support
2. `test_hospitalized_covid_dimensions` - Missing `openpyxl` for Excel file support  
3. `test_kepler_lightcurves_dimensions` - Missing `astropy` for astronomical data processing
4. `test_epomeo_gpx_dimensions` - Missing `gpxpy` for GPS data processing

## Acceptance Criteria

- [ ] All missing dependencies are properly installed in CI environment
- [ ] `test_airline_delay_dimensions` passes without import errors
- [ ] `test_hospitalized_covid_dimensions` passes without import errors
- [ ] `test_kepler_lightcurves_dimensions` passes without import errors
- [ ] `test_epomeo_gpx_dimensions` passes without import errors
- [ ] CI workflow installs `all-datasets` extra correctly

## Implementation Notes

The dependencies are already defined in `pyproject.toml`:
```toml
[tool.poetry.extras]
all-datasets = ["tables", "pytrends", "geopandas", "astropy", "netpbmfile", "gpxpy", "openpyxl"]
```

The GitHub Actions workflow should install with:
```bash
poetry install --with dev --extras "all-datasets"
```

**Required packages:**
- `pytables` (for HDF5 support)
- `openpyxl` (for Excel support)
- `astropy` (for astronomical data)
- `gpxpy` (for GPS data)

## Related

- CIP: None
- PRs: None
- Documentation: `.github/workflows/tests.yml`

## Progress Updates

### 2025-07-11
Task created to track missing dependency issues identified in test suite analysis. 
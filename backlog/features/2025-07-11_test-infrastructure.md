---
id: "2025-07-11_test-infrastructure"
title: "Modernize and Fix Test Infrastructure for ODS"
status: "In Progress"
priority: "High"
created: "2025-07-11"
last_updated: "2025-07-11"
owner: "Neil D. Lawrence"
github_issue: ""
dependencies: ""
tags:
- backlog
- testing
- infrastructure
---

# Task: Modernize and Fix Test Infrastructure

## Description

The current test infrastructure for ODS relies on the nose test runner, which is incompatible with Python 3.11+ and is no longer maintained. Tests are not auto-discovered by pytest or unittest due to their structure. This task aims to modernize the test infrastructure so that tests are compatible with current Python versions, are easily runnable locally and in CI, and are auto-discoverable by standard tools (pytest/unittest). This will improve reliability, maintainability, and contributor experience.

## Acceptance Criteria

- [x] All existing tests are runnable with pytest and/or unittest on Python 3.11+
- [x] No dependency on nose for running tests
- [x] Tests are auto-discoverable by pytest/unittest
- [x] CI workflow is updated to use the new test runner
- [ ] Tests are passing
- [ ] Documentation is updated to reflect new test instructions

## Implementation Notes

- Refactor test files to use standard unittest or pytest conventions (class-based or function-based with proper naming)
- Remove or replace nose-specific decorators and assertions
- Update GitHub Actions workflow to use pytest or unittest
- Ensure all tests pass on Python 3.11+
- Update README and developer docs with new test instructions

## Related

- CIP: [To be created if major refactor required]
- PRs: []
- Documentation: []

## Progress Updates

### 2025-07-11
Task created with Proposed status.

### 2025-07-11
Updated to In Progress status after implementing pytest migration:
- Migrated from nose to pytest
- Updated pyproject.toml with pytest configuration and dependencies
- Created new GitHub Actions workflow using Poetry
- Fixed binary compatibility issues with conda environment
- Tests now run successfully with 25 passing tests
- Remaining issues are missing optional dependencies and code compatibility fixes
- Need to update documentation and fix remaining test failures 
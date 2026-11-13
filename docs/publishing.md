# Publishing to PyPI

This repository is configured to automatically publish to PyPI when a new release is created on GitHub. Packaging uses [uv](https://docs.astral.sh/uv/).

## How it works

1. *Create a release* on GitHub with a version tag (e.g., `v0.1.18`)
2. *Update the version* in `pyproject.toml` to match the release tag
3. *Publish the release* on GitHub
4. *GitHub Actions* automatically runs tests and publishes to PyPI via `uv publish`

## Setup Requirements

### 1. Publishing authentication

**Preferred: Trusted Publishing (OIDC)** — no API token secret required.

1. On PyPI, open the `pods` project → Settings → Publishing
2. Add a GitHub Actions publisher with:
   - Owner: `lawrennd`
   - Repository: `ods`
   - Workflow: `publish.yml`
   - Environment: `release` (must match `.github/workflows/publish.yml`)
3. Ensure the GitHub repo has an Environment named `release`

The publish job already sets `permissions.id-token: write` and `environment: release` so `uv publish` can use OIDC.

**Fallback: API token** — reuse the existing repo secret `PYPI_API_TOKEN` (mapped to `UV_PUBLISH_TOKEN` in the workflow). You do not need a new secret name for the uv migration. Create or rotate the token only if publishing fails and Trusted Publishing is not configured:

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Create an API token
3. Store it as GitHub Actions secret `PYPI_API_TOKEN`

### 2. Version Management

Before creating a release:

1. Update the version in `pyproject.toml`:
   ```toml
   [project]
   version = "0.1.18"  # Match your release tag
   ```

2. Commit and push the version change:
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to 0.1.18"
   git push
   ```

## Creating a Release

1. *Create a new release* on GitHub:
   - Go to Releases → "Create a new release"
   - Tag version: `v0.1.18` (must match pyproject.toml version)
   - Release title: `Version 0.1.18`
   - Description: Add release notes
   - Check "Set as the latest release"

2. *Publish the release* - This triggers the GitHub Actions workflow

## Workflow Steps

The publishing workflow (`publish.yml`) performs these steps:

1. *Setup* - Installs uv and the project environment
2. *Install dependencies* - `uv sync --frozen --group dev --all-extras`
3. *Run tests* - Ensures all tests pass before publishing
4. *Version check* - Verifies the release tag matches `[project].version`
5. *Build package* - `uv build`
6. *Publish to PyPI* - `uv publish` (OIDC Trusted Publishing, with `PYPI_API_TOKEN` as fallback)

## Local development

```bash
# Install uv: https://docs.astral.sh/uv/getting-started/installation/
uv sync --group dev --all-extras
uv run pytest
uv build
```

## Troubleshooting

### Version Mismatch Error

If you see "Release version doesn't match project version":
- Ensure the version in `pyproject.toml` matches your release tag
- The release tag should be `v0.1.18` and pyproject.toml should have `version = "0.1.18"`

### PyPI Authentication Error

If you see authentication errors:
- Confirm the Trusted Publisher on PyPI matches `publish.yml` and environment `release`
- Or verify the `PYPI_API_TOKEN` secret is set and valid
- Check that the token hasn't expired

### Test Failures

If tests fail during the publishing workflow:
- Fix the failing tests locally first
- Push the fixes to the main branch
- Create a new release with the corrected code

## Manual Publishing (if needed)

```bash
uv sync --group dev --all-extras
uv run pytest
uv build
# Local publish needs a token (Trusted Publishing is CI-only):
UV_PUBLISH_TOKEN=pypi-... uv publish
```

## Package Information

The package is published as `pods` on PyPI:
- *Package name*: `pods`
- *Homepage*: https://github.com/lawrennd/ods
- *Documentation*: Available through the GitHub repository
- *License*: MIT

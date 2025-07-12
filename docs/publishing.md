# Publishing to PyPI

This repository is configured to automatically publish to PyPI when a new release is created on GitHub.

## How it works

1. **Create a release** on GitHub with a version tag (e.g., `v0.1.18`)
2. **Update the version** in `pyproject.toml` to match the release tag
3. **Publish the release** on GitHub
4. **GitHub Actions** automatically runs tests and publishes to PyPI

## Setup Requirements

### 1. PyPI API Token

You need to create a PyPI API token and add it to your GitHub repository secrets:

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Create an API token with "Entire account" scope
3. Copy the token
4. Go to your GitHub repository → Settings → Secrets and variables → Actions
5. Create a new secret named `PYPI_API_TOKEN` with the PyPI token value

### 2. Version Management

Before creating a release:

1. Update the version in `pyproject.toml`:
   ```toml
   [tool.poetry]
   version = "0.1.18"  # Match your release tag
   ```

2. Commit and push the version change:
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to 0.1.18"
   git push
   ```

## Creating a Release

1. **Create a new release** on GitHub:
   - Go to Releases → "Create a new release"
   - Tag version: `v0.1.18` (must match pyproject.toml version)
   - Release title: `Version 0.1.18`
   - Description: Add release notes
   - Check "Set as the latest release"

2. **Publish the release** - This triggers the GitHub Actions workflow

## Workflow Steps

The publishing workflow (`publish.yml`) performs these steps:

1. **Setup** - Installs Python and Poetry
2. **Install dependencies** - Installs all project dependencies
3. **Run tests** - Ensures all tests pass before publishing
4. **Version check** - Verifies the release tag matches pyproject.toml version
5. **Build package** - Creates distribution files
6. **Publish to PyPI** - Uploads the package to PyPI

## Troubleshooting

### Version Mismatch Error

If you see "Release version doesn't match Poetry version":
- Ensure the version in `pyproject.toml` matches your release tag
- The release tag should be `v0.1.18` and pyproject.toml should have `version = "0.1.18"`

### PyPI Authentication Error

If you see authentication errors:
- Verify the `PYPI_API_TOKEN` secret is set correctly in GitHub
- Ensure the token has the correct permissions on PyPI
- Check that the token hasn't expired

### Test Failures

If tests fail during the publishing workflow:
- Fix the failing tests locally first
- Push the fixes to the main branch
- Create a new release with the corrected code

## Manual Publishing (if needed)

If you need to publish manually:

```bash
# Install dependencies
poetry install --with dev

# Run tests
poetry run pytest

# Build package
poetry build

# Publish (requires PyPI token)
poetry publish
```

## Package Information

The package is published as `pods` on PyPI:
- **Package name**: `pods`
- **Homepage**: https://github.com/lawrennd/ods
- **Documentation**: Available through the GitHub repository
- **License**: MIT 
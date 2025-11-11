# CI/CD Scripts

This directory contains scripts used for CI/CD pipelines and release automation.

## Purpose

**CI/CD scripts verify package installation and release processes.**

- Smoke test that package installs correctly from PyPI
- Validate version consistency between git tags and pyproject.toml
- Run without mocks - test real package installation
- Execute during releases and after every push

**vs. tests/** - Unit tests that verify code functionality with full coverage

## When Run

| Script | test.yml (every push) | publish.yml (release) |
|--------|----------------------|----------------------|
| verify_installation.py | ✅ After unit tests | ✅ After PyPI upload |
| validate_version.py | ❌ | ✅ Before build |

## Scripts

### verify_installation.py

Verifies that the GAIK package was installed correctly. This script:
- Tests all module imports
- Checks public API availability
- Validates provider registry
- Tests basic functionality without making API calls

**Used by:** `.github/workflows/test.yml` and `.github/workflows/publish.yml`

**Run manually:**
```bash
python scripts/verify_installation.py
```

### validate_version.py

Validates that the git tag matches the version in `pyproject.toml`.

**Used by:** `.github/workflows/publish.yml` during release process

**Run manually:**
```bash
python scripts/validate_version.py v0.3.0
```

## Note

These are CI/CD tools, not unit tests. For unit tests, see the `tests/` directory.

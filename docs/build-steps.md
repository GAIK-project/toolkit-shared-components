# Build & Publish - Quick Reference

## Test PyPI (Development)

```powershell
# Setup (once)
uv pip install build twine

# Build and publish
cd .\gaik-py\
python -m build
python -m twine upload --repository-url https://test.pypi.org/legacy/ -u __token__ -p $env:TEST_PYPI_API_TOKEN dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ gaik
```

**Prerequisites:**

- Set environment variable: `$env:TEST_PYPI_API_TOKEN = "pypi-..."`
- Get token from: <https://test.pypi.org/manage/account/token/>

---

## Production PyPI (Automated via GitHub Actions)

```bash
# 1. Update version in gaik-py/pyproject.toml
version = "0.2.0"

# 2. Commit and create tag
git add gaik-py/pyproject.toml
git commit -m "Bump version to 0.2.0"
git tag v0.2.0
git push origin main
git push origin v0.2.0
```

**GitHub Actions will automatically:**

- Build the package
- Publish to Test PyPI
- Test installation

**Prerequisites:**

- GitHub Secret: `TEST_PYPI_API_TOKEN` configured in repository settings

---

## Manual Production Publish (if needed)

```powershell
cd .\gaik-py\
python -m build
python -m twine upload dist/*
# Uses: $env:PYPI_API_TOKEN
```

**Note:** Production PyPI doesn't allow re-uploading same version. Always bump version first!

# Python Package Build Steps

## Steps to Publish Package to TestPyPI

### 1. Install Required Tools

```powershell
uv pip install build twine
```

### 2. Navigate to Project Directory

```powershell
cd .\gaik-py\
```

### 3. Build the Package

```powershell
python -m build
```

This creates a `dist/` directory containing `.whl` and `.tar.gz` files.

### 4. Upload Package to TestPyPI

```powershell
python -m twine upload --repository-url https://test.pypi.org/legacy/ -u __token__ -p $env:TEST_PYPI_API_TOKEN dist/*
```

**Note:** Make sure the `TEST_PYPI_API_TOKEN` environment variable is set before running this command.

---

## Cheat Sheet

```powershell
# Complete process in one go
uv pip install build twine
cd .\gaik-py\
python -m build
python -m twine upload --repository-url https://test.pypi.org/legacy/ -u __token__ -p $env:TEST_PYPI_API_TOKEN dist/*
```

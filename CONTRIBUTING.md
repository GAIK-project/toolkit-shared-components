# 📋 Contributing to GAIK - Quick Guide

Simple cheatsheet for developers new to this project.

---

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/GAIK-project/gaik-toolkit.git
cd gaik-toolkit/gaik-py

# Create virtual environment and install
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac

# Install for development (all features)
pip install -e .[all]

# Test it works
python ../examples/extract/demo_anthropic.py
python ../examples/vision/demo_vision_simple.py
```

**Installation options:**

```bash
# All features (recommended for development)
pip install -e .[all]

# Extract only (data extraction with all LLM providers)
pip install -e .[extract]

# Vision only (PDF parsing)
pip install -e .[vision]
```

---

## ➕ Adding New Code

### Add a New LLM Provider

**Files to edit:**

1. **Create provider** → `gaik-py/src/gaik/providers/yourprovider.py`

   ```python
   from langchain_yourprovider import ChatYourProvider
   from .base import LLMProvider, _build_model_kwargs

   class YourProviderProvider(LLMProvider):
       @property
       def default_model(self) -> str:
           return "model-name"

       def create_chat_model(self, model=None, api_key=None, **kwargs):
           model_name = model or self.default_model
           model_kwargs = _build_model_kwargs(model_name, api_key=api_key, **kwargs)
           return ChatYourProvider(**model_kwargs)
   ```

2. **Add dependency** → `gaik-py/pyproject.toml`

   Add to `[project.optional-dependencies]` extract group:

   ```toml
   extract = [
       "langchain-core>=1.0.3",
       "langchain-yourprovider>=1.0.0",  # Add here
   ]
   ```

3. **Register** → `gaik-py/src/gaik/providers/__init__.py`

**Done!** Use with `SchemaExtractor("task", provider="yourprovider")`

### Add a New Feature/Parser

- **Extraction features** → `gaik-py/src/gaik/extract/`
- **Vision/PDF parsers** → `gaik-py/src/gaik/parsers/`
- **Add examples** → `examples/extract/` or `examples/vision/`

---

## 📦 Dependencies - Feature Groups

**GAIK uses optional dependency groups** - users install only what they need!

### Feature Groups

| Group       | Purpose                                | Dependencies                                             |
| ----------- | -------------------------------------- | -------------------------------------------------------- |
| `[extract]` | Data extraction with all LLM providers | langchain-\* packages (OpenAI, Anthropic, Google, Azure) |
| `[vision]`  | PDF/image parsing                      | openai, pdf2image, pillow                                |
| `[all]`     | All features                           | extract + vision                                         |

### Naming Convention

- **LangChain providers:** `langchain-{provider}` (e.g., `langchain-openai`, `langchain-anthropic`)
- **Vision tools:** `pdf2image`, `pillow`, `openai`
- **Core utilities:** `pydantic` (always installed)

### Where to Add Dependencies

**Location:** `gaik-py/pyproject.toml` under `[project.optional-dependencies]`

**For extract providers:**

```toml
[project.optional-dependencies]
extract = [
    "langchain-core>=1.0.3",
    "langchain-yourprovider>=1.0.0",  # Add here
]
```

**For vision features:**

```toml
vision = [
    "openai>=2.7",
    "your-vision-tool>=1.0.0",  # Add here
]
```

**After adding:** Reinstall with `pip install -e .[all]`

---

## 🧪 Testing

**Write tests for your code:**

- Add tests to `gaik-py/tests/` - GitHub Actions runs these automatically
- Add usage example to `examples/` - Shows how to use your feature

**Code quality:**

```bash
ruff format src/gaik/
ruff check --fix src/gaik/
```

**Before committing:**

- ✅ Tests added (if needed)
- ✅ Code formatted (ruff)

---

## 🚀 Release Process (Maintainers Only)

**GitHub Actions handles everything automatically!**

### Automated Release Steps

1. **Update version** → Edit `gaik-py/pyproject.toml`

   ```toml
   version = "0.3.0"  # Bump version number
   ```

2. **Commit changes**

   ```bash
   git add gaik-py/pyproject.toml
   git commit -m "Bump to v0.3.0"
   ```

3. **Create git tag**

   ```bash
   git tag v0.3.0
   ```

4. **Push everything**

   ```bash
   git push origin main
   git push origin v0.3.0
   ```

5. **Done!** 🎉 GitHub Actions automatically:
   - Builds the package (`python -m build`)
   - Validates metadata (`twine check dist/*`)
   - Publishes to PyPI (`twine upload dist/*`)
   - Creates GitHub Release with notes

**Check progress:** GitHub → Actions tab → "Publish to Production PyPI" workflow

### Manual Release (Emergency Only)

If GitHub Actions fails, maintainers can publish manually:

```bash
cd gaik-py

# Build package
python -m build

# Validate
twine check dist/*

# Upload to PyPI (requires PYPI_API_TOKEN)
twine upload dist/*
```

> **Note:** This is rarely needed. GitHub Actions is the recommended way to publish.

---

## 📁 Project Structure Reference

```
gaik-toolkit/
├── gaik-py/                          # 📦 PyPI package (published)
│   ├── src/gaik/                     # Source code
│   │   ├── extract/                  # Data extraction module
│   │   ├── parsers/                  # Vision/PDF parsing
│   │   └── providers/                # LLM provider implementations
│   ├── tests/                        # 🧪 Test scripts
│   ├── pyproject.toml                # Package config & dependencies
│   └── README.md                     # Package documentation
│
├── dev/                              # 🚧 Work in progress (not published)
│   ├── experimental/                 # Experimental features
│   ├── features/                     # Features under development
│   └── README.md                     # Dev workflow guide
│
├── examples/                         # 📚 Usage examples (not published)
│   ├── extract/                      # Extraction demos
│   └── vision/                       # Vision parsing demos
│
└── .github/workflows/                # 🤖 CI/CD pipelines
    ├── test.yml                      # Run tests on PR/push
    └── publish.yml                   # Auto-publish to PyPI
```

**Where to add code:**

- Production-ready code → `gaik-py/src/gaik/`
- Code in development → `dev/` (see [dev/README.md](dev/README.md))
- Usage examples → `examples/`

---

## ❓ Questions?

- **Issues**: [github.com/GAIK-project/gaik-toolkit/issues](https://github.com/GAIK-project/gaik-toolkit/issues)
- **Documentation**: [gaik-py/README.md](gaik-py/README.md)

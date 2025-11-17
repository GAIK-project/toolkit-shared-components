**IMPORTANT:** Keep this updated with architecture changes — this is the source of truth for AI agents.

## Monorepo Structure
```
gaik-toolkit/
├── packages/python/gaik/     # Published PyPI package
│   ├── src/gaik/
│   │   ├── extract/          # Schema extraction + co-located tests
│   │   ├── providers/        # LLM provider integrations + tests
│   │   └── parsers/          # Vision/PDF parsing + tests
│   ├── scripts/              # Installation verification
│   └── pyproject.toml        # Package config, dependencies, versioning
├── dev/scripts/              # Monorepo CI utilities (test runner)
├── examples/                 # Usage examples (extract/, vision/)
└── .github/workflows/        # CI/CD (test.yml, publish.yml)
```

## Package Details
- **Published as:** `gaik` on [PyPI](https://pypi.org/project/gaik/)
- **Source location:** `packages/python/gaik/src/gaik/`
- **Tests:** Co-located with code in `src/gaik/*/tests/`
- **Versioning:** Automatic via `setuptools-scm` from git tags (`vX.Y.Z`)

## Core APIs
```python
# Extraction (requires: pip install gaik[extract])
from gaik.extract import SchemaExtractor
extractor = SchemaExtractor("Extract name and age", provider="anthropic")
results = extractor.extract(["Alice is 25"])

# Parser (requires: pip install gaik[parser])
from gaik.parsers import VisionParser, get_openai_config
config = get_openai_config(use_azure=True)  # or False for OpenAI
parser = VisionParser(config)
markdown = parser.convert_pdf("document.pdf")
```

## Environment Variables
Choose one LLM provider:
- **OpenAI:** `OPENAI_API_KEY`
- **Anthropic:** `ANTHROPIC_API_KEY`
- **Google:** `GOOGLE_API_KEY`
- **Azure:** `AZURE_API_KEY` + `AZURE_ENDPOINT`

## Adding a New LLM Provider
1. Create `packages/python/gaik/src/gaik/providers/<name>.py`
   - Implement `create_chat_model()` method
   - Use `_build_model_kwargs()` helper for consistency
2. Add dependency: `packages/python/gaik/pyproject.toml` → `[project.optional-dependencies]`
   ```toml
   extract = ["langchain-<name>>=X.Y"]
   ```
3. Export: `packages/python/gaik/src/gaik/providers/__init__.py`
4. Test: `python examples/extract/demo_anthropic.py` (adapt for your provider)

## Adding a New Parser
1. Create `packages/python/gaik/src/gaik/parsers/<name>.py`
2. Add dependencies to `packages/python/gaik/pyproject.toml` → `[project.optional-dependencies]`
   ```toml
   vision = ["your-library>=X.Y"]
   ```
3. Export: `packages/python/gaik/src/gaik/parsers/__init__.py`
4. Add tests: `packages/python/gaik/src/gaik/parsers/tests/test_<name>.py`
5. Add example: `examples/<name>/demo.py` with README

## Local Development
```bash
cd packages/python/gaik
pip install -e .[all,dev]     # All features + dev tools
pytest                         # Run tests
ruff check --fix src/gaik/    # Lint
python -m build                # Build package
twine check dist/*             # Validate
```

## Testing
- **Smoke test:** `python examples/extract/demo_anthropic.py`
- **Unit tests:** `cd packages/python/gaik && pytest`
- **CI tests:** Automatic on push via `.github/workflows/test.yml`
- **Test runner:** `python dev/scripts/run_python_package_tests.py` (used by CI)

## Publishing Workflow
1. **Merge changes** to `main` branch
2. **Create version tag:**
   ```bash
   git tag v0.3.0
   git push origin v0.3.0
   ```
3. **GitHub Actions** automatically:
   - Runs tests via `test.yml`
   - Builds package from `packages/python/gaik/`
   - Publishes to PyPI
   - Creates GitHub Release with artifacts
4. **Verify:**
   ```bash
   pip install --upgrade gaik
   python -c "import gaik; print(gaik.__version__)"
   ```

**Note:** Tag format MUST be `vX.Y.Z` (semantic versioning)

## Key Configuration Files
- `packages/python/gaik/pyproject.toml` - Package metadata, dependencies, build config
- `.github/workflows/test.yml` - Run tests on push/PR
- `.github/workflows/publish.yml` - Publish to PyPI on tag push
- `dev/scripts/run_python_package_tests.py` - Monorepo test discovery

## Documentation Guidelines
- Use cheatsheet format (commands/examples, minimal prose)
- Show code examples, not explanations
- Use tables for multi-option configs
- Keep file references as clickable links
- Update all docs/examples when behavior changes

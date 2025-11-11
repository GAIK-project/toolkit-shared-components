**IMPORTANT:** Concise cheatsheet for AI agents. Keep current.

## Package Structure
- Source: `gaik-py/src/gaik/`
- Modules: `extract/` (extraction API), `providers/` (LLM registry), `parsers/` (vision/PDF)
- Published: [pypi.org/project/gaik](https://pypi.org/project/gaik/)

## Core APIs
```python
# Extraction
from gaik.extract import SchemaExtractor
extractor = SchemaExtractor("Extract name and age", provider="anthropic")
results = extractor.extract(["Alice is 25"])

# Vision (requires: pip install gaik[vision])
from gaik.parsers import VisionParser, get_openai_config
config = get_openai_config(use_azure=True)  # or False for OpenAI
parser = VisionParser(config)
```

## Env Vars (choose one provider)
- OpenAI: `OPENAI_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`
- Google: `GOOGLE_API_KEY`
- Azure: `AZURE_API_KEY` + `AZURE_ENDPOINT` (backward compatible: `AZURE_OPENAI_*`)

## Adding Provider
1. Create `gaik/providers/<name>.py` with `LLMProvider.create_chat_model()`
2. Use `_build_model_kwargs()` helper
3. Add `langchain-<name>` to `pyproject.toml`
4. Register in `gaik/providers/__init__.py`
5. Test with `examples/demo_anthropic.py` pattern

## Testing
- Smoke test: `python examples/demo_anthropic.py`
- Build: `cd gaik-py && python -m build && twine check dist/*`
- CI: `environment: release` → version validation → PyPI publish → GitHub Release

## Publishing (see CONTRIBUTING.md Release section)
1. Update `gaik-py/pyproject.toml` version
2. Commit and tag: `git tag vX.Y.Z && git push origin main vX.Y.Z`
3. GitHub Actions auto-publishes to PyPI
4. Verify: `pip install gaik && python -c "import gaik; print(gaik.__version__)"`

## Documentation Style
- **Cheatsheet format**: Commands/examples only, minimal prose
- **Keep concise**: Remove marketing language, focus on facts
- **Tables over prose**: Use tables for multi-option configs
- **Reference, not tutorial**: Quick lookup, not explanations

## Breaking Changes
- Maintain backward compatibility within minor versions
- Document breaking changes in release notes before tagging
- Update all docs/examples when behavior changes

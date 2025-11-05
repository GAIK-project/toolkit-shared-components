**IMPORTANT:** Keep this concise cheat sheet current so agents ship code safely.

## Architecture & Conventions
- Package lives in `gaik-py/src/gaik`
- Two modules: `providers/` (LLM adapters + registry) and `extract/` (SchemaExtractor API)
- Providers share `_build_model_kwargs()` helper and must register in `gaik/providers/__init__.py`
- Default models: OpenAI `gpt-4.1`, Anthropic `claude-sonnet-4-5-20250929`, Google `gemini-2.5-flash`, Azure `gpt-4.1`
- Never pass `api_key=None`; rely on env vars so LangChain loads keys automatically

## Provider Extension Checklist
1. Create `gaik/providers/<name>.py` implementing `LLMProvider.create_chat_model()`
2. Use `_build_model_kwargs()` to merge model + kwargs safely
3. Add dependency (e.g., `langchain-<name>`) to `pyproject.toml`
4. Register provider in `gaik/providers/__init__.py`
5. Smoke test with `examples/demo_anthropic.py` pattern

## Testing & Tooling
- Quick regression: `python examples/01_getting_started.py`
- Provider demo: `python examples/demo_anthropic.py`
- Packaging sanity: `cd gaik-py && python -m build && twine check dist/*`
- CI pipeline: GitHub Actions → version check → tests → build → publish (Test PyPI)

## Release Flow
1. Update version in `gaik-py/pyproject.toml`
2. Commit change and tag `vX.Y.Z`, push tag + main
3. GH Actions publishes to Test PyPI
4. Create GitHub release notes after pipeline succeeds

## Guardrails
- Keep `gaik.extract` API backward compatible within minor versions
- Sync docs/examples whenever behavior changes
- No secrets in repo; rely on env variables
- Document any breaking change in release notes before tagging

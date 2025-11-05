**IMPORTANT:** Keep this updated with architecture changes — this is the source of truth for AI agents.

## Project Snapshot
- Multi-provider AI toolkit for structured data extraction (OpenAI, Anthropic, Google, Azure)
- Ships PyPI distribution from `gaik-py/src/gaik` via GitHub Actions
- Built on LangChain with `.with_structured_output()` API
- Current version: **0.2.5** (optional user_description parameter)

## Tech Stack
- Python 3.10+, LangChain, Pydantic
- GitHub Actions: validates version → tests → build → publish to Test PyPI
- `pyproject.toml` defines all dependencies
- Version validation via `gaik-py/tests/validate_version.py`

## Architecture
```
gaik/
├── providers/    # Shared LLM provider registry (OpenAI, Anthropic, etc.)
│   ├── base.py   # LLMProvider base class with _build_model_kwargs()
│   ├── openai.py, anthropic.py, google.py, azure.py
│   └── __init__.py  # PROVIDERS registry dict
└── extract/      # Dynamic schema extraction module
    ├── extractor.py  # SchemaExtractor (main API)
    ├── models.py     # ExtractionRequirements, FieldSpec
    └── utils.py      # create_extraction_model()
```

## Key Conventions
- **Providers**: All in `gaik/providers/`, registry in `__init__.py`
- **Default models**: OpenAI=gpt-4.1, Anthropic=claude-sonnet-4-5-20250929, Google=gemini-2.5-flash
- **Dependencies**: All providers in core deps (no optional extras)
- **Version sync**: `pyproject.toml` version must match git tag (v0.2.5 = 0.2.5)
- **API key handling**: Never pass `api_key=None` explicitly - let LangChain read from env

## Adding New Provider
1. Create `gaik/providers/yourprovider.py` with `LLMProvider` subclass
2. Implement `create_chat_model()` using `_build_model_kwargs()` helper
3. Add `langchain-yourprovider>=x.x.x` to `dependencies` in `pyproject.toml`
4. Register in `gaik/providers/__init__.py` PROVIDERS dict
5. Test with `examples/demo_anthropic.py` pattern

## Testing
- **Quick test**: `python examples/01_getting_started.py`
- **Full demo**: `python examples/demo_anthropic.py` (shows all features)
- **Build**: `cd gaik-py && python -m build && twine check dist/*`
- **CI**: Workflow validates version, tests registry, builds, publishes

## Release Workflow
1. Update version in `pyproject.toml` (e.g., 0.2.6)
2. Commit: `git commit -m "chore: Bump version to 0.2.6"`
3. Tag: `git tag v0.2.6 && git push origin main v0.2.6`
4. GitHub Actions validates tag matches version, then publishes to Test PyPI
5. Create release: `gh release create v0.2.6 --title "..." --notes "..."`

## Key API Changes
- **v0.2.5**: `user_description` is now optional when `requirements` is provided
  - Before: `SchemaExtractor("", requirements=req)` 
  - After: `SchemaExtractor(requirements=req)`
- **v0.2.4**: Added Literal type hints for `provider` parameter (IDE autocomplete)
- **v0.2.3**: Fixed API key handling - providers now work with python-dotenv

## Rules
- Keep `gaik.extract` API backward compatible (minor versions)
- Update examples when adding features
- Never commit secrets/tokens
- Test before pushing packaging changes
- Document breaking changes in release notes

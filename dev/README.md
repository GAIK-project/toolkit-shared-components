# Dev Folder Quick Guide

Use `dev/` for work that is not ready for `packages/python/gaik/src/gaik/`. Ship code only after it meets the promotion checklist below.

## When to use each folder

| Location                         | Use it for                                       |
| -------------------------------- | ------------------------------------------------ |
| `dev/`                           | Prototypes and features under active development |
| `packages/python/gaik/src/gaik/` | Stable code published to PyPI                    |
| `examples/`                      | Short runnable usage demos                       |

## Layout

```text
dev/
├── experimental/  # Throwaway spikes
├── features/      # Planned features progressing to release
└── README.md
```

## Promotion checklist

- Feature works, handles edge cases, and fails cleanly
- Code matches gaik style with type hints and docstrings where needed
- Example added under `examples/`
- Tests or manual verification complete
- Required dependencies captured in `packages/python/gaik/pyproject.toml`

## Minimal workflow

1. Build in `dev/features/<feature>` (or `experimental/` for spikes)
2. Install editable package: `cd packages/python/gaik && pip install -e .`
3. Run targeted scripts or tests against the feature
4. Add an example and docs as part of promotion
5. Move code into `packages/python/gaik/src/gaik/` only after checklist passes

## Ground rules

- Keep `dev/` tidy; delete stale work
- Never import `dev/` modules from `packages/python/gaik`
- Do not commit secrets or credentials
- Prefer small, reviewable changes over large drops

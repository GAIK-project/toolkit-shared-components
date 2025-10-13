# Toolkit Shared Components

One place where we share Python and TypeScript components for every team project.

## Why not copy/paste?

- Single source of truth: bug fixes and improvements land once and flow to every project.
- Versioned releases: each project can pin or upgrade confidently.
- Easier maintenance: imports, docs, and tests travel together.
- Ready-to-install packages: no manual syncing or cherry-picking.

## Install packages

- Python: `pip install "git+https://github.com/GAIK-project/toolkit-shared-components.git#subdirectory=gaik-py"`
- TypeScript: `pnpm add github:GAIK-project/toolkit-shared-components`

Use `@v0.2.0` to pin a specific version (e.g. `pip install git+…@v0.2.0#subdirectory=gaik-py`).

## Need to publish a component?

- Follow the step-by-step deployment guide in `deployment.md`.
- TL;DR: add your component, run tests, bump the version, tag a release, and update release notes.

## Repository Contents

- `gaik-py`: shared Python components and tests
- `gaik-ts`: shared TypeScript components and tests
- `gaik-demo`: Docker app with both packages preinstalled for demos

## Release Cheat Sheet

1. Make sure `main` is up to date and tests pass.
2. Update the version files.
3. `git commit` and `git tag vX.Y.Z`.
4. `git push origin main --tags`.
5. Open GitHub `Releases`, pick the tag, and add highlights.

GitHub automatically provides zip/tarball downloads and supports attaching binaries to the release [[1]](#references).

## Using Components in Projects

- Keep dependencies pinned in `requirements.txt` / `package.json`.
- When a new release drops, bump the version and review the release notes.
- Fixes should land here first, then propagate via version bumps.

## Example: Python Whisper Transcription Component

1. Install the shared package:

```bash
pip install "git+https://github.com/GAIK-project/toolkit-shared-components.git#subdirectory=gaik-py"
```

2. Add the shared helper in `gaik-py/src/gaik/audio/whisper.py` (dependency pinned in `gaik-py/requirements.txt`):

```python
from functools import lru_cache
from pathlib import Path

import whisper


@lru_cache(maxsize=1)
def _load_model(model_name: str = "base") -> whisper.Whisper:
    return whisper.load_model(model_name)


def transcribe_audio(audio_path: str | Path, model_name: str | None = None) -> str:
    audio_path = Path(audio_path)
    model = _load_model(model_name or "base")
    result = model.transcribe(str(audio_path))
    return result["text"].strip()
```

3. Consume it in any project:

```python
from gaik.audio.whisper import transcribe_audio

print(transcribe_audio("samples/meeting.wav"))
```

## References

1. <a name="references"></a>GitHub Docs: About releases. https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

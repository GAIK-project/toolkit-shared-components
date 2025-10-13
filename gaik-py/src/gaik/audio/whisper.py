"""Reusable helpers for Whisper-based audio transcription."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Final

import whisper

# Default model name used by this helper. Override in the consumer code if needed.
_DEFAULT_MODEL: Final[str] = "base"


@lru_cache(maxsize=1)
def _load_model(model_name: str = _DEFAULT_MODEL) -> whisper.Whisper:
    """Load and cache the Whisper model to avoid repeated downloads."""

    return whisper.load_model(model_name)


def transcribe_audio(audio_path: str | Path, model_name: str | None = None) -> str:
    """Return the transcription for a single audio file."""

    audio_path = Path(audio_path)
    model = _load_model(model_name or _DEFAULT_MODEL)
    result = model.transcribe(str(audio_path))
    return result["text"].strip()


__all__ = ["transcribe_audio"]


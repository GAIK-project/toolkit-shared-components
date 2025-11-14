#!/usr/bin/env python3
"""Smoke test that gaik installs and exposes its public API."""

from __future__ import annotations

from gaik import __version__
from gaik.extract import (ExtractionRequirements, FieldSpec,
                          create_extraction_model)
from gaik.providers import PROVIDERS, get_provider


def run_checks() -> None:
    print(f"gaik version detected: {__version__}")

    # Validate Pydantic models can be constructed
    field_name = FieldSpec(
        field_name="name",
        field_type="str",
        description="Person name",
        required=True,
    )
    field_age = FieldSpec(
        field_name="age",
        field_type="int",
        description="Person age",
        required=False,
    )

    requirements = ExtractionRequirements(
        use_case_name="InstallSmokeTest",
        fields=[field_name, field_age],
    )

    model = create_extraction_model(requirements)
    instance = model(name="Test User", age=30)
    assert instance.name == "Test User"
    assert instance.age == 30

    # Provider registry sanity check
    expected = {"openai", "anthropic", "google", "azure"}
    missing = expected.difference(PROVIDERS)
    if missing:
        raise RuntimeError(f"Provider registry missing entries: {sorted(missing)}")

    provider = get_provider("openai")
    if not hasattr(provider, "create_chat_model"):
        raise RuntimeError("Provider object missing required API")

    print("✅ verify_installation checks passed")


if __name__ == "__main__":
    run_checks()

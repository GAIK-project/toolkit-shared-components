"""Utility functions for creating dynamic Pydantic models.

This module provides helper functions for sanitizing model names and creating
dynamic Pydantic schemas from field specifications.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field, create_model

if TYPE_CHECKING:
    from gaik.extract.models import ExtractionRequirements


def sanitize_model_name(name: str) -> str:
    """Sanitize model name to match OpenAI's requirements.

    Only alphanumeric, underscores, and hyphens are allowed.
    Removes invalid characters and normalizes the name.

    Args:
        name: The raw model name to sanitize

    Returns:
        A sanitized model name safe for OpenAI API

    Example:
        >>> sanitize_model_name("My Project! (2024)")
        'My_Project_2024'
    """
    # Replace spaces and other characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
    # Remove consecutive underscores
    sanitized = re.sub(r"_+", "_", sanitized)
    # Remove leading/trailing underscores
    sanitized = sanitized.strip("_")
    return sanitized


def create_extraction_model(requirements: ExtractionRequirements) -> type[BaseModel]:
    """Create a Pydantic model dynamically from field specifications.

    This is type-safe and doesn't require code generation or eval().
    The resulting model can be used with OpenAI's structured outputs API.

    Args:
        requirements: Extraction requirements containing field specifications

    Returns:
        A dynamically created Pydantic model class

    Example:
        >>> from gaik.extract.models import ExtractionRequirements, FieldSpec
        >>> requirements = ExtractionRequirements(
        ...     use_case_name="Invoice",
        ...     fields=[
        ...         FieldSpec(
        ...             field_name="invoice_number",
        ...             field_type="str",
        ...             description="The invoice number",
        ...             required=True
        ...         ),
        ...         FieldSpec(
        ...             field_name="amount",
        ...             field_type="float",
        ...             description="Total amount in USD",
        ...             required=True
        ...         )
        ...     ]
        ... )
        >>> invoice_model = create_extraction_model(requirements)
        >>> invoice_model.__name__
        'Invoice_Extraction'
    """
    # Map string type names to actual Python types
    type_mapping = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "list[str]": list[str],
    }

    # Build field definitions for create_model()
    field_definitions = {}

    for field_spec in requirements.fields:
        python_type = type_mapping[field_spec.field_type]

        if field_spec.required:
            # Required field
            field_definitions[field_spec.field_name] = (
                python_type,
                Field(description=field_spec.description),
            )
        else:
            # Optional field
            field_definitions[field_spec.field_name] = (
                python_type | None,
                Field(default=None, description=field_spec.description),
            )

    # Sanitize the model name for OpenAI compatibility
    model_name = sanitize_model_name(requirements.use_case_name) + "_Extraction"

    # Create the model dynamically using Pydantic's built-in method
    dynamic_model = create_model(
        model_name,
        __doc__=f"Extraction model for {requirements.use_case_name}",
        **field_definitions,
    )

    return dynamic_model


__all__ = ["sanitize_model_name", "create_extraction_model"]

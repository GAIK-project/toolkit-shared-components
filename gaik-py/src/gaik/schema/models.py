"""Pydantic models for dynamic schema extraction.

This module defines the data structures used to specify extraction requirements
and field specifications for creating dynamic Pydantic schemas.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class FieldSpec(BaseModel):
    """Specification for a single field to extract.

    Attributes:
        field_name: Snake_case field name (e.g., 'project_title')
        field_type: Python type for this field
        description: What this field represents and how to extract it
        required: Whether this field is required in the extraction
    """

    field_name: str = Field(description="Snake_case field name (e.g., 'project_title')")
    field_type: Literal["str", "int", "float", "bool", "list[str]"] = Field(
        description="Python type for this field"
    )
    description: str = Field(description="What this field represents")
    required: bool = Field(default=True, description="Whether this field is required")


class ExtractionRequirements(BaseModel):
    """Parsed extraction requirements from user input.

    Attributes:
        use_case_name: Name for this extraction use case
        fields: List of fields to extract from documents
    """

    use_case_name: str = Field(description="Name for this extraction use case")
    fields: list[FieldSpec] = Field(description="List of fields to extract")


__all__ = ["FieldSpec", "ExtractionRequirements"]

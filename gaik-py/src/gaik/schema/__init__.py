"""Dynamic schema extraction with OpenAI structured outputs.

This module provides tools for extracting structured data from unstructured text
using dynamically created Pydantic schemas and OpenAI's structured outputs API.

Benefits of this approach:
- Type-safe and guaranteed structure (enforced by the API)
- Cost-effective (fewer tokens, no code generation)
- Secure (no eval/exec needed)
- Simple and maintainable
- Reliable results with automatic retries

Quick Start:
    >>> from gaik.schema import dynamic_extraction_workflow
    >>>
    >>> results = dynamic_extraction_workflow(
    ...     user_description="Extract title, date, and author from articles",
    ...     documents=[doc1, doc2, doc3]
    ... )

Advanced Usage:
    >>> from gaik.schema import SchemaExtractor
    >>>
    >>> # Reuse the same schema for multiple batches
    >>> extractor = SchemaExtractor("Extract invoice number and amount")
    >>> batch1 = extractor.extract(documents1)
    >>> batch2 = extractor.extract(documents2)

Custom Field Specifications:
    >>> from gaik.schema import (
    ...     FieldSpec,
    ...     ExtractionRequirements,
    ...     create_extraction_model,
    ... )
    >>>
    >>> fields = [
    ...     FieldSpec(
    ...         field_name="invoice_number",
    ...         field_type="str",
    ...         description="Extract invoice ID",
    ...         required=True
    ...     )
    ... ]
    >>> requirements = ExtractionRequirements(
    ...     use_case_name="Invoice",
    ...     fields=fields
    ... )
    >>> model = create_extraction_model(requirements)
"""

from gaik.schema.extractor import SchemaExtractor, dynamic_extraction_workflow
from gaik.schema.models import ExtractionRequirements, FieldSpec
from gaik.schema.utils import create_extraction_model, sanitize_model_name

__all__ = [
    # Main API
    "SchemaExtractor",
    "dynamic_extraction_workflow",
    # Models
    "FieldSpec",
    "ExtractionRequirements",
    # Utilities
    "create_extraction_model",
    "sanitize_model_name",
]

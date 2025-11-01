"""Dynamic data extraction with OpenAI structured outputs.

This module provides tools for extracting structured data from unstructured text
using dynamically created Pydantic schemas and OpenAI's structured outputs API.

Benefits of this approach:
- Type-safe and guaranteed structure (enforced by the API)
- Cost-effective (fewer tokens, no code generation)
- Secure (no eval/exec needed)
- Simple and maintainable
- Reliable results with automatic retries

Quick Start:
    >>> from gaik.extract import dynamic_extraction_workflow
    >>>
    >>> results = dynamic_extraction_workflow(
    ...     user_description="Extract title, date, and author from articles",
    ...     documents=[doc1, doc2, doc3]
    ... )

Advanced Usage:
    >>> from gaik.extract import SchemaExtractor
    >>>
    >>> # Reuse the same schema for multiple batches
    >>> extractor = SchemaExtractor("Extract invoice number and amount")
    >>> batch1 = extractor.extract(documents1)
    >>> batch2 = extractor.extract(documents2)
    >>>
    >>> # Access the generated Pydantic model
    >>> schema = extractor.model.model_json_schema()
    >>> print(schema)

Custom Field Specifications:
    >>> from gaik.extract import (
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

from gaik.extract.extractor import SchemaExtractor, dynamic_extraction_workflow
from gaik.extract.models import ExtractionRequirements, FieldSpec
from gaik.extract.utils import create_extraction_model, sanitize_model_name

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

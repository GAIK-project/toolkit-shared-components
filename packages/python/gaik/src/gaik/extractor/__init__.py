"""
Knowledge Extraction Using Dynamic Schema Generation

Extract structured data from documents using natural language requirements.
Automatically generates Pydantic schemas and validates extracted data.
"""

from .config import get_openai_config, create_openai_client
from .schema import SchemaGenerator
from .extractor import DataExtractor

__all__ = [
    "get_openai_config",
    "create_openai_client",
    "SchemaGenerator",
    "DataExtractor",
]

__version__ = "0.1.0"

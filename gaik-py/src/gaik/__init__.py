"""General AI Kit (GAIK) - Reusable AI/ML components for Python.

GAIK provides modular, production-ready tools for common AI/ML tasks including:
- Dynamic data extraction with structured outputs
- And more modules coming soon...

Available modules:
    - gaik.extract: Dynamic data extraction with OpenAI structured outputs

Example:
    >>> from gaik.extract import SchemaExtractor
    >>> extractor = SchemaExtractor("Extract title and date from articles")
    >>> results = extractor.extract(documents)
"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("gaik")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0.dev"

__all__ = ["__version__"]

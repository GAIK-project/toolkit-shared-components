"""General AI Kit (GAIK) - Reusable AI/ML components for Python.

GAIK provides modular, production-ready tools for common AI/ML tasks including:
- Dynamic schema extraction with structured outputs
- And more modules coming soon...

Available modules:
    - gaik.schema: Dynamic schema extraction with OpenAI structured outputs

Example:
    >>> from gaik.schema import SchemaExtractor
    >>> extractor = SchemaExtractor("Extract title and date from articles")
    >>> results = extractor.extract(documents)
"""

__version__ = "0.1.0"
__author__ = "GAIK Project"
__license__ = "MIT"

__all__ = ["__version__", "__author__", "__license__"]

"""General AI Kit (GAIK) - AI/ML toolkit for Python.

AI toolkit with structured data extraction and document parsing using OpenAI/Azure OpenAI.

Modules:
    - gaik.extractor: Schema generation and structured data extraction
    - gaik.parsers: PDF to Markdown parsing (vision models, PyMuPDF, Docling)

Example - Schema-based Extraction:
    >>> from gaik.extractor import SchemaGenerator, DataExtractor, get_openai_config
    >>> config = get_openai_config(use_azure=True)
    >>> generator = SchemaGenerator(config=config)
    >>> schema = generator.generate_schema("Extract name and age")
    >>> extractor = DataExtractor(config=config)
    >>> results = extractor.extract(
    ...     extraction_model=schema,
    ...     requirements=generator.item_requirements,
    ...     user_requirements="Extract name and age",
    ...     documents=["Alice is 25 years old"]
    ... )

Example - PDF Parsing:
    >>> from gaik.parsers import VisionParser, get_openai_config
    >>> config = get_openai_config(use_azure=True)
    >>> parser = VisionParser(openai_config=config)
    >>> pages = parser.convert_pdf("document.pdf")
"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("gaik")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0.dev"

# Expose submodules for cleaner imports
from . import extractor
from . import parsers

__all__ = [
    "__version__",
    "extractor",
    "parsers",
]

"""Reusable parsers for documents and images.

This module provides:
- VisionParser: Convert PDFs to Markdown using OpenAI vision models
- PyMuPDFParser: Fast local PDF text extraction using PyMuPDF
"""

from .vision import OpenAIConfig, VisionParser, get_openai_config
from .pymypdf import PyMuPDFParser, parse_pdf

__all__ = [
    "OpenAIConfig",
    "VisionParser",
    "get_openai_config",
    "PyMuPDFParser",
    "parse_pdf",
]

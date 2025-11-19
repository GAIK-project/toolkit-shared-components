"""Reusable parsers for documents and images.

This module provides:
- VisionParser: Convert PDFs to Markdown using OpenAI vision models
- PyMuPDFParser: Fast local PDF text extraction using PyMuPDF
- DoclingParser: Advanced document parsing with OCR, table extraction, and multi-format support
"""

from .docling import DoclingParser, parse_document
from .pymypdf import PyMuPDFParser, parse_pdf
from .vision import OpenAIConfig, VisionParser, get_openai_config

__all__ = [
    "OpenAIConfig",
    "VisionParser",
    "get_openai_config",
    "PyMuPDFParser",
    "parse_pdf",
    "DoclingParser",
    "parse_document",
]

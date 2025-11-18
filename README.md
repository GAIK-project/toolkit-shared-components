# GAIK - General AI Kit

[![PyPI version](https://badge.fury.io/py/gaik.svg)](https://pypi.org/project/gaik/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/GAIK-project/gaik-toolkit/actions/workflows/test.yml/badge.svg)](https://github.com/GAIK-project/gaik-toolkit/actions)

Multi-provider AI toolkit for Python - structured data extraction and document parsing with OpenAI, Anthropic, Google, and Azure.

## Install

```bash
pip install gaik[extract]  # Extraction features
pip install gaik[parser]   # PDF/document parsing
pip install gaik[all]      # All features
```

## Quick Start

```python
from gaik.extract import SchemaExtractor

# Set API key: export OPENAI_API_KEY='sk-...'
extractor = SchemaExtractor("Extract name and age from text")
result = extractor.extract_one("Alice is 25 years old")
print(result)  # {'name': 'Alice', 'age': 25}
```

## Features

- **Multi-provider** - OpenAI, Anthropic, Google, Azure
- **Type-safe** - Pydantic models, API-enforced schemas
- **Document parsing** - PDF to Markdown with vision models
- **Simple API** - Natural language to structured data

## Documentation

- **Full API Reference**: [packages/python/gaik/README.md](packages/python/gaik/README.md)
- **Examples**: [examples/](examples/)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)

## How It Works

```mermaid
graph LR
    A[GAIK Library<br/>Development] -->|Build & Release| B[PyPI<br/>gaik package]
    B -->|pip install gaik| C[Your Project]
    C -->|Simple Import| D[from gaik.extract import SchemaExtractor]

    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#e8f5e9
    style D fill:#f3e5f5
```

**No copy-paste needed** - Just install from PyPI and import. We maintain the library, you use it.

## Repository Structure

```
gaik-toolkit/
├── packages/python/gaik/  # Python package
│   ├── src/gaik/
│   │   ├── extract/       # Data extraction
│   │   ├── providers/     # LLM providers
│   │   └── parsers/       # Vision/PDF parsing
│   └── pyproject.toml
├── examples/              # Usage examples
├── scripts/               # CI/build scripts
└── .github/workflows/     # CI/CD
```

## License

MIT - see [LICENSE](LICENSE)

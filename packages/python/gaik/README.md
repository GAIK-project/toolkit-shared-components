# GAIK - General AI Kit

Multi-provider AI toolkit for Python with structured data extraction and document parsing.

## Installation

```bash
# Extract features (OpenAI, Anthropic, Google, Azure)
pip install gaik[extract]

# PDF parsing
pip install gaik[parser]

# All features
pip install gaik[all]
```

## Quick Start

### Extract Data

```python
from gaik.extract import SchemaExtractor

# Set API key first: export OPENAI_API_KEY='sk-...'
extractor = SchemaExtractor("Extract name and age from text")
result = extractor.extract_one("Alice is 25 years old")
print(result)  # {'name': 'Alice', 'age': 25}

# Switch provider
extractor = SchemaExtractor("Extract name and age", provider="anthropic")  # or "google", "azure"
```

### Parse PDF to Markdown

```python
from gaik.parsers import VisionParser, get_openai_config

# Set environment: AZURE_API_KEY, AZURE_ENDPOINT, AZURE_DEPLOYMENT
config = get_openai_config(use_azure=True)
parser = VisionParser(config)

pages = parser.convert_pdf("invoice.pdf", clean_output=True)
markdown = "\n\n".join(pages)
```

### Fast Local PDF Parsing

```python
from gaik.parsers import PyMuPDFParser

parser = PyMuPDFParser()
result = parser.parse_document("document.pdf")
print(result["text_content"])
```

## Features

### 🔍 Structured Data Extraction

- **Multi-provider** - OpenAI, Anthropic, Google, Azure
- **Type-safe** - Full Pydantic validation
- **API-enforced** - Guaranteed schema compliance
- **Simple** - Natural language to structured data

### 📄 Document Parsing

- **VisionParser** - PDF to Markdown using vision models
- **PyMuPDFParser** - Fast local text extraction
- **No external binaries** - Pure Python dependencies

## API Reference

### Extraction

```python
SchemaExtractor(
    user_description: str,
    provider: Literal["openai", "anthropic", "google", "azure"] = "openai",
    model: str | None = None,
    api_key: str | None = None,
)
```

**Methods:**
- `extract_one(text: str) -> dict` - Extract from single text
- `extract(texts: list[str]) -> list[dict]` - Batch extraction
- `field_names` - List of field names
- `model` - Generated Pydantic model

### Vision Parser

```python
VisionParser(
    config: OpenAIConfig,
    custom_prompt: str | None = None,
    use_context: bool = True,
    max_tokens: int = 16_000,
)
```

**Methods:**
- `convert_pdf(pdf_path: str, dpi: int = 200, clean_output: bool = True) -> list[str]`
- `save_markdown(pages: list[str], output_path: str)`

**Config Helper:**
```python
get_openai_config(use_azure: bool = True) -> OpenAIConfig
```

### PyMuPDF Parser

```python
PyMuPDFParser()
```

**Methods:**
- `parse_document(file_path: str) -> dict` - Extract text and metadata

## Environment Variables

| Provider | Variables |
|----------|-----------|
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| Google | `GOOGLE_API_KEY` |
| Azure | `AZURE_API_KEY`, `AZURE_ENDPOINT`, `AZURE_DEPLOYMENT` |

## Default Models

| Provider | Model |
|----------|-------|
| OpenAI | `gpt-4.1` |
| Anthropic | `claude-sonnet-4-5-20250929` |
| Google | `gemini-2.5-flash` |
| Azure | User's deployment |

## Batch Processing

```python
extractor = SchemaExtractor("""
Extract:
- invoice_number: Invoice ID
- amount: Total in USD
- vendor: Company name
""")

documents = [
    "Invoice #12345 from Acme Corp. Total: $1,500",
    "INV-67890, Supplier: TechCo, Amount: $2,750"
]

results = extractor.extract(documents)
for result in results:
    print(f"Invoice: {result['invoice_number']}, Amount: ${result['amount']}")
```

## Schema Inspection

```python
extractor = SchemaExtractor("Extract name and age")

# Field names
print(extractor.field_names)  # ['name', 'age']

# JSON schema
schema = extractor.model.model_json_schema()

# Field specs
for field in extractor.fields:
    print(f"{field.field_name}: {field.field_type}")
```

## Advanced Usage

### Custom Prompt for Vision Parser

```python
custom_prompt = """
Convert document to markdown:
- Preserve all tables
- Include headers and footers
- Maintain layout structure
"""

parser = VisionParser(config, custom_prompt=custom_prompt)
```

### Pre-defined Schema

```python
from gaik.extract import FieldSpec, ExtractionRequirements, create_extraction_model

requirements = ExtractionRequirements(
    use_case_name="Invoice",
    fields=[
        FieldSpec("invoice_number", "str", "Invoice ID", required=True),
        FieldSpec("amount", "float", "Total amount", required=True),
    ]
)

InvoiceModel = create_extraction_model(requirements)
extractor = SchemaExtractor(requirements=requirements)
```

## Resources

- **Examples**: [examples/](../../examples/)
- **Repository**: [github.com/GAIK-project/gaik-toolkit](https://github.com/GAIK-project/gaik-toolkit)
- **Contributing**: [CONTRIBUTING.md](../../../CONTRIBUTING.md)

## License

MIT - see [LICENSE](../../../LICENSE)

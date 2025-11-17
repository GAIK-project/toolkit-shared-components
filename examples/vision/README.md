# Vision Parser Examples

Convert PDFs to Markdown using OpenAI/Azure vision models.

## Setup

```bash
pip install gaik[parser]
```

## Environment

```bash
# OpenAI
export OPENAI_API_KEY='sk-...'

# Azure OpenAI (all 3 required)
export AZURE_API_KEY='...'
export AZURE_ENDPOINT='https://...'
export AZURE_DEPLOYMENT='gpt-4o'
```

## Examples

### Simple Demo
```bash
python demo_vision_simple.py
```

### CLI Tool
```bash
# Basic usage
python demo_vision_parser.py invoice.pdf

# Advanced options
python demo_vision_parser.py invoice.pdf --output result.md
python demo_vision_parser.py invoice.pdf --openai  # Use OpenAI instead of Azure
python demo_vision_parser.py invoice.pdf --no-clean  # Skip LLM cleanup
```

## Files

- `demo_vision_simple.py` - Basic PDF→Markdown conversion
- `demo_vision_parser.py` - CLI with advanced options
- `WEF-page-10.pdf` - Sample PDF for testing

# Examples

Quick examples to get started with GAIK.

## Setup

### Option 1: Development Installation (recommended for testing)

If you're developing or testing the latest code:

```bash
# From the repository root
cd packages/python/gaik
pip install -e ".[all]"

# Set API keys (choose what you need)
export OPENAI_API_KEY='sk-...'           # OpenAI
export ANTHROPIC_API_KEY='sk-ant-...'   # Anthropic
export GOOGLE_API_KEY='...'              # Google
```

### Option 2: Install from PyPI

For stable releases:

```bash
# Install package
pip install gaik[extract]

# For vision/PDF parsing
pip install gaik[parser]

# Set API key (choose one)
export OPENAI_API_KEY='sk-...'           # OpenAI
export ANTHROPIC_API_KEY='sk-ant-...'   # Anthropic
export GOOGLE_API_KEY='...'              # Google
```

## Running Examples

### Extraction

```bash
python examples/extract/demo_anthropic.py
```

### Vision/PDF Parsing

```bash
# Simple demo
python examples/vision/demo_vision_simple.py

# CLI tool
python examples/vision/demo_vision_parser.py your-file.pdf
```

## Available Examples

| Category | File | Description |
|----------|------|-------------|
| Extract | `extract/demo_anthropic.py` | Structured data extraction demo |
| Vision | `vision/demo_vision_simple.py` | Basic PDF to Markdown |
| Vision | `vision/demo_vision_parser.py` | Advanced CLI tool |

## Full Documentation

See [packages/python/gaik/README.md](../packages/python/gaik/README.md) for complete API reference and detailed usage.

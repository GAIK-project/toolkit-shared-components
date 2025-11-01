# GAIK Examples

This directory contains example scripts demonstrating various use cases of the GAIK library.

## Available Examples

### 1. `test_gaik_installation.py`
Tests basic functionality without making API calls. Perfect for:
- Verifying installation
- Understanding the API structure
- Testing without an OpenAI API key

**Run it:**
```bash
python test_gaik_installation.py
```

### 2. `test_real_extraction.py`
Demonstrates real extraction with OpenAI API calls. Shows:
- Simple extraction with `SchemaExtractor`
- Using `dynamic_extraction_workflow`
- Batch processing multiple documents

**Requirements:**
- OpenAI API key in environment or `.env` file
- `python-dotenv` package

**Run it:**
```bash
# Set your API key
export OPENAI_API_KEY='sk-...'

# Run the example
python test_real_extraction.py
```

## More Information

- [Main Documentation](../gaik-py/README.md)
- [GitHub Repository](https://github.com/GAIK-project/toolkit-shared-components)

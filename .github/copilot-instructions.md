## Monorepo Structure
```
gaik-toolkit/
├── packages/python/gaik/     # PyPI package source
│   ├── src/gaik/
│   │   ├── extract/          # Schema extraction
│   │   ├── providers/        # LLM integrations
│   │   └── parsers/          # PDF/document parsing
│   └── pyproject.toml        # Package config
├── examples/                 # Usage examples
└── .github/workflows/        # CI/CD pipelines
```

## Core APIs
```python
# Extraction
from gaik.extract import SchemaExtractor
extractor = SchemaExtractor("Extract name and age", provider="anthropic")
results = extractor.extract(["Alice is 25"])

# Parsing
from gaik.parsers.pymypdf import PyMuPDFParser
parser = PyMuPDFParser()
result = parser.parse_document("document.pdf")
```

## Local Development
```bash
cd packages/python/gaik
pip install -e .[all,dev]
pytest                     # Run tests
ruff check --fix .         # Lint
python -m build            # Build package
```

## Publishing
```bash
git tag v0.3.0             # Tag format: vX.Y.Z
git push origin v0.3.0     # Triggers GitHub Actions
```

GitHub Actions auto-publishes to PyPI and creates release.

"""Test gaik with real LLM API calls (OpenAI, Anthropic, Google)."""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file in project root
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")

from gaik.extract import SchemaExtractor, dynamic_extraction_workflow


def test_simple_extraction():
    """Test simple extraction with SchemaExtractor (default OpenAI)."""
    print("Test 1: Simple person extraction (OpenAI)")
    print("-" * 60)

    extractor = SchemaExtractor("""
    Extract from the text:
    - Person's name
    - Age (as number)
    - City where they live
    """)

    doc = "John Doe is 32 years old and lives in Helsinki."

    result = extractor.extract_one(doc)
    print(f"Input: {doc}")
    print(f"Result: {result}")
    print()


def test_anthropic_extraction():
    """Test extraction with Anthropic Claude."""
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Test 1b: Anthropic extraction - SKIPPED (no API key)")
        print("-" * 60)
        return

    print("Test 1b: Simple extraction (Anthropic Claude)")
    print("-" * 60)

    extractor = SchemaExtractor(
        """
        Extract from the text:
        - Person's name
        - Age (as number)
        - City where they live
        """,
        provider="anthropic"
    )

    doc = "Jane Smith is 28 years old and lives in London."

    result = extractor.extract_one(doc)
    print(f"Input: {doc}")
    print(f"Result: {result}")
    print()


def test_google_extraction():
    """Test extraction with Google Gemini."""
    if not os.getenv("GOOGLE_API_KEY"):
        print("Test 1c: Google extraction - SKIPPED (no API key)")
        print("-" * 60)
        return

    print("Test 1c: Simple extraction (Google Gemini)")
    print("-" * 60)

    extractor = SchemaExtractor(
        """
        Extract from the text:
        - Person's name
        - Age (as number)
        - City where they live
        """,
        provider="google"
    )

    doc = "Bob Johnson is 45 years old and lives in Tokyo."

    result = extractor.extract_one(doc)
    print(f"Input: {doc}")
    print(f"Result: {result}")
    print()


def test_azure_extraction():
    """Test extraction with Azure OpenAI."""
    # Support both AZURE_OPENAI_* and AZURE_* env variable patterns
    has_azure = os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("AZURE_API_KEY")

    if not has_azure:
        print("Test 1d: Azure extraction - SKIPPED (no API key)")
        print("-" * 60)
        return

    print("Test 1d: Simple extraction (Azure OpenAI)")
    print("-" * 60)

    # Build Azure configuration
    azure_config = {}
    if os.getenv("AZURE_API_KEY"):
        azure_config["api_key"] = os.getenv("AZURE_API_KEY")
    if os.getenv("AZURE_API_BASE"):
        azure_config["azure_endpoint"] = os.getenv("AZURE_API_BASE")

    # Azure requires a deployment name - using gpt-4 as default
    azure_config["azure_deployment"] = os.getenv("AZURE_DEPLOYMENT", "gpt-4")

    try:
        extractor = SchemaExtractor(
            """
            Extract from the text:
            - Person's name
            - Age (as number)
            - City where they live
            """,
            provider="azure",
            **azure_config
        )

        doc = "Emma Wilson is 30 years old and lives in Stockholm."

        result = extractor.extract_one(doc)
        print(f"Input: {doc}")
        print(f"Result: {result}")
        print()
    except Exception as e:
        print(f"Azure extraction failed: {e}")
        print("Note: Azure requires proper deployment configuration")
        print()


def test_workflow():
    """Test with dynamic_extraction_workflow."""
    print("Test 2: Invoice extraction with workflow")
    print("-" * 60)

    description = """
    Extract from invoices:
    - Invoice number
    - Total amount in euros (as number)
    - Vendor name
    """

    documents = [
        "Invoice #12345 from Acme Corp. Total: 1500 EUR",
        "INV-67890, Supplier: TechCo Ltd, Amount: 2750.00 euros",
    ]

    results = dynamic_extraction_workflow(description, documents, verbose=True)

    print("\nExtracted results:")
    for i, result in enumerate(results, 1):
        print(f"\nDocument {i}:")
        for key, value in result.items():
            print(f"  {key}: {value}")


def test_multiple_documents():
    """Test extracting from multiple documents with same schema."""
    print("\n" + "=" * 60)
    print("Test 3: Batch extraction")
    print("=" * 60)

    extractor = SchemaExtractor("""
    Extract:
    - Product name
    - Price in USD (as number)
    - Rating from 1-5 (as number)
    """)

    documents = [
        "The SuperWidget costs $29.99 and has a rating of 4.5 stars",
        "MegaTool is priced at $149 with 5-star reviews",
        "Budget Gadget - only $9.99, rated 3 out of 5",
    ]

    results = extractor.extract(documents)

    print("\nExtracted from 3 product reviews:")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")


def test_schema_preview():
    """Show how the extractor schema can be inspected without running extraction."""
    print("\n" + "=" * 60)
    print("Schema preview (no extraction)")
    print("=" * 60)

    extractor = SchemaExtractor(
        """
        Extract details from press releases:
        - Announcement title
        - Organisation name
        - Publication date (ISO format)
        - Key themes (list of strings)
        """
    )

    schema = extractor.model.model_json_schema()

    print("Generated JSON Schema:")
    print(json.dumps(schema, indent=2))

    print("\nField names:")
    for field in extractor.field_names:
        print(f"- {field}")


if __name__ == "__main__":
    # Check if at least one API key is set
    has_openai = bool(os.getenv("OPENAI_API_KEY"))
    has_anthropic = bool(os.getenv("ANTHROPIC_API_KEY"))
    has_google = bool(os.getenv("GOOGLE_API_KEY"))
    has_azure = bool(os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("AZURE_API_KEY"))

    if not any([has_openai, has_anthropic, has_google, has_azure]):
        print("ERROR: No API keys found in environment variables!")
        print("Please set at least one in .env file or export it:")
        print("  export OPENAI_API_KEY='sk-...'")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        print("  export GOOGLE_API_KEY='...'")
        print("  export AZURE_API_KEY='...' (and AZURE_API_BASE='...')")
        exit(1)

    print("Testing gaik with real LLM API calls...")
    print("=" * 60)
    print(f"Available providers:")
    if has_openai:
        print("  [OK] OpenAI")
    if has_anthropic:
        print("  [OK] Anthropic")
    if has_google:
        print("  [OK] Google")
    if has_azure:
        print("  [OK] Azure OpenAI")
    print()

    try:
        if has_openai:
            test_simple_extraction()
        test_anthropic_extraction()
        test_google_extraction()
        test_azure_extraction()
        if has_openai:
            test_workflow()
            test_multiple_documents()
            test_schema_preview()

        print("\n" + "=" * 60)
        print("All tests completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback

        traceback.print_exc()

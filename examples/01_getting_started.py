"""GAIK Toolkit - Getting Started Example

This example demonstrates the core capabilities of the GAIK toolkit:
1. Creating a SchemaExtractor with natural language descriptions
2. Extracting structured data from unstructured text
3. Working with multiple providers (OpenAI, Anthropic, Google, Azure)
4. Accessing the generated Pydantic schema
5. Getting JSON Schema for integration with other tools

Requirements:
- Set at least one API key in .env file (see .env.example)
- Run: python examples/01_getting_started.py
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file in project root
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")

from gaik.extract import SchemaExtractor


def example_1_basic_extraction():
    """Example 1: Basic data extraction with natural language schema."""
    print("=" * 70)
    print("EXAMPLE 1: Basic Extraction")
    print("=" * 70)
    print()

    # Define what you want to extract using natural language
    description = """
    Extract the following information from text:
    - person_name: The full name of the person
    - age: The person's age as a number
    - city: The city where they live
    """

    # Create the extractor - it automatically generates a Pydantic schema
    extractor = SchemaExtractor(description)

    # Extract from text
    text = "John Doe is 32 years old and lives in Helsinki."
    result = extractor.extract_one(text)

    print(f"Input text: {text}")
    print(f"\nExtracted data:")
    print(f"  - Name: {result['person_name']}")
    print(f"  - Age: {result['age']}")
    print(f"  - City: {result['city']}")
    print()


def example_2_multiple_documents():
    """Example 2: Batch processing multiple documents."""
    print("=" * 70)
    print("EXAMPLE 2: Batch Processing")
    print("=" * 70)
    print()

    description = """
    Extract product information:
    - product_name: Name of the product
    - price: Price in USD (as a number)
    - rating: Rating from 1-5 (as a number)
    """

    extractor = SchemaExtractor(description)

    # Process multiple documents at once
    documents = [
        "The SuperWidget costs $29.99 and has a rating of 4.5 stars",
        "MegaTool is priced at $149 with 5-star reviews",
        "Budget Gadget - only $9.99, rated 3 out of 5",
    ]

    results = extractor.extract(documents)

    print("Extracted from 3 product reviews:\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['product_name']}: ${result['price']} (Rating: {result['rating']})")
    print()


def example_3_schema_inspection():
    """Example 3: Inspect the generated schema without running extraction."""
    print("=" * 70)
    print("EXAMPLE 3: Schema Inspection")
    print("=" * 70)
    print()

    description = """
    Extract invoice information:
    - invoice_number: The invoice number (string)
    - vendor_name: Name of the vendor
    - total_amount: Total amount in EUR (as a number)
    - line_items: List of items purchased (list of strings)
    """

    extractor = SchemaExtractor(description)

    # Get the generated Pydantic model
    pydantic_model = extractor.model
    print(f"Generated Pydantic model name: {pydantic_model.__name__}")
    print(f"\nModel fields:")
    for field_name, field_info in pydantic_model.model_fields.items():
        print(f"  - {field_name}: {field_info.annotation}")

    # Get JSON Schema (standard format, works with any tool)
    json_schema = pydantic_model.model_json_schema()
    print(f"\nJSON Schema:")
    print(json.dumps(json_schema, indent=2))
    print()


def example_4_different_providers():
    """Example 4: Using different LLM providers."""
    print("=" * 70)
    print("EXAMPLE 4: Multiple Providers")
    print("=" * 70)
    print()

    description = """
    Extract:
    - company: Company name
    - revenue: Annual revenue in millions (as a number)
    """

    text = "Acme Corporation reported annual revenue of 250 million dollars."

    # Check which providers are available
    has_openai = bool(os.getenv("OPENAI_API_KEY"))
    has_anthropic = bool(os.getenv("ANTHROPIC_API_KEY"))
    has_google = bool(os.getenv("GOOGLE_API_KEY"))
    has_azure = bool(os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("AZURE_API_KEY"))

    print(f"Input text: {text}\n")

    # Test with OpenAI (default)
    if has_openai:
        print("Using OpenAI (default):")
        extractor_openai = SchemaExtractor(description)
        result = extractor_openai.extract_one(text)
        print(f"  Result: {result}")
        print()

    # Test with Anthropic Claude
    if has_anthropic:
        print("Using Anthropic Claude:")
        extractor_anthropic = SchemaExtractor(
            description,
            provider="anthropic"
        )
        result = extractor_anthropic.extract_one(text)
        print(f"  Result: {result}")
        print()

    # Test with Google Gemini
    if has_google:
        print("Using Google Gemini:")
        extractor_google = SchemaExtractor(
            description,
            provider="google"
        )
        result = extractor_google.extract_one(text)
        print(f"  Result: {result}")
        print()

    # Test with Azure OpenAI
    if has_azure:
        print("Using Azure OpenAI:")
        azure_config = {}

        # Support both AZURE_OPENAI_* and AZURE_* env variable patterns
        if os.getenv("AZURE_API_KEY"):
            azure_config["api_key"] = os.getenv("AZURE_API_KEY")
        if os.getenv("AZURE_API_BASE"):
            azure_config["azure_endpoint"] = os.getenv("AZURE_API_BASE")

        # Azure requires a deployment name - use a sensible default
        azure_config["azure_deployment"] = "gpt-4"

        try:
            extractor_azure = SchemaExtractor(
                description,
                provider="azure",
                **azure_config
            )
            result = extractor_azure.extract_one(text)
            print(f"  Result: {result}")
            print()
        except Exception as e:
            print(f"  Note: Azure setup requires deployment name: {e}")
            print()


def example_5_complex_schema():
    """Example 5: Complex schema with nested structures and lists."""
    print("=" * 70)
    print("EXAMPLE 5: Complex Schema")
    print("=" * 70)
    print()

    description = """
    Extract meeting information:
    - meeting_title: Title of the meeting
    - date: Meeting date (ISO format)
    - participants: List of participant names
    - action_items: List of action items discussed
    - priority: Priority level (high, medium, low)
    """

    text = """
    Team Sync Meeting held on 2024-01-15. Attendees: Alice Johnson, Bob Smith, Carol White.
    Discussed: 1) Complete Q1 budget review (high priority), 2) Update project timeline,
    3) Schedule client presentation. Important tasks identified for next week.
    """

    extractor = SchemaExtractor(description)
    result = extractor.extract_one(text)

    print(f"Input text: {text}\n")
    print("Extracted meeting information:")
    print(f"  Title: {result.get('meeting_title')}")
    print(f"  Date: {result.get('date')}")
    print(f"  Participants: {result.get('participants')}")
    print(f"  Action Items: {result.get('action_items')}")
    print(f"  Priority: {result.get('priority')}")
    print()


def main():
    """Run all examples."""
    print("\n")
    print("=" * 70)
    print("         GAIK TOOLKIT - GETTING STARTED")
    print("=" * 70)
    print()

    # Check if at least one API key is set
    has_any_key = any([
        os.getenv("OPENAI_API_KEY"),
        os.getenv("ANTHROPIC_API_KEY"),
        os.getenv("GOOGLE_API_KEY"),
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_API_KEY"),
    ])

    if not has_any_key:
        print("ERROR: No API keys found!")
        print("Please set at least one API key in your .env file:")
        print("  OPENAI_API_KEY=sk-...")
        print("  ANTHROPIC_API_KEY=sk-ant-...")
        print("  GOOGLE_API_KEY=...")
        print("  AZURE_API_KEY=... (and AZURE_API_BASE=...)")
        print()
        return

    print("Available providers:")
    if os.getenv("OPENAI_API_KEY"):
        print("  [OK] OpenAI")
    if os.getenv("ANTHROPIC_API_KEY"):
        print("  [OK] Anthropic Claude")
    if os.getenv("GOOGLE_API_KEY"):
        print("  [OK] Google Gemini")
    if os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("AZURE_API_KEY"):
        print("  [OK] Azure OpenAI")
    print("\n")

    try:
        # Run examples
        example_1_basic_extraction()
        example_2_multiple_documents()
        example_3_schema_inspection()
        example_4_different_providers()
        example_5_complex_schema()

        print("=" * 70)
        print("All examples completed successfully!")
        print("=" * 70)
        print()
        print("Next steps:")
        print("  - Check examples/02_pydantic_schemas.py for advanced schema usage")
        print("  - Check examples/03_real_world_use_cases.py for practical examples")
        print("  - Read docs for more information")
        print()

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

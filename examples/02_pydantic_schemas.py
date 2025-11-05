"""GAIK Toolkit - Working with Pydantic Schemas

This example demonstrates advanced schema functionality:
1. How GAIK generates Pydantic models from natural language
2. Accessing and inspecting the generated schema
3. Exporting schemas to JSON Schema format
4. Using schemas with other tools and frameworks
5. Working with complex data types (lists, nested objects, enums)

Requirements:
- Set at least one API key in .env file
- Run: python examples/02_pydantic_schemas.py
"""

import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# Load environment variables from .env file in project root
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")

from gaik.extract import SchemaExtractor


def example_1_inspect_pydantic_model():
    """Example 1: Inspect the generated Pydantic model."""
    print("=" * 70)
    print("EXAMPLE 1: Inspecting Generated Pydantic Models")
    print("=" * 70)
    print()

    description = """
    Extract customer information:
    - customer_id: Unique customer identifier (string)
    - full_name: Customer's full name
    - email: Email address
    - phone: Phone number (optional)
    - is_active: Whether the account is active (boolean)
    """

    extractor = SchemaExtractor(description)

    # Access the generated Pydantic model
    model = extractor.model

    print(f"Model class name: {model.__name__}")
    print(f"Model base classes: {[base.__name__ for base in model.__bases__]}")
    print()

    # Inspect fields
    print("Model fields:")
    for field_name, field_info in model.model_fields.items():
        required = field_info.is_required()
        field_type = field_info.annotation
        description = field_info.description or "No description"
        print(f"  • {field_name}:")
        print(f"      Type: {field_type}")
        print(f"      Required: {required}")
        print(f"      Description: {description}")
    print()


def example_2_json_schema_export():
    """Example 2: Export schema to JSON Schema format."""
    print("=" * 70)
    print("EXAMPLE 2: JSON Schema Export")
    print("=" * 70)
    print()

    description = """
    Extract product information:
    - sku: Product SKU code
    - name: Product name
    - price: Price in USD (number)
    - in_stock: Availability status (boolean)
    - categories: Product categories (list of strings)
    """

    extractor = SchemaExtractor(description)

    # Get JSON Schema - standard format that works with any tool
    json_schema = extractor.model.model_json_schema()

    print("Generated JSON Schema:")
    print(json.dumps(json_schema, indent=2))
    print()

    # This JSON Schema can be used with:
    # - API documentation tools (Swagger/OpenAPI)
    # - Form generators
    # - Validation libraries in other languages
    # - Database schema generators
    print("This JSON Schema can be used with:")
    print("  • OpenAPI/Swagger documentation")
    print("  • Form generation libraries")
    print("  • Cross-language validation")
    print("  • Database schema generation")
    print()


def example_3_using_pydantic_features():
    """Example 3: Using Pydantic model features directly."""
    print("=" * 70)
    print("EXAMPLE 3: Using Pydantic Features")
    print("=" * 70)
    print()

    description = """
    Extract invoice data:
    - invoice_id: Invoice number
    - amount: Total amount (number)
    - currency: Currency code (e.g., EUR, USD)
    - issued_date: Date when issued (ISO format)
    """

    extractor = SchemaExtractor(description)

    text = "Invoice #INV-2024-001 for 1500 EUR issued on 2024-01-15"
    result = extractor.extract_one(text)

    print(f"Input: {text}\n")

    # The result is a dict, but we can validate it with the Pydantic model
    model = extractor.model
    validated_instance = model(**result)

    print("Validated instance:")
    print(f"  {validated_instance}")
    print()

    # Convert to different formats
    print("As JSON:")
    print(f"  {validated_instance.model_dump_json(indent=2)}")
    print()

    print("As dict:")
    print(f"  {validated_instance.model_dump()}")
    print()


def example_4_complex_nested_schema():
    """Example 4: Working with complex nested structures."""
    print("=" * 70)
    print("EXAMPLE 4: Complex Nested Schemas")
    print("=" * 70)
    print()

    description = """
    Extract order information:
    - order_id: Unique order identifier
    - customer_name: Name of the customer
    - items: List of items ordered (each item should include name and quantity)
    - total: Total order value (number)
    - status: Order status (e.g., pending, shipped, delivered)
    - shipping_address: Full shipping address
    - notes: Additional notes or comments (optional)
    """

    extractor = SchemaExtractor(description)

    text = """
    Order #ORD-12345 for Sarah Johnson. Items: 2x Laptop Stand, 1x Wireless Mouse.
    Total: $89.98. Status: Shipped. Deliver to: 123 Main St, Helsinki, Finland.
    Note: Please leave at reception.
    """

    result = extractor.extract_one(text)

    print(f"Input: {text}\n")
    print("Extracted order:")
    print(json.dumps(result, indent=2))
    print()

    # Show the schema
    schema = extractor.model.model_json_schema()
    print("Generated schema properties:")
    for prop_name, prop_def in schema.get("properties", {}).items():
        prop_type = prop_def.get("type", "unknown")
        print(f"  • {prop_name}: {prop_type}")
    print()


def example_5_field_names_and_types():
    """Example 5: Accessing field names and checking types."""
    print("=" * 70)
    print("EXAMPLE 5: Field Introspection")
    print("=" * 70)
    print()

    description = """
    Extract article metadata:
    - title: Article title
    - author: Author name
    - publication_date: Publication date
    - word_count: Number of words (integer)
    - tags: Article tags (list of strings)
    - is_published: Whether published (boolean)
    - views: Number of views (integer)
    """

    extractor = SchemaExtractor(description)

    print("Available field names:")
    for field in extractor.field_names:
        print(f"  • {field}")
    print()

    print("Field specifications:")
    for field in extractor.fields:
        print(f"  • {field.field_name}:")
        print(f"      Type: {field.field_type}")
        print(f"      Required: {field.required}")
        print(f"      Description: {field.description}")
    print()


def example_6_schema_validation():
    """Example 6: Schema validation and error handling."""
    print("=" * 70)
    print("EXAMPLE 6: Schema Validation")
    print("=" * 70)
    print()

    description = """
    Extract numeric data:
    - temperature: Temperature in Celsius (number)
    - humidity: Humidity percentage (number)
    - pressure: Atmospheric pressure (number)
    """

    extractor = SchemaExtractor(description)
    model = extractor.model

    print("Testing schema validation with Pydantic:\n")

    # Valid data
    try:
        valid_data = {
            "temperature": 22.5,
            "humidity": 65.0,
            "pressure": 1013.25
        }
        instance = model(**valid_data)
        print(f"[OK] Valid data accepted: {instance.model_dump()}")
    except Exception as e:
        print(f"[ERROR] Validation error: {e}")

    print()

    # Invalid data (missing required field)
    try:
        invalid_data = {
            "temperature": 22.5,
            "humidity": 65.0
            # pressure is missing
        }
        instance = model(**invalid_data)
        print(f"[OK] Data accepted: {instance.model_dump()}")
    except Exception as e:
        print(f"[EXPECTED] Validation error for missing field: {type(e).__name__}")

    print()


def example_7_reusing_schemas():
    """Example 7: Reusing schemas across different contexts."""
    print("=" * 70)
    print("EXAMPLE 7: Reusing Schemas")
    print("=" * 70)
    print()

    description = """
    Extract contact information:
    - name: Person's name
    - email: Email address
    - company: Company name
    """

    # Create extractor once
    extractor = SchemaExtractor(description)

    # Use it multiple times with different texts
    texts = [
        "John Smith from Acme Corp, email: john@acme.com",
        "Contact: Jane Doe, TechCo, jane.doe@techco.com",
        "Mike Johnson (mike.j@startup.io) - StartupXYZ"
    ]

    print("Processing multiple contacts with same schema:\n")
    results = extractor.extract(texts)

    for i, result in enumerate(results, 1):
        print(f"{i}. {result['name']} - {result['company']} ({result['email']})")

    print()

    # You can also save and reuse the schema
    schema_json = extractor.model.model_json_schema()
    print("Schema can be saved and reused:")
    print(f"  • Save to file: json.dump(schema_json, file)")
    print(f"  • Share across services")
    print(f"  • Version control the schema")
    print(f"  • Generate code in other languages")
    print()


def main():
    """Run all examples."""
    print("\n")
    print("=" * 70)
    print("         GAIK TOOLKIT - PYDANTIC SCHEMAS")
    print("=" * 70)
    print()

    # Check for API key
    if not any([
        os.getenv("OPENAI_API_KEY"),
        os.getenv("ANTHROPIC_API_KEY"),
        os.getenv("GOOGLE_API_KEY"),
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_API_KEY"),
    ]):
        print("ERROR: No API keys found!")
        print("Please set at least one API key in your .env file")
        return

    try:
        example_1_inspect_pydantic_model()
        example_2_json_schema_export()
        example_3_using_pydantic_features()
        example_4_complex_nested_schema()
        example_5_field_names_and_types()
        example_6_schema_validation()
        example_7_reusing_schemas()

        print("=" * 70)
        print("All examples completed!")
        print("=" * 70)
        print()
        print("Key takeaways:")
        print("  • GAIK generates fully-featured Pydantic models")
        print("  • Schemas can be exported to JSON Schema format")
        print("  • Full Pydantic validation and serialization support")
        print("  • Schemas are reusable across different contexts")
        print()

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

"""GAIK Toolkit - Real-World Use Cases

This example demonstrates practical, real-world applications:
1. Invoice processing
2. Customer feedback analysis
3. Resume/CV parsing
4. Product catalog extraction
5. News article metadata extraction
6. Email parsing and classification

Each example shows how GAIK can solve actual business problems.

Requirements:
- Set at least one API key in .env file
- Run: python examples/03_real_world_use_cases.py
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file in project root
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")

from gaik.extract import SchemaExtractor, dynamic_extraction_workflow


def use_case_1_invoice_processing():
    """Use Case 1: Automated Invoice Processing."""
    print("=" * 70)
    print("USE CASE 1: Invoice Processing")
    print("=" * 70)
    print()
    print("Business need: Extract structured data from invoice PDFs/emails")
    print("Application: Automated accounting, expense management")
    print()

    description = """
    Extract from invoice:
    - invoice_number: The invoice or reference number
    - vendor_name: Name of the vendor/supplier
    - invoice_date: Date of invoice (ISO format)
    - due_date: Payment due date (ISO format)
    - subtotal: Subtotal amount before tax (number)
    - tax_amount: Tax amount (number)
    - total_amount: Total amount including tax (number)
    - currency: Currency code (EUR, USD, etc.)
    - line_items: List of items/services (list of strings)
    """

    invoices = [
        """
        INVOICE #INV-2024-0156
        From: Acme Office Supplies Ltd.
        Date: January 15, 2024
        Due: February 15, 2024

        Items:
        - 5x Printer Paper Reams
        - 2x Stapler Heavy Duty
        - 10x Blue Pens

        Subtotal: 145.00 EUR
        VAT (24%): 34.80 EUR
        Total: 179.80 EUR
        """,
        """
        Invoice Number: TEC-2024-789
        Tech Solutions Inc.
        Issued: 2024-01-20
        Payment Due: 2024-02-20

        Services:
        - Cloud hosting (monthly)
        - Technical support (5 hours)

        Net Amount: $450.00
        Tax: $45.00
        Grand Total: $495.00 USD
        """
    ]

    extractor = SchemaExtractor(description)
    results = extractor.extract(invoices)

    print("Processed invoices:\n")
    for i, result in enumerate(results, 1):
        print(f"Invoice {i}:")
        print(f"  Number: {result.get('invoice_number')}")
        print(f"  Vendor: {result.get('vendor_name')}")
        print(f"  Total: {result.get('total_amount')} {result.get('currency')}")
        print(f"  Due: {result.get('due_date')}")
        print(f"  Items: {len(result.get('line_items', []))} items")
        print()


def use_case_2_customer_feedback():
    """Use Case 2: Customer Feedback Analysis."""
    print("=" * 70)
    print("USE CASE 2: Customer Feedback Analysis")
    print("=" * 70)
    print()
    print("Business need: Analyze customer feedback and reviews")
    print("Application: Product improvement, customer satisfaction tracking")
    print()

    description = """
    Extract from customer feedback:
    - customer_name: Name of the customer (if mentioned)
    - product_name: Product or service mentioned
    - sentiment: Overall sentiment (positive, negative, neutral)
    - rating: Rating if provided (1-5 scale, as number)
    - issues: List of problems or complaints mentioned
    - suggestions: List of improvement suggestions
    - would_recommend: Whether they would recommend (boolean)
    """

    feedback = [
        """
        Review by Sarah M.
        Product: SmartWatch Pro

        I've been using this smartwatch for 3 months and it's fantastic! Battery life is
        excellent, easily lasts 5 days. The fitness tracking is accurate. Only minor issue
        is the app could be more intuitive. Would definitely recommend to friends!
        Rating: 4.5/5
        """,
        """
        Customer: John D.
        Regarding: Premium Headphones

        Disappointed with these headphones. Sound quality is mediocre at best, and they're
        uncomfortable for long use. For the price, expected much better. Connection drops
        frequently. Would not buy again or recommend. The only positive is the design looks nice.
        2 stars.
        """
    ]

    extractor = SchemaExtractor(description)
    results = extractor.extract(feedback)

    print("Analyzed feedback:\n")
    for i, result in enumerate(results, 1):
        print(f"Feedback {i}:")
        print(f"  Product: {result.get('product_name')}")
        print(f"  Sentiment: {result.get('sentiment')}")
        print(f"  Rating: {result.get('rating')}/5")
        print(f"  Recommend: {'Yes' if result.get('would_recommend') else 'No'}")
        if result.get('issues'):
            print(f"  Issues: {', '.join(result.get('issues', []))}")
        print()


def use_case_3_resume_parsing():
    """Use Case 3: Resume/CV Parsing."""
    print("=" * 70)
    print("USE CASE 3: Resume/CV Parsing")
    print("=" * 70)
    print()
    print("Business need: Extract structured data from resumes")
    print("Application: Recruitment, applicant tracking systems")
    print()

    description = """
    Extract from resume:
    - full_name: Candidate's full name
    - email: Email address
    - phone: Phone number
    - current_title: Current or most recent job title
    - years_of_experience: Total years of professional experience (number)
    - skills: List of technical and professional skills
    - education: Highest education level
    - languages: Languages spoken (list)
    - location: City and country
    """

    resume = """
    CURRICULUM VITAE

    Maria Rodriguez
    Senior Software Engineer
    Email: maria.rodriguez@email.com | Phone: +358 40 123 4567
    Location: Helsinki, Finland

    PROFESSIONAL SUMMARY
    Experienced software engineer with 8 years in full-stack development.
    Specialized in cloud-native applications and microservices architecture.

    TECHNICAL SKILLS
    - Languages: Python, JavaScript, TypeScript, Go
    - Frameworks: React, Node.js, Django, FastAPI
    - Cloud: AWS, Azure, Docker, Kubernetes
    - Databases: PostgreSQL, MongoDB, Redis

    EDUCATION
    M.Sc. Computer Science, University of Helsinki (2015)

    LANGUAGES
    Finnish (native), English (fluent), Spanish (professional)
    """

    extractor = SchemaExtractor(description)
    result = extractor.extract_one(resume)

    print("Parsed resume:\n")
    print(f"Name: {result.get('full_name')}")
    print(f"Title: {result.get('current_title')}")
    print(f"Experience: {result.get('years_of_experience')} years")
    print(f"Email: {result.get('email')}")
    print(f"Location: {result.get('location')}")
    print(f"Skills: {', '.join(result.get('skills', [])[:5])}...")
    print(f"Languages: {', '.join(result.get('languages', []))}")
    print()


def use_case_4_product_catalog():
    """Use Case 4: Product Catalog Extraction from Descriptions."""
    print("=" * 70)
    print("USE CASE 4: Product Catalog Extraction")
    print("=" * 70)
    print()
    print("Business need: Structure product information from text descriptions")
    print("Application: E-commerce, inventory management")
    print()

    description = """
    Extract product information:
    - product_name: Full product name
    - brand: Brand or manufacturer
    - model_number: Model or SKU number
    - price: Price (number)
    - currency: Currency code
    - features: List of key features
    - dimensions: Physical dimensions if mentioned
    - weight: Weight if mentioned
    - in_stock: Stock availability (boolean)
    - warranty: Warranty period if mentioned
    """

    products = [
        """
        Dell XPS 15 Laptop (Model: XPS15-9520)
        Price: 1,899 EUR

        Premium ultrabook featuring Intel i7-12700H processor, 16GB RAM, 512GB SSD.
        15.6" 4K OLED display with 100% DCI-P3 color gamut. NVIDIA RTX 3050 Ti graphics.
        Dimensions: 344.72 x 230.14 x 18mm, Weight: 2.0kg

        Key Features:
        - Thunderbolt 4 ports
        - Wi-Fi 6E connectivity
        - Windows 11 Pro
        - Premium metal chassis
        - Up to 13 hours battery life

        In stock. 2-year warranty included.
        """,
        """
        Samsung Galaxy S24 Ultra - Titanium Gray (SM-S928)
        $1,299.99 USD

        Flagship smartphone with 6.8" Dynamic AMOLED display, Snapdragon 8 Gen 3,
        12GB RAM, 256GB storage. Quad camera system with 200MP main sensor.
        Built-in S Pen. IP68 water resistance.

        162.3 x 79 x 8.6 mm, 232g
        Available now - 1 year manufacturer warranty
        """
    ]

    extractor = SchemaExtractor(description)
    results = extractor.extract(products)

    print("Extracted product catalog:\n")
    for i, result in enumerate(results, 1):
        print(f"Product {i}: {result.get('product_name')}")
        print(f"  Brand: {result.get('brand')}")
        print(f"  Price: {result.get('price')} {result.get('currency')}")
        print(f"  Model: {result.get('model_number')}")
        print(f"  In Stock: {'Yes' if result.get('in_stock') else 'No'}")
        print(f"  Warranty: {result.get('warranty')}")
        print()


def use_case_5_news_metadata():
    """Use Case 5: News Article Metadata Extraction."""
    print("=" * 70)
    print("USE CASE 5: News Article Metadata")
    print("=" * 70)
    print()
    print("Business need: Extract metadata from news articles")
    print("Application: News aggregation, content management systems")
    print()

    description = """
    Extract article metadata:
    - headline: Article headline
    - author: Author name
    - publication_date: Publication date (ISO format)
    - category: Article category (politics, technology, business, etc.)
    - tags: Relevant tags or keywords (list)
    - location: Geographic location mentioned
    - organizations: Organizations mentioned (list)
    - summary: Brief one-sentence summary
    """

    article = """
    Tech Giant Announces Major AI Investment in Nordic Region

    By Emma Virtanen | January 25, 2024 | Technology

    HELSINKI - Microsoft announced today a €1 billion investment in artificial intelligence
    infrastructure across Finland and Sweden. The initiative will establish three new data
    centers and create over 500 jobs in the region.

    The project, dubbed "Nordic AI Hub," will focus on sustainable AI computing using
    renewable energy. Finnish Minister of Economic Affairs welcomed the announcement,
    highlighting the country's expertise in clean energy and technology innovation.

    Microsoft CEO emphasized the strategic importance of the Nordic region for AI development,
    citing skilled workforce and commitment to sustainability.

    Tags: artificial intelligence, Microsoft, Nordic countries, data centers, investment
    """

    extractor = SchemaExtractor(description)
    result = extractor.extract_one(article)

    print("Extracted metadata:\n")
    print(f"Headline: {result.get('headline')}")
    print(f"Author: {result.get('author')}")
    print(f"Date: {result.get('publication_date')}")
    print(f"Category: {result.get('category')}")
    print(f"Location: {result.get('location')}")
    print(f"Organizations: {', '.join(result.get('organizations', []))}")
    print(f"Tags: {', '.join(result.get('tags', []))}")
    print()


def use_case_6_email_parsing():
    """Use Case 6: Email Parsing and Classification."""
    print("=" * 70)
    print("USE CASE 6: Email Parsing and Classification")
    print("=" * 70)
    print()
    print("Business need: Parse and classify incoming emails")
    print("Application: Email automation, customer support routing")
    print()

    description = """
    Extract from email:
    - sender_name: Name of the sender
    - sender_email: Email address of sender
    - subject: Email subject line
    - urgency: Urgency level (high, medium, low)
    - category: Email category (support, sales, inquiry, complaint, etc.)
    - action_required: Whether action is required (boolean)
    - deadline: Any mentioned deadline or due date
    - key_points: List of main points or requests
    """

    emails = [
        """
        From: John Smith <john.smith@customer.com>
        Subject: URGENT: System Down - Production Issue

        Hi Support Team,

        Our production system has been down since 9:00 AM. This is affecting all our operations
        and costing us significant revenue. We need immediate assistance.

        Issue: Database connection timeout errors
        Affected systems: All web services
        Started: 2024-01-25 09:00 UTC

        Please respond ASAP. This is critical.

        John Smith
        IT Manager, Customer Corp
        """,
        """
        From: Sarah Johnson <sarah.j@prospect.com>
        Subject: Inquiry about Enterprise Plan

        Hello,

        I came across your product and I'm interested in learning more about the Enterprise
        plan for our company (200+ employees).

        Could you please provide:
        - Pricing information
        - Feature comparison with Professional plan
        - Implementation timeline
        - Training options

        We're looking to make a decision by end of Q1.

        Best regards,
        Sarah Johnson
        Procurement Manager
        """
    ]

    extractor = SchemaExtractor(description)
    results = extractor.extract(emails)

    print("Classified emails:\n")
    for i, result in enumerate(results, 1):
        print(f"Email {i}:")
        print(f"  From: {result.get('sender_name')} ({result.get('sender_email')})")
        print(f"  Subject: {result.get('subject')}")
        print(f"  Category: {result.get('category')}")
        print(f"  Urgency: {result.get('urgency')}")
        print(f"  Action Required: {'Yes' if result.get('action_required') else 'No'}")
        if result.get('deadline'):
            print(f"  Deadline: {result.get('deadline')}")
        print(f"  Key Points: {len(result.get('key_points', []))} items")
        print()


def main():
    """Run all use case examples."""
    print("\n")
    print("=" * 70)
    print("         GAIK TOOLKIT - REAL-WORLD USE CASES")
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

    print("These examples demonstrate real business applications of GAIK.\n")

    try:
        use_case_1_invoice_processing()
        use_case_2_customer_feedback()
        use_case_3_resume_parsing()
        use_case_4_product_catalog()
        use_case_5_news_metadata()
        use_case_6_email_parsing()

        print("=" * 70)
        print("All use cases completed!")
        print("=" * 70)
        print()
        print("These examples show how GAIK can:")
        print("  + Automate document processing")
        print("  + Extract insights from unstructured text")
        print("  + Structure data for business applications")
        print("  + Scale across different domains and use cases")
        print()
        print("Next steps:")
        print("  - Adapt these examples to your specific needs")
        print("  - Combine with your existing workflows")
        print("  - Integrate with databases and APIs")
        print()

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

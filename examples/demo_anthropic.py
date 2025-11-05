from dotenv import load_dotenv

load_dotenv()

from gaik.extract import SchemaExtractor

# IDE shows available providers: "openai" | "anthropic" | "google" | "azure"
extractor = SchemaExtractor(
    "Extract name and age from text",
    provider="anthropic",  # ← Try typing here, IDE suggests options!
)

result = extractor.extract_one("Alice is 25 years old")
print(result)

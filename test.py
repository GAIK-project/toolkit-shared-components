import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Debug: Check if environment variables are loaded
print(f"AZURE_API_KEY: {'Set' if os.getenv('AZURE_API_KEY') else 'Not set'}")
print(f"AZURE_ENDPOINT: {os.getenv('AZURE_ENDPOINT')}")
print(f"AZURE_DEPLOYMENT: {os.getenv('AZURE_DEPLOYMENT')}")
print(f"AZURE_API_VERSION: {os.getenv('AZURE_API_VERSION')}\n")

# Azure OpenAI with OpenAI client requires specific base_url format
azure_endpoint = os.getenv("AZURE_ENDPOINT", "").rstrip("/")
deployment = os.getenv("AZURE_DEPLOYMENT")
api_version = os.getenv("AZURE_API_VERSION", "2025-04-01-preview")

# For Azure OpenAI, base_url should point to deployment
base_url = f"{azure_endpoint}/openai/deployments/{deployment}"

print(f"Base URL: {base_url}\n")

client = OpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    base_url=base_url,
    default_query={"api-version": api_version},
)

response = client.chat.completions.create(
    model=deployment,  # Azure deployment name
    messages=[
        {
            "role": "user",
            "content": "What steps should I think about when writing my first Python API?",
        },
    ],
    max_completion_tokens=5000,
    reasoning_effort="low",  # Only works with o1/o3/gpt-5 models
)

print(response.model_dump_json(indent=2))

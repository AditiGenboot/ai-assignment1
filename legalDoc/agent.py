import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key is loaded properly
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Configure Gemini AI with API key
genai.configure(api_key=api_key)

def extract_legal_details(text):
    """Extract structured details from legal agreements using Gemini AI."""
    prompt = f"""
    Extract the following details from the given legal agreement text and format them in JSON:
    - Name of the parties
    - Payment amount
    - Payment method
    - Payment date
    - A short two-line description of the agreement.

    Agreement Text:
    {text}
    """

    # Use an available model
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    try:
        response = model.generate_content(prompt)
        return response.text  # Returns the extracted JSON
    except Exception as e:
        print("Error generating content:", e)
        return None

# Load legal agreement text from file
try:
    with open("legalDocument", "r", encoding="utf-8") as file:
        legal_text = file.read()
except FileNotFoundError:
    print("Error: The file 'legalDocument' was not found.")
    exit(1)

# Extract structured data
structured_data = extract_legal_details(legal_text)

# Print the extracted data
if structured_data:
    print("Extracted Data:", structured_data)
else:
    print("Failed to extract legal details.")

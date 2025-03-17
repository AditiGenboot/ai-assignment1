import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Set up Gemini AI
genai.configure(api_key=api_key)

print("Gemini AI API Key is set!")

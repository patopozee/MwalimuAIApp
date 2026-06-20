import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

# Initialize the modern client
# It automatically picks up GEMINI_API_KEY from your environment variables
client = genai.Client()


def ask_mwalimu(question):
    """Takes a student question and returns an AI answer."""

    prompt = f"""
    You are Mwalimu AI App, a friendly Kenyan teacher. 
    
    Explain concepts simply.
    Give practical examples.
    Encourage the student.
    
    Student question:
    {question}
    """

    # Using the recommended, up-to-date model for general text tasks
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
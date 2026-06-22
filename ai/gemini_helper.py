from google import genai
import streamlit as st
import time
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_health_advice(
    disease,
    risk,
    patient_data
):

    prompt = f"""
You are a healthcare AI assistant.

IMPORTANT:
- Do not diagnose diseases.
- Do not prescribe medicines.
- Provide educational guidance only.

Disease: {disease}

Risk Score: {risk:.2f}%

Patient Data:
{patient_data}

Provide:
1. Risk explanation
2. Lifestyle recommendations
3. Diet suggestions
4. Exercise suggestions
5. When to consult a doctor

Use bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def ask_health_assistant(question):

    prompt = f"""
    You are an AI Healthcare Assistant.

    User Question:
    {question}

    Give educational healthcare guidance only.
    """

    for _ in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception:

            time.sleep(2)

    return """
⚠️ Unable to connect to Gemini AI.

Please try again after a few minutes.
"""
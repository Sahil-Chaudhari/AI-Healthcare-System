from google import genai
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
You are HealthAI Assistant.

Rules:
- Educational information only
- Do not diagnose diseases
- Do not prescribe medications
- Recommend doctor consultation when appropriate

Question:
{question}

Provide a clear answer.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
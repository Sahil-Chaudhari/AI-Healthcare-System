from ai.gemini_helper import (
    get_health_advice
)

response = get_health_advice(
    "Diabetes",
    75,
    """
Age: 55
BMI: 31
Glucose: 180
"""
)

print(response)
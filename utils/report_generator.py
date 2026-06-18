from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_diabetes_report(
    patient_name,
    gender,
    age,
    bmi,
    risk,
    risk_level,
    glucose,
    blood_pressure,
    insulin,
    dpf
):

    filename = "diabetes_report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==========================
    # TITLE
    # ==========================

    elements.append(
        Paragraph(
            "HealthAI Diabetes Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # PATIENT DETAILS
    # ==========================

    elements.append(
        Paragraph(
            f"<b>Patient Name:</b> {patient_name}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Gender:</b> {gender}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Age:</b> {age}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>BMI:</b> {bmi:.2f}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # PREDICTION
    # ==========================

    elements.append(
        Paragraph(
            f"<b>Risk Score:</b> {risk:.2f}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Risk Category:</b> {risk_level}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    if risk_level == "Low":

        recommendations = [
            "Maintain healthy diet",
            "Exercise regularly",
            "Annual health checkup"
        ]

    elif risk_level == "Moderate":

        recommendations = [
            "Reduce sugar intake",
            "Monitor glucose regularly",
            "Increase physical activity"
        ]

    else:

        recommendations = [
            "Consult a physician",
            "Monitor blood sugar frequently",
            "Follow diabetic diet plan",
            "Exercise daily"
        ]

    for item in recommendations:

        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    # ==========================
    # RISK FACTOR ANALYSIS
    # ==========================

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Risk Factor Evaluation",
            styles["Heading2"]
        )
    )

    risk_factors = []

    if glucose > 140:
        risk_factors.append(
            f"High Glucose Level ({glucose})"
        )

    if bmi > 25:
        risk_factors.append(
            f"Elevated BMI ({bmi:.2f})"
        )

    if age > 45:
        risk_factors.append(
            f"Age Factor ({age})"
        )

    if blood_pressure > 90:
        risk_factors.append(
            f"High Blood Pressure ({blood_pressure})"
        )

    if insulin > 150:
        risk_factors.append(
            f"Elevated Insulin Level ({insulin})"
        )

    if dpf > 0.5:
        risk_factors.append(
            f"Family History Risk (DPF: {dpf})"
        )

    if len(risk_factors) == 0:

        elements.append(
            Paragraph(
                "No major risk factors detected.",
                styles["Normal"]
            )
        )

    else:

        for factor in risk_factors:

            elements.append(
                Paragraph(
                    f"• {factor}",
                    styles["Normal"]
                )
            )

    doc.build(elements)

    return filename
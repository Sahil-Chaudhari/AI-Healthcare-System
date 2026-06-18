from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_heart_report(
    patient_name,
    gender,
    age,
    risk,
    risk_level,
    chol,
    trestbps,
    thalach
):

    filename = "heart_disease_report.pdf"

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
            "HealthAI Heart Disease Report",
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
        Spacer(1, 20)
    )

    # ==========================
    # RISK SUMMARY
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
    # RISK FACTOR ANALYSIS
    # ==========================

    elements.append(
        Paragraph(
            "Risk Factor Evaluation",
            styles["Heading2"]
        )
    )

    risk_factors = []

    if chol > 240:
        risk_factors.append(
            f"High Cholesterol ({chol})"
        )

    if trestbps > 140:
        risk_factors.append(
            f"High Blood Pressure ({trestbps})"
        )

    if thalach < 120:
        risk_factors.append(
            f"Low Maximum Heart Rate ({thalach})"
        )

    if age > 50:
        risk_factors.append(
            f"Age Risk Factor ({age})"
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
            "Maintain healthy lifestyle",
            "Exercise regularly",
            "Annual heart screening"
        ]

    elif risk_level == "Moderate":

        recommendations = [
            "Reduce cholesterol intake",
            "Monitor blood pressure",
            "Increase physical activity",
            "Avoid smoking"
        ]

    else:

        recommendations = [
            "Consult a cardiologist",
            "Follow heart healthy diet",
            "Monitor blood pressure regularly",
            "Reduce salt intake",
            "Regular ECG checkups"
        ]

    for item in recommendations:

        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    doc.build(elements)

    return filename
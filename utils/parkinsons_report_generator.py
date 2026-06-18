from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_parkinsons_report(
    patient_name,
    gender,
    age,
    risk,
    risk_level
):

    filename = "parkinsons_report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "HealthAI Parkinson's Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now()}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

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

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    recommendations = []

    if risk_level == "Low":

        recommendations = [
            "Maintain healthy lifestyle",
            "Regular neurological checkups"
        ]

    elif risk_level == "Moderate":

        recommendations = [
            "Monitor symptoms regularly",
            "Consult neurologist if needed"
        ]

    else:

        recommendations = [
            "Consult neurologist immediately",
            "Schedule advanced diagnostic tests",
            "Regular monitoring recommended"
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
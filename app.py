import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from ai.gemini_helper import (
    get_health_advice,
    ask_health_assistant
)
from utils.report_generator import (
    generate_diabetes_report
)
from utils.heart_report_generator import (
    generate_heart_report
)
import streamlit as st
from utils.predictor import predict_diabetes
from utils.heart_predictor import predict_heart
from utils.parkinsons_predictor import (
    predict_parkinsons
)

from utils.parkinsons_report_generator import (
    generate_parkinsons_report
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="HealthAI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

.metric-card {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.markdown("# 🏥 HealthAI")

    st.markdown("""
    ### AI Healthcare Platform

    Predict diseases using
    Machine Learning & AI
    """)

    st.divider()

    selected = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🩺 Diabetes Prediction",
            "❤️ Heart Disease Prediction",
            "🧠 Parkinson's Prediction",
            "🤖 AI Health Assistant"
        ]
    )

    st.divider()


# ---------------- DASHBOARD ---------------- #

if selected == "🏠 Dashboard":

    st.title("🏥 HealthAI")

    st.subheader(
        "AI-Powered Disease Prediction Platform"
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Supported Diseases",
            "3"
        )

    with col2:
        st.metric(
            "Model Accuracy",
            "86%"
        )

    with col3:
        st.metric(
            "Predictions Made",
            "500+"
        )

    st.divider()

    st.success("""
    Welcome to HealthAI

    ✔ Predict Diabetes Risk

    ✔ Get Risk Score

    ✔ Receive Recommendations

    ✔ AI Powered Healthcare Assistance
    """)

# ---------------- DIABETES PAGE ---------------- #
elif selected == "🩺 Diabetes Prediction":

    st.title("🩺 Diabetes Risk Assessment")
    st.markdown(
        "Fill in the patient details and medical parameters below."
    )

    st.divider()

    # =====================================
    # PATIENT PROFILE
    # =====================================

    st.subheader("👤 Patient Profile")

    col1, col2 = st.columns(2)

    with col1:

        patient_name = st.text_input(
            "Full Name",
            placeholder="Enter patient name"
        )

        gender = st.selectbox(
            "Gender",
            [
                "Select Gender",
                "Male",
                "Female",
                "Other"
            ]
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=0.0,
            value=None,
            placeholder="Enter height in cm"
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=0.0,
            value=None,
            placeholder="Enter weight in kg"
        )

    # =====================================
    # BMI CALCULATION
    # =====================================

    bmi = None

    if height and weight:

        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            bmi_category = "🔵 Underweight"

        elif bmi < 25:
            bmi_category = "🟢 Normal"

        elif bmi < 30:
            bmi_category = "🟡 Overweight"

        else:
            bmi_category = "🔴 Obese"

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Calculated BMI",
                f"{bmi:.2f}"
            )

        with col2:
            st.metric(
                "BMI Category",
                bmi_category
            )

    st.divider()

    # =====================================
    # MEDICAL PARAMETERS
    # =====================================

    st.subheader("🧪 Medical Parameters")

    col1, col2 = st.columns(2)

    with col1:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0
        )

        glucose = st.number_input(
            "Glucose Level",
            min_value=0.0
        )

        blood_pressure = st.number_input(
            "Blood Pressure",
            min_value=0.0
        )

        skin_thickness = st.number_input(
            "Skin Thickness",
            min_value=0.0
        )

    with col2:

        insulin = st.number_input(
            "Insulin Level",
            min_value=0.0
        )

        dpf = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            format="%.3f"
        )

        age = st.number_input(
            "Age",
            min_value=1
        )

    st.divider()

    # =====================================
    # PREDICT BUTTON
    # =====================================

    if st.button("🔍 Predict Risk"):

        # Validation

        if not patient_name:

            st.error(
                "Please enter patient name."
            )

        elif gender == "Select Gender":

            st.error(
                "Please select gender."
            )

        elif bmi is None:

            st.error(
                "Please enter height and weight."
            )

        else:

            features = [
                pregnancies,
                glucose,
                blood_pressure,
                skin_thickness,
                insulin,
                bmi,
                dpf,
                age
            ]

            prediction, probability = predict_diabetes(
                features
            )

            risk = probability * 100

            # =====================================
            # PATIENT SUMMARY
            # =====================================

            st.subheader("📋 Patient Summary")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Patient",
                    patient_name
                )

            with col2:
                st.metric(
                    "Gender",
                    gender
                )

            with col3:
                st.metric(
                    "Age",
                    age
                )

            with col4:
                st.metric(
                    "BMI",
                    f"{bmi:.2f}"
                )

            st.divider()

            # =====================================
            # PREDICTION RESULT
            # =====================================

            st.subheader("📈 Prediction Result")

            st.metric(
                "Risk Score",
                f"{risk:.2f}%"
            )

            gauge_fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=risk,
                    title={
                        "text": "Diabetes Risk Score"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "darkred"
                        },
                        "steps": [
                            {
                                "range": [0, 30],
                                "color": "#00cc96"
                            },
                            {
                                "range": [30, 70],
                                "color": "#FECB52"
                            },
                            {
                                "range": [70, 100],
                                "color": "#EF553B"
                            }
                        ]
                    }
                )
            )

            gauge_fig.update_layout(
                height=350
            )

            st.plotly_chart(
                gauge_fig,
                width="stretch"
            )

            st.progress(
                int(risk)
            )

            if risk < 30:

                st.success(
                    f"🟢 Low Risk ({risk:.1f}%)"
                )

                risk_level = "Low"

            elif risk < 70:

                st.warning(
                    f"🟡 Moderate Risk ({risk:.1f}%)"
                )

                risk_level = "Moderate"

            else:

                st.error(
                    f"🔴 High Risk ({risk:.1f}%)"
                )

                risk_level = "High"

            st.metric(
                "Risk Category",
                risk_level
            )

            # =====================================
            # AI EXPLANATION
            # =====================================

            st.divider()

            st.subheader("🧠 Risk Factor Analysis")

            risk_factors = {
                "Glucose": glucose,
                "Blood Pressure": blood_pressure,
                "Skin Thickness": skin_thickness,
                "Insulin": insulin,
                "BMI": round(bmi, 2),
                "DPF": dpf,
                "Age": age
            }

            risk_df = pd.DataFrame(
                list(risk_factors.items()),
                columns=["Parameter", "Value"]
            )

            fig = px.bar(
                risk_df,
                x="Parameter",
                y="Value",
                text="Value",
                title="Patient Health Parameters"
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                height=500,
                xaxis_title="Parameters",
                yaxis_title="Values"
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

            st.subheader("🔍 Key Risk Factors")

            risk_messages = []

            if glucose > 140:
                risk_messages.append(
                    f"⚠️ High Glucose Level ({glucose})"
                )

            if bmi > 25:
                risk_messages.append(
                    f"⚠️ Elevated BMI ({bmi:.2f})"
                )

            if age > 45:
                risk_messages.append(
                    f"⚠️ Age Factor ({age})"
                )

            if blood_pressure > 90:
                risk_messages.append(
                    f"⚠️ High Blood Pressure ({blood_pressure})"
                )

            if risk_messages:

                for msg in risk_messages:
                    st.warning(msg)

            else:

                st.success(
                    "✅ No major risk factors detected."
                )

            # =====================================
            # RECOMMENDATIONS
            # =====================================

            st.subheader("📋 Recommendations")

            if risk < 30:

                st.success("""
                ✓ Maintain healthy eating habits

                ✓ Exercise regularly

                ✓ Annual health checkups

                ✓ Maintain healthy weight
                """)

            elif risk < 70:

                st.warning("""
                ✓ Reduce sugar intake

                ✓ Walk 30 minutes daily

                ✓ Monitor blood glucose

                ✓ Maintain proper BMI

                ✓ Avoid processed foods
                """)

            else:

                st.error("""
                ✓ Consult a healthcare professional

                ✓ Follow diabetic diet

                ✓ Regular blood sugar monitoring

                ✓ Increase physical activity

                ✓ Avoid sugary beverages

                ✓ Maintain healthy weight
                """)

            st.divider()

            # ==========================
            # PDF REPORT
            # ==========================

            pdf_file = generate_diabetes_report(
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
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📄 Download PDF Report",
                    data=file,
                    file_name="HealthAI_Report.pdf",
                    mime="application/pdf"
                )

# ====================================================
# HEART DISEASE PAGE
# ====================================================

elif selected == "❤️ Heart Disease Prediction":

    st.title("❤️ Heart Disease Risk Assessment")

    st.markdown(
        "Fill in cardiovascular health parameters below."
    )

    st.divider()

    # =====================================
    # PATIENT PROFILE
    # =====================================

    st.subheader("👤 Patient Profile")

    col1, col2 = st.columns(2)

    with col1:

        patient_name = st.text_input(
            "Patient Name"
        )

        gender = st.selectbox(
            "Gender",
            [
                "Select Gender",
                "Male",
                "Female"
            ],
            key="heart_gender"
        )

    with col2:

        age = st.number_input(
            "Age",
            min_value=1,
            key="heart_age"
        )

    st.divider()

    # =====================================
    # HEART PARAMETERS
    # =====================================

    st.subheader("❤️ Cardiovascular Parameters")

    col1, col2 = st.columns(2)

    with col1:

        cp = st.number_input(
            "Chest Pain Type",
            min_value=0
        )

        trestbps = st.number_input(
            "Resting Blood Pressure"
        )

        chol = st.number_input(
            "Serum Cholesterol"
        )

        fbs = st.number_input(
            "Fasting Blood Sugar"
        )

        restecg = st.number_input(
            "Rest ECG"
        )

        thalach = st.number_input(
            "Maximum Heart Rate"
        )

    with col2:

        exang = st.number_input(
            "Exercise Induced Angina"
        )

        oldpeak = st.number_input(
            "Old Peak"
        )

        slope = st.number_input(
            "Slope"
        )

        ca = st.number_input(
            "Major Vessels"
        )

        thal = st.number_input(
            "Thal"
        )

    st.divider()

    if st.button("❤️ Predict Heart Risk"):

        if not patient_name:

            st.error(
                "Please enter patient name."
            )

        elif gender == "Select Gender":

            st.error(
                "Please select gender."
            )

        else:

            sex = 1 if gender == "Male" else 0

            features = [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal
            ]

            prediction, probability = predict_heart(
                features
            )

            risk = probability * 100

            st.subheader("📋 Patient Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Patient",
                    patient_name
                )

            with col2:
                st.metric(
                    "Gender",
                    gender
                )

            with col3:
                st.metric(
                    "Age",
                    age
                )

            st.divider()

            st.subheader(
                "📈 Heart Disease Risk"
            )

            st.metric(
                "Risk Score",
                f"{risk:.2f}%"
            )

            gauge_fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=risk,
                    title={
                        "text": "Heart Disease Risk Score"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "darkred"
                        },
                        "steps": [
                            {
                                "range": [0, 30],
                                "color": "#00cc96"
                            },
                            {
                                "range": [30, 70],
                                "color": "#FECB52"
                            },
                            {
                                "range": [70, 100],
                                "color": "#EF553B"
                            }
                        ]
                    }
                )
            )

            gauge_fig.update_layout(
                height=350
            )

            st.plotly_chart(
                gauge_fig,
                width="stretch"
            )

            st.progress(
                int(risk)
            )

            if risk < 30:

                risk_level = "Low"

                st.success(
                    f"🟢 Low Risk ({risk:.1f}%)"
                )

            elif risk < 70:

                risk_level = "Moderate"

                st.warning(
                    f"🟡 Moderate Risk ({risk:.1f}%)"
                )

            else:

                risk_level = "High"

                st.error(
                    f"🔴 High Risk ({risk:.1f}%)"
                )

            st.divider()

            # =====================================
            # HEART RISK FACTORS
            # =====================================

            st.subheader(
                "🔍 Heart Risk Factor Evaluation"
            )

            risk_factors = []

            if chol > 240:
                risk_factors.append(
                    f"⚠️ High Cholesterol Level ({chol})"
                )

            if trestbps > 140:
                risk_factors.append(
                    f"⚠️ High Blood Pressure ({trestbps})"
                )

            if thalach < 120:
                risk_factors.append(
                    f"⚠️ Low Maximum Heart Rate ({thalach})"
                )

            if age > 50:
                risk_factors.append(
                    f"⚠️ Age Related Risk ({age})"
                )

            if exang == 1:
                risk_factors.append(
                    "⚠️ Exercise Induced Angina Detected"
                )

            if oldpeak > 2:
                risk_factors.append(
                    f"⚠️ Abnormal ST Depression ({oldpeak})"
                )

            if risk_factors:

                for factor in risk_factors:
                    st.warning(factor)

            else:

                st.success(
                    "✅ No major cardiovascular risk factors detected."
                )

            # =====================================
            # HEART HEALTH ANALYSIS
            # =====================================

            st.subheader("📊 Heart Health Analysis")

            heart_parameters = {
                "Age": age,
                "Blood Pressure": trestbps,
                "Cholesterol": chol,
                "Max Heart Rate": thalach,
                "Old Peak": oldpeak,
                "Major Vessels": ca
            }

            heart_df = pd.DataFrame(
                list(heart_parameters.items()),
                columns=["Parameter", "Value"]
            )

            fig = px.bar(
                heart_df,
                x="Parameter",
                y="Value",
                text="Value",
                title="Cardiovascular Health Parameters"
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                height=500,
                xaxis_title="Parameters",
                yaxis_title="Values"
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

            # =====================================
            # RECOMMENDATIONS
            # =====================================

            st.subheader("📋 Recommendations")

            if risk_level == "Low":

                st.success("""
                ✓ Maintain healthy lifestyle

                ✓ Regular exercise

                ✓ Balanced diet

                ✓ Annual heart checkup
                """)

            elif risk_level == "Moderate":

                st.warning("""
                ✓ Reduce cholesterol intake

                ✓ Monitor blood pressure

                ✓ Exercise regularly

                ✓ Avoid smoking
                """)

            else:

                st.error("""
                ✓ Consult cardiologist

                ✓ Follow heart-healthy diet

                ✓ Reduce salt intake

                ✓ Regular ECG monitoring

                ✓ Increase physical activity
                """)

            st.divider()

            # =====================================
            # HEART PDF REPORT
            # =====================================

            pdf_file = generate_heart_report(
                patient_name,
                gender,
                age,
                risk,
                risk_level,
                chol,
                trestbps,
                thalach
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📄 Download Heart Report",
                    data=file,
                    file_name="Heart_Disease_Report.pdf",
                    mime="application/pdf"
                )

# ====================================================
# PARKINSON'S PAGE
# ====================================================

elif selected == "🧠 Parkinson's Prediction":

    st.title("🧠 Parkinson's Disease Assessment")

    st.markdown(
        "Fill in voice analysis parameters below."
    )

    st.divider()

    # =====================================
    # PATIENT PROFILE
    # =====================================

    st.subheader("👤 Patient Profile")

    col1, col2 = st.columns(2)

    with col1:

        patient_name = st.text_input(
            "Patient Name",
            key="park_name"
        )

        gender = st.selectbox(
            "Gender",
            ["Select Gender", "Male", "Female"],
            key="park_gender"
        )

    with col2:

        age = st.number_input(
            "Age",
            min_value=1,
            key="park_age"
        )

    st.divider()

    # =====================================
    # VOICE ANALYSIS PARAMETERS
    # =====================================

    st.subheader(
        "🧪 Voice Analysis Parameters"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.number_input("Fo(Hz)")
        fhi = st.number_input("Fhi(Hz)")
        flo = st.number_input("Flo(Hz)")
        jitter = st.number_input("Jitter %")
        jitter_abs = st.number_input("Jitter Abs")
        rap = st.number_input("RAP")
        ppq = st.number_input("PPQ")
        ddp = st.number_input("DDP")

    with col2:
        shimmer = st.number_input("Shimmer")
        shimmer_db = st.number_input("Shimmer dB")
        apq3 = st.number_input("APQ3")
        apq5 = st.number_input("APQ5")
        apq = st.number_input("APQ")
        dda = st.number_input("DDA")
        nhr = st.number_input("NHR")

    with col3:
        hnr = st.number_input("HNR")
        rpde = st.number_input("RPDE")
        dfa = st.number_input("DFA")
        spread1 = st.number_input("Spread1")
        spread2 = st.number_input("Spread2")
        d2 = st.number_input("D2")
        ppe = st.number_input("PPE")

    st.divider()

    # =====================================
    # PREDICT BUTTON
    # =====================================

    if st.button("🧠 Predict Parkinson's Risk"):

        if not patient_name:

            st.error(
                "Please enter patient name."
            )

        elif gender == "Select Gender":

            st.error(
                "Please select gender."
            )

        else:

            features = [
                fo, fhi, flo, jitter, jitter_abs,
                rap, ppq, ddp,
                shimmer, shimmer_db,
                apq3, apq5, apq, dda,
                nhr, hnr,
                rpde, dfa,
                spread1, spread2,
                d2, ppe
            ]

            prediction, probability = predict_parkinsons(
                features
            )

            risk = probability * 100

            # =====================================
            # PATIENT SUMMARY
            # =====================================

            st.subheader("📋 Patient Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Patient",
                    patient_name
                )

            with col2:
                st.metric(
                    "Gender",
                    gender
                )

            with col3:
                st.metric(
                    "Age",
                    age
                )

            st.divider()

            # =====================================
            # PREDICTION RESULT
            # =====================================

            st.subheader("📈 Parkinson's Disease Risk")

            st.metric(
                "Risk Score",
                f"{risk:.2f}%"
            )

            gauge_fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=risk,
                    title={
                        "text": "Parkinson's Risk Score"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "darkred"
                        },
                        "steps": [
                            {
                                "range": [0, 30],
                                "color": "#00cc96"
                            },
                            {
                                "range": [30, 70],
                                "color": "#FECB52"
                            },
                            {
                                "range": [70, 100],
                                "color": "#EF553B"
                            }
                        ]
                    }
                )
            )

            gauge_fig.update_layout(
                height=350
            )

            st.plotly_chart(
                gauge_fig,
                width="stretch"
            )

            st.progress(
                int(risk)
            )

            if risk < 30:

                risk_level = "Low"

                st.success(
                    f"🟢 Low Risk ({risk:.1f}%)"
                )

            elif risk < 70:

                risk_level = "Moderate"

                st.warning(
                    f"🟡 Moderate Risk ({risk:.1f}%)"
                )

            else:

                risk_level = "High"

                st.error(
                    f"🔴 High Risk ({risk:.1f}%)"
                )

            st.divider()

            # =====================================
            # NEUROLOGICAL RISK ANALYSIS
            # =====================================

            st.subheader(
                "🔍 Neurological Risk Analysis"
            )

            risk_factors = []

            if ppe > 0.25:
                risk_factors.append(
                    f"⚠️ High PPE ({ppe})"
                )

            if rpde > 0.5:
                risk_factors.append(
                    f"⚠️ High RPDE ({rpde})"
                )

            if nhr > 0.03:
                risk_factors.append(
                    f"⚠️ Elevated NHR ({nhr})"
                )

            if risk_factors:

                for factor in risk_factors:
                    st.warning(factor)

            else:

                st.success(
                    "✅ No major Parkinson's indicators detected."
                )

            # =====================================
            # VOICE PARAMETER ANALYSIS
            # =====================================

            st.subheader("📊 Voice Parameter Analysis")

            park_parameters = {
                "PPE": ppe,
                "RPDE": rpde,
                "DFA": dfa,
                "NHR": nhr,
                "HNR": hnr,
                "Jitter %": jitter
            }

            park_df = pd.DataFrame(
                list(park_parameters.items()),
                columns=["Parameter", "Value"]
            )

            fig = px.bar(
                park_df,
                x="Parameter",
                y="Value",
                text="Value",
                title="Voice Analysis Parameters"
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                height=500,
                xaxis_title="Parameters",
                yaxis_title="Values"
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

            # =====================================
            # RECOMMENDATIONS
            # =====================================

            st.subheader("📋 Recommendations")

            if risk_level == "Low":

                st.success("""
                ✓ Maintain regular physical activity

                ✓ Routine neurological checkups

                ✓ Balanced diet rich in antioxidants

                ✓ Adequate sleep and stress management
                """)

            elif risk_level == "Moderate":

                st.warning("""
                ✓ Consult a neurologist for evaluation

                ✓ Monitor tremors and motor symptoms

                ✓ Engage in regular physical therapy

                ✓ Track voice and speech changes
                """)

            else:

                st.error("""
                ✓ Consult a neurologist promptly

                ✓ Consider comprehensive movement disorder evaluation

                ✓ Begin physical and speech therapy

                ✓ Regular monitoring of disease progression
                """)

            st.divider()

            # =====================================
            # PARKINSON'S PDF REPORT
            # =====================================

            pdf_file = generate_parkinsons_report(
                patient_name,
                gender,
                age,
                risk,
                risk_level
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📄 Download Parkinson's Report",
                    data=file,
                    file_name="Parkinsons_Report.pdf",
                    mime="application/pdf"
                )
# ====================================================
# AI HEALTH ASSISTANT
# ====================================================

elif selected == "🤖 AI Health Assistant":

    st.title("🤖 HealthAI Assistant")

    st.markdown("""
    Ask any health-related question and get AI-powered guidance.

    """)

    st.divider()

    user_question = st.text_area(
        "Ask your question",
        placeholder="Example: What foods help lower cholesterol?"
    )

    if st.button("🚀 Ask AI"):

        if not user_question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Thinking..."
            ):

                response = ask_health_assistant(
                    user_question
                )

            st.success("AI Response")

            st.markdown(response)
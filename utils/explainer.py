import joblib
import pandas as pd
import shap

model = joblib.load(
    "models/diabetes_model.pkl"
)

columns = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

explainer = shap.TreeExplainer(model)


def get_shap_values(features):

    input_df = pd.DataFrame(
        [features],
        columns=columns
    )

    shap_values = explainer.shap_values(
        input_df
    )

    return shap_values, input_df
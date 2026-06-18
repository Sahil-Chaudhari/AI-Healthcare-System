import joblib
import pandas as pd

model = joblib.load(
    "models/diabetes_model.pkl"
)

def predict_diabetes(features):

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

    input_df = pd.DataFrame(
        [features],
        columns=columns
    )

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(
        input_df
    )[0][1]

    return prediction, probability
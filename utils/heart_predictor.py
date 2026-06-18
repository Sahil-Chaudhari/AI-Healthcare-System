import joblib
import pandas as pd

heart_model = joblib.load(
    "models/heart_disease_model.pkl"
)

heart_columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]


def predict_heart(features):

    input_df = pd.DataFrame(
        [features],
        columns=heart_columns
    )

    prediction = heart_model.predict(
        input_df
    )[0]

    probability = heart_model.predict_proba(
        input_df
    )[0][1]

    return prediction, probability
import joblib
import pandas as pd

parkinsons_model = joblib.load(
    "models/parkinsons_model.pkl"
)

columns = [
    'MDVP:Fo(Hz)',
    'MDVP:Fhi(Hz)',
    'MDVP:Flo(Hz)',
    'MDVP:Jitter(%)',
    'MDVP:Jitter(Abs)',
    'MDVP:RAP',
    'MDVP:PPQ',
    'Jitter:DDP',
    'MDVP:Shimmer',
    'MDVP:Shimmer(dB)',
    'Shimmer:APQ3',
    'Shimmer:APQ5',
    'MDVP:APQ',
    'Shimmer:DDA',
    'NHR',
    'HNR',
    'RPDE',
    'DFA',
    'spread1',
    'spread2',
    'D2',
    'PPE'
]


def predict_parkinsons(features):

    input_df = pd.DataFrame(
        [features],
        columns=columns
    )

    prediction = parkinsons_model.predict(
        input_df
    )[0]

    probability = parkinsons_model.predict_proba(
        input_df
    )[0][1]

    return prediction, probability
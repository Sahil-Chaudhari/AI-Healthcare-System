import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("parkinsons.csv")

# Drop name column
df = df.drop("name", axis=1)

# Features and target
X = df.drop("status", axis=1)
y = df["status"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(
    model,
    "models/parkinsons_model.pkl"
)

print("Parkinson's model saved successfully!")
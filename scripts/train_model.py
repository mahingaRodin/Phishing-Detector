import pandas as pd # type: ignore
import numpy as np # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.metrics import accuracy_score, classification_report # type: ignore
import joblib # type: ignore

# Load dataset (replace with your dataset)
df = pd.read_csv("data/phishing_data.csv")  # You need a dataset

# Split into training/testing
X = df.drop(columns=["label"])  # Features
y = df["label"]  # Phishing (1) or Legitimate (0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/phishing_detector.pkl")

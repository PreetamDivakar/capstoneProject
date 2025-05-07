import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("workload_dataset.csv")
X = df.drop("target_platform", axis=1)
y = df["target_platform"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "orchestrator_model.pkl")
print("✅ Model trained and saved to orchestrator_model.pkl")

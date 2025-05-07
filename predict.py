import joblib
import pandas as pd

# Load model
model = joblib.load("orchestrator_model.pkl")

# Example workload
example = {
    "cpu_cores": 1,
    "memory_mb": 256,
    "latency_sensitive": 1,
    "execution_time_sec": 3,
    "data_size_mb": 10
}

# Print input features
print("Workload Features:")
for key, value in example.items():
    print(f"  - {key}: {value}")


features = pd.DataFrame([example])
# Predict
prediction = model.predict(features)[0]

# Print result
print(f"\n🚀 Deploy to: {prediction}")

## Directory Structure

project/

├── workload_dataset.csv        # Dataset of workloads

├── train_model.py              # Script to train and save the ML model

├── predict.py                  # Script to load the model and predict

├── orchestrator_model.pkl      # Trained model (output of train_model.py)

├── requirements.txt            # Dependencies

└── README.md                   # Project description


## ML-Based Orchestrator

This simple Python project trains a machine learning model to decide whether to deploy a workload to a serverless or traditional cloud environment based on its characteristics.


## 📊 Dataset Feature Description

| Column             | Type                | Example   | Meaning                                                                                         | Importance in Classification                                                                                          |
|--------------------|---------------------|-----------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `cpu_cores`        | Integer             | 1         | Number of virtual CPU cores needed for the workload                                             | 💡 **High** — Serverless platforms (like AWS Lambda) have a limit on CPU usage. Low-CPU tasks are better for serverless; high-CPU workloads suit traditional. |
| `memory_mb`        | Integer             | 512       | Amount of memory (RAM) in megabytes required                                                    | 💡 **High** — Serverless functions have memory caps (e.g., AWS Lambda max 10 GB). Large-memory workloads need traditional setups. |
| `latency_sensitive`| Integer (0 or 1)    | 1         | Indicates if the workload is sensitive to delay (1 = Yes, 0 = No)                               | ⚡ **High** — Serverless can introduce cold start latency. If latency is critical, prefer a pre-warmed traditional environment or managed Kubernetes. |
| `execution_time_sec`| Integer            | 5         | Expected duration of the task in seconds                                                        | ⏱️ **High** — Serverless has time limits (e.g., 15 min in AWS Lambda). Long-running processes need traditional deployment. |
| `data_size_mb`     | Integer             | 10        | Size of data to be processed or transferred                                                     | 📦 **Medium** — Very large data workloads (e.g., image/video processing, big analytics) may be more efficient or feasible in a traditional setup. |
| `target_platform`  | Categorical         | serverless or traditional | The label indicating the ideal platform (what the model learns to predict)           | 🎯 **Target Variable** — Used by the ML model to learn patterns from input features.                                 |



## Cloud Platforms and Tools

| Platform           | Traditional Tool           | Serverless Tool           | Hybrid Tool                                | Free for Students? | Student Cost                                             |
|--------------------|----------------------------|----------------------------|--------------------------------------------|--------------------|----------------------------------------------------------|
| **AWS**            | EC2                        | Lambda                     | Step Functions, Fargate, EKS + KNative    | ✅ Yes (AWS Educate) | $100+ credits via AWS Educate or GitHub Student Pack    |
| **Azure**          | AKS (Azure Kubernetes Service) | Azure Functions            | Durable Functions, Logic Apps             | ✅ Yes             | $100+ credits via Azure for Students                    |
| **Google Cloud (GCP)** | GKE (Google Kubernetes Engine) | Cloud Functions            | Workflows, Cloud Run + GKE                | ✅ Yes             | $300 credits (valid for 90 days) via GCP Free Tier      |

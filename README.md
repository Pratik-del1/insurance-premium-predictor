# 🛡️ Insurance Premium Category Predictor

An end-to-end Machine Learning application that predicts the **insurance premium category** of a customer based on demographic and lifestyle information.

The application exposes a REST API using **FastAPI**, provides an interactive interface using **Streamlit**, and is containerized using **Docker** for easy deployment.

---

## 🚀 Features

- Predict Insurance Premium Category
- FastAPI REST API
- Interactive Streamlit Frontend
- Input Validation using Pydantic
- Dockerized Application
- Swagger API Documentation
- Machine Learning Model Integration
- Clean Project Structure

---

## 🛠 Tech Stack

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Deployment
- Docker

---

# 📂 Project Structure

```
insurance-premium-predictor
│
├── config/
├── model/
├── schema/
├── app.py
├── frontend.py
├── Dockerfile
├── requirements.txt
├── README.md
└── insurance.csv
```

---

# ⚙️ Workflow

```
User
    │
    ▼
Streamlit Frontend
    │
    ▼
FastAPI Backend
    │
    ▼
Load Trained ML Model
    │
    ▼
Predict Premium Category
    │
    ▼
Return Prediction
```

---

# 📊 Model Workflow

1. Collect user information.
2. Validate input using Pydantic.
3. Preprocess the input.
4. Load the trained Machine Learning model.
5. Predict the insurance premium category.
6. Return prediction to the frontend.

---

## Swagger UI

```
http://localhost:8888/docs
```

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t insurance-premium-api .
```

## Run Docker Container

```bash
docker run -p 8888:8888insurance-premium-api
```

# ▶ Running Locally

Clone the repository

```bash
git clone https://github.com/Pratik-del1/insurance-premium-predictor.git
```

Navigate to the project

```bash
cd insurance-premium-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Run Streamlit

```bash
streamlit run frontend.py
```

---

# 🔮 Future Improvements

- User Authentication
- Cloud Deployment (AWS/Render)
- Model Monitoring
- CI/CD Pipeline
- Database Integration
- Explainable AI using SHAP
- Model Retraining Pipeline

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/predict` | Predict Insurance Premium Category |
| GET | `/docs` | Swagger Documentation |

---

# 👨‍💻 Author

**Pratik Srivastava**

GitHub:
https://github.com/Pratik-del1

---

# ⭐ If you found this project useful, consider giving it a star.

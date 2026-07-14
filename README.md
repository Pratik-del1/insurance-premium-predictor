# 🏥 Insurance Premium Category Predictor

An end-to-end Machine Learning application that predicts an insurance premium category based on a user's demographic and lifestyle information.

The project combines a trained Scikit-learn pipeline with a FastAPI backend for inference and a Streamlit frontend for an interactive user experience.

---

## 🚀 Features

- Predicts insurance premium category in real time
- FastAPI REST API for model serving
- Interactive Streamlit web interface
- Pydantic data validation
- Automatic feature engineering using computed fields
- Scikit-learn Pipeline for preprocessing and prediction
- Clean and modular project structure

---

## 🛠️ Tech Stack

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- Streamlit

---

## 📂 Project Structure

```
Insurance-Premium-Predictor/
│
├── app.py               # FastAPI backend
├── frontend.py          # Streamlit frontend
├── model.pkl            # Trained ML model
├── model.ipynb          # Model training notebook
├── insurance.csv        # Dataset
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/insurance-premium-predictor.git

cd insurance-premium-predictor
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Start the FastAPI server

```bash
uvicorn app:app --reload
```

FastAPI Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Start the Streamlit frontend

```bash
streamlit run frontend.py
```

Streamlit will be available at

```
http://localhost:8501
```

---

## 📊 Input Features

The model predicts the insurance premium category using:

| Feature | Description |
|----------|-------------|
| Age | User's age |
| Weight | Weight in kilograms |
| Height | Height in meters |
| Annual Income | Income in Lakhs Per Annum |
| Smoker | Smoking status |
| City | User's city |
| Occupation | Employment category |

---

## ⚡ Engineered Features

The API automatically computes additional features before prediction:

- BMI (Body Mass Index)
- Age Group
- Lifestyle Risk
- City Tier

These engineered features are passed to the trained machine learning model.

---

## 🔗 API Endpoint

### POST `/predict`

Example Request

```json
{
    "age": 30,
    "weight": 72,
    "height": 1.75,
    "income_lpa": 12,
    "smoker": true,
    "city": "Mumbai",
    "occupation": "private_job"
}
```

Example Response

```json
{
    "predicted_category": "Medium"
}
```

---

## 🧠 Machine Learning Pipeline

The project uses a Scikit-learn Pipeline that includes:

- Feature Engineering
- OneHotEncoder for categorical variables
- Data preprocessing
- Machine Learning Classifier
- Serialized model using Pickle

---

## 📌 Future Improvements

- Docker support
- Cloud deployment (AWS / Azure / GCP)
- Model versioning with MLflow
- Authentication for API endpoints
- Batch prediction support
- CI/CD pipeline using GitHub Actions

---

## 👨‍💻 Author

**Pratik Srivastava**

# 🩺 Diabetes Prediction System

A Machine Learning-based web application that predicts the risk of diabetes using patient health information. The application is built with **Flask** and uses multiple machine learning algorithms to compare prediction performance.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-Educational-green)

---

# 📖 Project Overview

The Diabetes Prediction System is designed to assist in predicting whether a patient is at risk of diabetes based on medical information such as age, BMI, HbA1c level, blood glucose level, smoking history, hypertension, and heart disease.

The project compares the performance of three different machine learning classification algorithms and deploys the best-performing model in a Flask web application.

---

# ✨ Features

- Predicts diabetes risk instantly
- Interactive and responsive web interface
- Trained using real-world diabetes dataset
- Compares multiple machine learning models
- Displays prediction confidence
- Professional healthcare-inspired UI
- Data preprocessing and feature engineering
- Model evaluation with performance metrics

---

# 🛠 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy

### Data Visualization

- Matplotlib

### Web Development

- Flask
- HTML5
- CSS3
- Bootstrap 5

### Model Serialization

- Joblib

---

# 📂 Project Structure

```
Diabetes-Prediction-System
│
├── data/
│   └── raw/
│       └── diabetes_prediction_dataset.csv
│
├── models/
│   ├── logistic_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   ├── gender_encoder.pkl
│   └── smoking_encoder.pkl
│
├── src/
│   ├── data/
│   ├── eda/
│   ├── feature_engineering/
│   ├── prediction/
│   └── training/
│
├── static/
│   └── css/
│
├── templates/
│   └── index.html
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Information

The project uses the **Diabetes Prediction Dataset** containing patient health records.

### Features

- Gender
- Age
- Hypertension
- Heart Disease
- Smoking History
- BMI
- HbA1c Level
- Blood Glucose Level

### Target

```
0 → Non-Diabetic
1 → Diabetic
```

---

# 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

---

# 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|----------|-----------|--------|----------|
| Logistic Regression | 95.95% | 86.84% | 63.80% | 73.56% |
| Decision Tree | **97.16%** | **100.00%** | 67.81% | **80.82%** |
| Random Forest | 96.95% | 94.90% | **69.10%** | 79.97% |

---

# ⚙️ Machine Learning Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Encoding
      │
      ▼
Train-Test Split
      │
      ▼
Feature Scaling
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Comparison
      │
      ▼
Save Best Model
      │
      ▼
Flask Web Application
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Gaurav-05-source/Diabetes-Prediction-System.git
```

Move into the project directory

```bash
cd Diabetes-Prediction-System
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 🖥 Application Screenshots

## Home Page

> *(Add a screenshot here)*

```
images/home.png
```

---

## Prediction Form

> *(Add a screenshot here)*

```
images/prediction_form.png
```

---

## Prediction Result

> *(Add a screenshot here)*

```
images/result.png
```

---

# 📌 Future Enhancements

- User authentication
- Patient history storage
- PDF medical report generation
- Cloud deployment
- Explainable AI (Feature Importance)
- Additional machine learning algorithms
- REST API integration

---

# 👨‍💻 Author

**Gaurav Devale**

Computer Engineering Student

GitHub

https://github.com/Gaurav-05-source

---

# ⭐ If you found this project useful, consider giving it a star!
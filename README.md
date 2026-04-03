# 🚀 FastAPI Patient Management API

A simple FastAPI-based backend project to manage and retrieve patient data.  
Built as part of my learning journey while transitioning from JavaScript to Python 🐍

---

## 📌 Features

- 📋 View all patients  
- 🔍 Get patient by ID  
- 📊 Sort patients by height, weight, or BMI  
- ⚡ FastAPI-based high-performance API  

---

## 🛠️ Tech Stack

- Python 🐍  
- FastAPI ⚡  
- JSON (for data storage)  

---

## 📂 Project Structure
├── app.py # Main FastAPI application
├── patient.json # Patient dataset
├── README.md # Project documentation

Learning Goal
Transitioning from JavaScript → Python
Understanding FastAPI
Building backend APIs

---

## ▶️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/redhead-coffee/learning-FastAPI
cd sybau
python -m venv venv
venv\Scripts\activate   # Windows
pip install fastapi uvicorn pyd

uvicorn app:app --reload

🌐 API Endpoints
🔹 Home
GET /
🔹 View All Patients
GET /view
🔹 Get Patient by ID
GET /patient/{patient_id}

Example:

/patient/P001
🔹 Sort Patients
GET /sort?sort_by=height&Order=asc


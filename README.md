# 🧠 Text-Based Personality Prediction using NLP

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://personality-predictor-6ds64zesypfywrs6cg8rbq.streamlit.app/)
[![GitHub license](https://img.shields.io/github/license/Rishabh5002/Personality-Predictor)](https://github.com/Rishabh5002/Personality-Predictor)

## 📌 Abstract
This project implements a Natural Language Processing (NLP) framework to predict human personality traits based on the Myers-Briggs Type Indicator (MBTI). By analyzing linguistic patterns in unstructured text, the system uses a pipeline of TF-IDF vectorization and an ensemble of binary Logistic Regression classifiers to predict traits across four axes: Introversion vs. Extroversion, Intuition vs. Sensing, Feeling vs. Thinking, and Judging vs. Perceiving.

---

## 🎯 Project Breakdown (Handwritten Format)

### 1. Objective
To build a machine learning model that automates psychological profiling by analyzing text data, providing a faster and data-driven alternative to traditional personality surveys.

### 2. Dataset
- **Source:** Kaggle MBTI Dataset (8,600+ rows).
- **Features:** Cleaned social media posts.
- **Target:** MBTI personality labels (e.g., INFP, ENTJ).

### 3. Methodology
The project follows a modular NLP pipeline:
- **Preprocessing:** Lowercasing, URL removal, special character filtering, and NLTK-based **Lemmatization**.
- **Conversion to Numeric:** **TF-IDF Vectorization** (5,000 features) to quantify word importance.
- **Model Building:** Transitioned from a 16-class classifier to a **4-Axis Binary Ensemble** using Logistic Regression.
- **Training/Testing:** 80/20 data split.

### 4. Evaluation & Results
The model achieves high performance by treating each personality dimension as a separate binary classification task:
- **Average Accuracy:** 84.39%
- **Best Performing Axis (N-S):** 88.01%
- **Baseline Accuracy Improvement:** Increased from 63.05% (16-class) to 84.39% (average axis).

---

## 🚀 Live Demo
You can test the trained model here:  
👉 **[Personality Predictor Web App](https://personality-predictor-6ds64zesypfywrs6cg8rbq.streamlit.app/)**

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Rishabh5002/Personality-Predictor.git](https://github.com/Rishabh5002/Personality-Predictor.git)
   cd Personality-Predictor

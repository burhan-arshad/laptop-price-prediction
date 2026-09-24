# Laptop Price Predictor

A Machine Learning application that predicts laptop prices based on specifications such as brand, RAM, storage, screen size, CPU, and GPU.

## 🚀 Live Demo

https://laptop-price-prediction-burhan.streamlit.app/

## 📌 Project Overview

This project uses Machine Learning to estimate the price of a laptop based on its hardware specifications.

The project covers the basic Machine Learning workflow:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Feature selection
* Categorical feature encoding
* Train-test split
* Regression model training
* Model evaluation
* Streamlit deployment

## 📊 Dataset

The project uses the **Laptop Price** dataset from Kaggle.

**Dataset:**
https://www.kaggle.com/datasets/muhammetvarl/laptop-price

The dataset contains laptop specifications and their corresponding prices.

## 💻 Features

The model uses laptop specifications such as:

* Brand
* RAM
* Storage
* Screen size
* CPU
* GPU
* Other hardware specifications

## 🤖 Machine Learning

This is a **regression problem**, where the model predicts a continuous laptop price.

The project uses:

**Random Forest Regressor**

Model performance can be evaluated using regression metrics such as:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

## 🖥️ Streamlit App

The trained model is integrated into a Streamlit web application.

Users can enter laptop specifications and receive an estimated laptop price through the web interface.

## 🛠️ Tech Stack

* Python
* pandas
* NumPy
* scikit-learn
* Streamlit

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/burhan-arshad/laptop-price-prediction.git
cd laptop-price-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 👨‍💻 Author

**Burhan Arshad**

GitHub: https://github.com/burhan-arshad

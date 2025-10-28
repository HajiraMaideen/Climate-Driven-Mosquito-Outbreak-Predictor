# 🌦️ Climate-Driven Mosquito Outbreak Predictor

🦟 An AI-powered system to predict mosquito outbreak risks using real-time climate data

### 📘 Project Overview

The Climate-Driven Mosquito Outbreak Predictor is an AI-powered web application that forecasts mosquito outbreak risks and rainfall likelihood based on real-time weather data.
It leverages a Random Forest Classifier trained on Tamil Nadu’s climatic conditions to analyze key environmental factors such as temperature, humidity, rainfall, surface pressure, cloud cover, and wind speed — identifying conditions favorable for mosquito breeding and potential disease outbreaks.

This project serves as an Early Warning System (EWS) to assist public health authorities, environmental agencies, and citizens in taking timely preventive measures.

### 🚀 Features

✅ Predicts rainfall likelihood using a trained Random Forest model

✅ Estimates mosquito outbreak risk levels (High, Moderate, Low)

✅ Accepts real-time weather inputs from users

✅ Displays color-coded outbreak predictions for easy interpretation

✅ Built with Streamlit for an interactive dashboard interface

✅ Supports Tamil Nadu district-wise predictions

### 🧠 Model Description

##### Algorithm: 
Random Forest Classifier

##### Libraries Used: 
scikit-learn, pandas, numpy, joblib

##### Training Data: 
Weather features including:

temperature_2m – Air temperature (°C)

relative_humidity_2m – Humidity level (%)

dew_point_2m – Dew point (°C)

precipitation – Rainfall amount (mm)

rain_today – Rain indicator (mm)

surface_pressure – Atmospheric pressure (hPa)

cloud_cover – Cloud cover (%)

cloud_cover_low – Low-altitude cloud cover (%)

wind_speed_10m – Wind speed (m/s)

wind_direction_10m – Wind direction

city – District name

time – Observation timestamp

### 💻 Tech Stack
| Component        | Technology                              |
| ---------------- | --------------------------------------- |
| Machine Learning | scikit-learn (Random Forest Classifier) |
| Frontend         | Streamlit                               |
| Backend          | Python                                  |
| Data Processing  | pandas, numpy                           |
| Model Storage    | joblib                                  |
| Visualization    | matplotlib (optional for trends)        |

### 🧩 How It Works

1. Input real-time weather parameters such as temperature, humidity, and precipitation.

2. The system encodes the inputs numerically and scales them using MinMaxScaler.

3. The pre-trained Random Forest model predicts:
   
        Rain likelihood (Yes/No)
   
        Rain probability (%)

5. A heuristic rule determines mosquito outbreak risk:
   
        High: Humidity > 65%, Temperature > 25°C, Precipitation > 3 mm
   
        Moderate: Humidity > 50%, Precipitation > 1 mm
   
        Low: Otherwise

7. Results are displayed with color-coded messages and emojis for clarity.

### ⚙️ Installation Guide

##### 🔧 Prerequisites
      Make sure you have the following installed:
      
      Python 3.8 or higher

#####     pip (Python package manager)

### 📦 Install Dependencies

        pip install streamlit pandas numpy scikit-learn joblib matplotlib

### 📁 Project Structure

        ├── random_forest_model.joblib

        ├── app.py                      # Streamlit application

        ├── climate_mosquito_data.csv   # Training dataset

        ├── README.md                   # Project documentation

### ▶️ Run the App

In your terminal, navigate to the project folder and run:

        streamlit run app.py

### 🌍 Example Input

        Enter district: Coimbatore

        Enter temperature (°C): 30

        Enter humidity (%): 60

        Enter dew point (°C): 25

        Enter precipitation (mm): 0

        Enter rain today (mm): 0

        Enter surface pressure (hPa): 1010

        Enter cloud cover (%): 30

        Enter low-altitude cloud cover (%): 10

        Enter wind speed (m/s): 2

        Enter wind direction: NW



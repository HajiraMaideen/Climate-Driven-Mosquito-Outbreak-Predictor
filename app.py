import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from sklearn.preprocessing import MinMaxScaler

# Load trained Random Forest model
rf_model = load('random_forest_model.joblib')

# Streamlit App
st.set_page_config(page_title="Tamil Nadu District Wise Mosquito Outbreak Prediction", page_icon="🌦️", layout="centered")

st.title("🌦️ Tamil Nadu Weather & Mosquito Outbreak Predictor")
st.write("""
This app predicts whether it will **rain today** and the **likelihood of a mosquito outbreak**  
based on real-time weather parameters.  
**Model used:** Random Forest (trained on Tamil Nadu weather data)
""")

# Input Section
st.header("Enter Weather Parameters:")

city = st.text_input("🏙️ Enter District / City Name", "Chennai")

temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, max_value=60.0, value=30.0)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
dew_point = st.number_input("💨 Dew Point (°C)", min_value=-20.0, max_value=40.0, value=22.0)
precipitation = st.number_input("🌧️ Precipitation (mm)", min_value=0.0, max_value=500.0, value=5.0)
rain_today = st.number_input("🌦️ Rain Today (mm)", min_value=0.0, max_value=500.0, value=0.0)
pressure = st.number_input("🌬️ Surface Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1010.0)
cloud_cover = st.number_input("☁️ Cloud Cover (%)", min_value=0.0, max_value=100.0, value=50.0)
cloud_low = st.number_input("🌫️ Low-altitude Cloud Cover (%)", min_value=0.0, max_value=100.0, value=40.0)
wind_speed = st.number_input("💨 Wind Speed (m/s)", min_value=0.0, max_value=100.0, value=5.0)
wind_dir = st.text_input("🧭 Wind Direction", "NE")

# Prediction Button
if st.button("🔍 Predict Weather & Outbreak"):
    # Simple encoding for categorical inputs
    wind_dir_encoded = hash(wind_dir.lower()) % 100
    city_encoded = hash(city.lower()) % 100

    # Numeric feature array
    input_features = np.array([[city_encoded, temperature, humidity, dew_point, precipitation, rain_today,
                                pressure, cloud_cover, cloud_low, wind_speed, wind_dir_encoded]])

    # Scale numeric data
    scaler = MinMaxScaler()
    scaled_input = scaler.fit_transform(input_features)

    # Weather prediction
    prediction = rf_model.predict(scaled_input)
    rain_prob = rf_model.predict_proba(scaled_input)[0][1] * 100  # probability %

    # Mosquito outbreak logic (simple heuristic based on climate)
    if humidity > 65 and temperature > 25 and precipitation > 3:
        outbreak_risk = "High 🦟"
        risk_color = "red"
    elif humidity > 50 and precipitation > 1:
        outbreak_risk = "Moderate ⚠️"
        risk_color = "orange"
    else:
        outbreak_risk = "Low ✅"
        risk_color = "green"

    # Results
    st.subheader(f"📍 Location: {city}")

    if prediction[0] == 1:
        st.success(f"🌧️ **Rain Expected Today!** (Probability: {rain_prob:.2f}%)")
    else:
        st.info(f"☀️ **No Rain Today.** (Rain Probability: {rain_prob:.2f}%)")

    st.markdown("---")
    st.subheader("🦟 Mosquito Outbreak Prediction")
    st.markdown(f"<h4 style='color:{risk_color}'>Outbreak Risk: {outbreak_risk}</h4>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Developed by Dharshini K Caroline A Hajira M Sahana JB Powered by Streamlit, Scikit-learn & Joblib")

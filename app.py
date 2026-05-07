import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("House Price Prediction")

# Inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
floors = st.number_input("Floors")
yearbuilt = st.number_input("Year Built")

location = st.selectbox(
    "Location",
    ["Downtown", "Suburban"]
)

condition = st.selectbox(
    "Condition",
    ["Excellent", "Good", "Fair"]
)

garage = st.selectbox(
    "Garage",
    ["Yes", "No"]
)

# Manual encoding
location = 0 if location == "Downtown" else 1

condition_map = {
    "Excellent": 0,
    "Good": 1,
    "Fair": 2
}

condition = condition_map[condition]

garage = 1 if garage == "Yes" else 0

# Prediction
if st.button("Predict Price"):

    features = np.array([[1, area, bedrooms, bathrooms,
                          floors, yearbuilt,
                          location, condition, garage]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: {prediction[0]}")
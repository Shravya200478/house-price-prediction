import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price.")

# User Inputs
area = st.number_input(
    "Area (in sq ft)",
    min_value=0.0,
    step=100.0
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=0,
    step=1
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=0,
    step=1
)

floors = st.number_input(
    "Number of Floors",
    min_value=0,
    step=1
)

yearbuilt = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2100,
    step=1
)

# Dropdowns
location = st.selectbox(
    "Location",
    ["Downtown", "Suburban"]
)

condition = st.selectbox(
    "Condition",
    ["Excellent", "Good", "Fair"]
)

garage = st.selectbox(
    "Garage Availability",
    ["Yes", "No"]
)

# Encoding categorical data
location = 0 if location == "Downtown" else 1

condition_map = {
    "Excellent": 0,
    "Good": 1,
    "Fair": 2
}

condition = condition_map[condition]

garage = 1 if garage == "Yes" else 0

# Prediction Button
if st.button("Predict Price"):

    # Prepare features
    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        floors,
        yearbuilt,
        location,
        condition,
        garage
    ]])

    # Predict
    prediction = model.predict(features)

    # Display Result
    st.success(
        f"🏡 Predicted House Price: ₹ {prediction[0]:,.2f}"
    )

# Footer
st.markdown("---")
st.markdown("Built using Streamlit and Machine Learning")

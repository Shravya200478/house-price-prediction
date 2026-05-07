import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction App")
st.write("Enter house details below to predict the price.")

# User Inputs
area = st.number_input(
    "Area (sq ft)",
    min_value=0.0,
    step=100.0
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    step=1
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=0,
    step=1
)

floors = st.number_input(
    "Floors",
    min_value=0,
    step=1
)

yearbuilt = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2100,
    step=1
)

# Dropdown Inputs
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

# Encoding categorical values
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

    # Feature array
    features = np.array([[
        1,
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

    # Show result
    st.success(
        f"🏡 Predicted House Price: ₹ {prediction[0]:,.2f}"
    )

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Machine Learning")

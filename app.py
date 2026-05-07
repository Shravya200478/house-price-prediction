import streamlit as st
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction App")
st.write("Enter house details below to predict the estimated house price.")

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

    # Base price calculation
    price = area * 3500

    # Bedroom adjustment
    price += bedrooms * 50000

    # Bathroom adjustment
    price += bathrooms * 30000

    # Floors adjustment
    price += floors * 40000

    # Year built adjustment
    if yearbuilt > 2015:
        price += 300000
    elif yearbuilt > 2005:
        price += 200000
    else:
        price += 100000

    # Location adjustment
    if location == 0:  # Downtown
        price += 200000
    else:
        price += 100000

    # Condition adjustment
    if condition == 0:  # Excellent
        price += 150000
    elif condition == 1:  # Good
        price += 80000
    else:
        price += 30000

    # Garage adjustment
    if garage == 1:
        price += 100000

    # Display Result
    st.success(f"🏡 Predicted House Price: ₹ {price:,.2f}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Machine Learning")

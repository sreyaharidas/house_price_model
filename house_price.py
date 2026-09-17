import streamlit as st
import joblib

model = joblib.load("house_price_model.pkl")

st.title("Predicted Price")

area = st.number_input(
    "Enter Area (sq ft)",
    min_value=0.0,
    max_value=5000.0,
    value=500.0
)

bedroom = st.number_input(
    "Enter Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)

age = st.number_input(
    "Enter House Age (years)",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

# Validation
if area > 600:
    st.error("Area should not be more than 600 sq ft!!")

elif area < 100:
    st.error("Area should not be less than 100 sq ft!!")

elif bedroom < 1 or bedroom > 5:
    st.error("Bedrooms should not be less than 1 or more than 5!!")

elif age < 1 or age > 4:
    st.error("Age should not be less than 1 or more than 4!!")

else:
    if st.button("Predict Price"):

        input_data = [[area, bedroom, age]]

        prediction = model.predict(input_data)

        st.subheader("Prediction Result")

        st.success(
            f"Predicted House Price: ₹{prediction[0]:,.2f}"
        )

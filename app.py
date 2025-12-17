# app.py
import streamlit as st
import pickle
import numpy as np

# Load the .pkl model
with open("https://drive.google.com/file/d/1UQLNxb3mv-UPk0RD0XOOP5xBuR3tD7mR/view?usp=sharing", "rb") as f:
    model = pickle.load(f)

st.title("Prediction App")

st.write("Enter input values for prediction:")

# Example: if your model expects 3 features
# Adjust this according to your dataset features
feature1 = st.number_input("age")
feature2 = st.number_input("Gender_encoded")
feature3 = st.number_input("bmi")
feature4 = st.number_input("smoker_encoded")

# Collect input into array
input_data = np.array([[feature1,feature2,feature3,feature4]])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted value: {prediction[0]}")

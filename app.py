import streamlit as st
import pickle
import numpy as np

# Load the model
with open('medical_insurance.pkl', 'rb') as file:  # Replace with your .pkl filename
    model = pickle.load(file)

st.title("Medical Insurance Charges Prediction")
st.write("Enter the patient details below:")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
smoker = st.selectbox("Smoker", ["yes", "no"])

# Preprocessing categorical inputs
sex_value = 1 if sex == "male" else 0
smoker_value = 1 if smoker == "yes" else 0

# Combine all inputs
input_features = np.array([[age, sex_value, bmi, smoker_value]])

# Prediction
if st.button("Predict Charges"):
    prediction = model.predict(input_features)
    st.success(f"Estimated Insurance Charges: ${prediction[0]:.2f}")

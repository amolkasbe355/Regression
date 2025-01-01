#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("RandomForestRegressor.pkl", "rb") as file:
    model = pickle.load(file)

# Title and description
st.title("Insurance Expenses Prediction")
st.write("Enter the details below to predict insurance expenses:")

# User input fields on the main page
age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
sex = st.selectbox("Sex", options=["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=5, value=0, step=1)
smoker = st.selectbox("Smoker", options=["Yes", "No"])
region = st.selectbox("Region", options=["Northeast", "Northwest", "Southeast", "Southwest"])

# Map inputs to numerical values
sex = 0 if sex == "Male" else 1
smoker = 1 if smoker == "Yes" else 0
region_mapping = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region = region_mapping[region]

# Prediction button
if st.button("Predict"):
    # Prepare input data for prediction
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(input_data)[0]
    
    # Display the prediction
    st.write(f"### Predicted Insurance Expenses: {prediction:.2f}")


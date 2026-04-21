import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("Student_Performance_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Title
st.title("🎓 Student Performance Prediction System")
st.write("Enter student details below:")

# Inputs
gender = st.selectbox("Gender", ["male", "female"])
race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent_edu = st.selectbox(
    "Parental Level of Education",
    ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
)
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation", ["none", "completed"])

# Prediction
if st.button("Predict"):

    # Create empty dataframe
    input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

    # Gender
    if gender == "male":
        input_data['gender_male'] = 1

    # Lunch
    if lunch == "standard":
        input_data['lunch_standard'] = 1

    # Test Preparation (IMPORTANT FIX 🔥)
    if test_prep == "none":
        input_data['test preparation course_none'] = 1

    # Race Encoding
    if f"race/ethnicity_{race}" in columns:
        input_data[f"race/ethnicity_{race}"] = 1

    # Parent Education Encoding
    if f"parental level of education_{parent_edu}" in columns:
        input_data[f"parental level of education_{parent_edu}"] = 1

    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.success("✅ Student is likely to PASS")
    else:
        st.error("❌ Student may FAIL")
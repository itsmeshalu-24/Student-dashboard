import streamlit as st
import numpy as np
import pickle
import pandas as pd

st.set_page_config(page_title="AI Student Predictor", layout="centered")

st.title("AI Student Drop-off Predictor")
st.write("AI-powered dashboard to predict student drop-off and improve retention in edtech platforms.")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Inputs
sessions = st.slider("Sessions Attended", 0, 50)
time_spent = st.slider("Avg Time Spent", 0, 200)
last_active = st.slider("Last Active Days", 0, 30)
quiz = st.slider("Quiz Score", 0, 100)

# Prediction
if st.button("Predict"):
    data = np.array([[sessions, time_spent, last_active, quiz]])

    result = model.predict(data)
    prob = model.predict_proba(data)[0][1]

    st.subheader("Prediction Result")

    if result[0] == 1:
        st.success(f"Student likely to stay active ✅ ({prob:.2f} confidence)")
        st.write("Suggestion: Keep engagement consistent.")
    else:
        st.error(f"Student likely to drop off ⚠️ ({1-prob:.2f} confidence)")
        st.write("Suggestion: Send reminder or provide extra support.")

# Summary
st.subheader("Student Summary")
st.write(f"Sessions: {sessions}, Time Spent: {time_spent}, Last Active: {last_active} days, Score: {quiz}")

# Load dataset
df = pd.read_csv("students.csv")

# Charts
st.subheader("Engagement Trends")
st.line_chart(df[['sessions_attended', 'avg_time_spent']])

st.subheader("Drop-off Distribution")
st.bar_chart(df['is_active'].value_counts())

# Insights
st.subheader("Key Insights")
st.write("• Students with more sessions are less likely to drop off")
st.write("• High inactivity leads to drop-off")
st.write("• Better quiz scores improve retention")
import pandas as pd
import streamlit as st

st.title("Predicting Depression from Mental Health Survey Data")

csv_url = "https://raw.githubusercontent.com/tayabba-19/Predicting-Depression-from-Mental-Health-Survey-Data-using-Deep-Learning/refs/heads/main/mental_health_survey.csv"
df = pd.read_csv(csv_url)

st.success("Dataset loaded successfully!")
st.dataframe(df.head())
        

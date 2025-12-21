import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Depression Prediction", layout="wide")

st.title("Predicting Depression from Mental Health Survey Data")
st.subheader("Streamlit Web Application")

st.markdown("""
This application analyzes mental health survey data and predicts
depression risk based on user inputs.
""")

# ---------------- DATASET UPLOAD ----------------
st.header("Upload Mental Health Survey Dataset (CSV)")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    # Chart
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
  if len(numeric_cols) > 0:
        selected_col = st.selectbox("Select column for visualization", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col], bins=20)
        ax.set_title(f"Distribution of {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")

        st.pyplot(fig)

# ---------------- PREDICTION SECTION ----------------
st.header("Depression Prediction")

stress = st.slider("Stress Level", 0, 10, 5)
anxiety = st.slider("Anxiety Level", 0, 10, 5)
sleep = st.slider("Sleep Problems", 0, 10, 5)

score = stress + anxiety + sleep

if st.button("Predict"):
    if score >= 18:
st.error("Prediction Result: High Risk of Depression")
    elif score >= 10:
        st.warning("Prediction Result: Moderate Risk")
    else:
        st.success("Prediction Result: Low Risk of Depression")

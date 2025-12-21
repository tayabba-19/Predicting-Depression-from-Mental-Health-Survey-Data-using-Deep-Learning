import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Depression Prediction App", layout="wide")

st.title("Predicting Depression from Mental Health Survey Data")
st.subheader("Streamlit App with Auto-loaded Dataset")

st.markdown("""
This web app loads a mental health survey dataset from GitHub,
visualizes key trends, and predicts depression risk automatically.
""")

# ---------------- Auto-load CSV from GitHub ----------------
csv_url = "https://raw.githubusercontent.com/tayabba-19/Predicting-Depression-from-Mental-Health-Survey-Data-using-Deep-Learning/main/sample_dataset.csv"

try:
    df = pd.read_csv(csv_url)
    st.success("Dataset loaded successfully from GitHub!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Summary Statistics")
    st.write(df.describe())

    # ---------------- Visualization ----------------
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    if len(numeric_cols) > 0:
        col = st.selectbox("Select column to visualize", numeric_cols)
         fig, ax = plt.subplots()
        sns.histplot(df[col], bins=20, kde=True)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    # ---------------- Depression Prediction ----------------
    st.header("Depression Prediction (Demo Model)")
    st.markdown("Adjust the sliders to simulate survey input:")

    stress = st.slider("Stress Level (0-10)", 0, 10, 5)
    anxiety = st.slider("Anxiety Level (0-10)", 0, 10, 5)
    sleep = st.slider("Sleep Problems (0-10)", 0, 10, 5)

    score = stress + anxiety + sleep

    if st.button("Predict"):
        if score >= 18:
            st.error("Prediction: High Risk of Depression")
        elif score >= 10:
            st.warning("Prediction: Moderate Risk")
        else:
            st.success("Prediction: Low Risk")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
        

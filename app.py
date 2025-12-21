import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Depression Prediction App', layout="wide")

st.title("Predicting Depression from Mental Health Survey Data")
st.subheader("Streamlit Cloud Ready App")

st.markdown("""
This web app allows you to upload mental health survey data (CSV),
visualize key trends, and get a simple depression prediction based on survey scores.
""")

# ---------------- DATASET UPLOAD ----------------
st.header("Upload Mental Health Survey Dataset (CSV)")
uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    #  ---------------- Visualization ----------------
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
  if len(numeric_cols) > 0:
    col = st.selectbox("Select column for visualization", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col], bins=20, kde=True)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig) 
        

# ---------------- Depression Prediction -----------------------
st.header("Depression Prediction  (Demo Model)")
st.markdown("Adjust the sliders to simulate survey input:")

stress = st.slider("Stress Level (0-10)", 0, 10, 5)
anxiety = st.slider("Anxiety Level (0-10)", 0, 10, 5)
sleep = st.slider("Sleep Problems (0-10)", 0, 10, 5)

score = stress + anxiety + sleep

if st.button("Predict"):
    if score >= 18:
st.error("Prediction Result: High Risk of Depression")
    elif score >= 10:
        st.warning("Prediction Result: Moderate Risk")
    else:
        st.success("Prediction Result: Low Risk of Depression")
else:
     st.info("Please upload a CSV dataset to begin analysis.")
        

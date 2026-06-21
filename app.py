from google.colab import files
uploaded = files.upload()
# %%writefile app.py
# %%writefile requirements.txt
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Local Food Wastage Management System",
    layout="wide"
)

st.title("🍲 Local Food Wastage Management System")

providers = pd.read_csv("providers_data.csv")

st.subheader("Providers Data")

st.dataframe(providers)

st.success("Application Loaded Successfully")

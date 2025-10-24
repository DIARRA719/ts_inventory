import streamlit as st
import pandas as pd
from utils.data_loader import load_sample_data, load_uploaded_data

st.set_page_config(page_title="Inventory Forecasting Dashboard", layout="wide")

st.title("📦 Inventory Forecasting Dashboard")

# Sidebar info
st.sidebar.header("ℹ️ Project Information")
st.sidebar.write("""
**App Name:** Inventory Forecasting AI  
**Model:** Prophet  
**Author:** Karen Bello  
**Goal:** Forecast future inventory levels using historical data.
""")

# File uploader
st.sidebar.header("📁 Upload Inventory Data")
use_sample = st.sidebar.checkbox("Use sample data")
uploaded_file = st.sidebar.file_uploader("Upload CSV or XLSX (Date, ClosingStock)", type=["csv", "xlsx"])

if use_sample:
    df = load_sample_data()
    st.success("✅ Using sample inventory dataset.")
elif uploaded_file:
    df = load_uploaded_data(uploaded_file)
    st.success("✅ Data uploaded successfully.")
else:
    st.info("Please upload your file or select sample data to continue.")
    st.stop()

st.subheader("📊 Historical Inventory Data")
st.line_chart(df.set_index("Date")["ClosingStock"], use_container_width=True)

st.session_state["data"] = df

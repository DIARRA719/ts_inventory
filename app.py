import streamlit as st

st.set_page_config(page_title="AI Inventory Forecasting", layout="wide")

st.sidebar.title("📂 Navigation")
st.sidebar.info("Use the pages below to explore the forecasting workflow:")
st.sidebar.page_link("pages/1_Home.py", label="🏠 Home")
st.sidebar.page_link("pages/2_Forecast.py", label="🔮 Forecast")
st.sidebar.page_link("pages/3_Dashboard.py", label="📊 Dashboard")

st.markdown("""
# 🤖 Inventory Forecasting AI
Welcome to the Inventory Forecasting App built with **Prophet**.  
This app predicts future inventory levels and provides insights on historical trends.
""")

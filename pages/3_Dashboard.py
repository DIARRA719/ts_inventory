import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("📊 Inventory Forecasting Dashboard")

if "data" not in st.session_state:
    st.warning("⚠️ Load data first from the Home page.")
    st.stop()

if "forecast" not in st.session_state:
    st.warning("⚠️ Run a forecast first from the Forecast page.")
    st.stop()

df = st.session_state["data"]
forecast = st.session_state["forecast"]

# Merge actual and forecast data
merged = pd.concat([df.set_index("Date"), forecast.set_index("ds")[["yhat"]]], axis=1)
merged.rename(columns={"ClosingStock": "Actual", "yhat": "Forecast"}, inplace=True)

st.subheader("📈 Actual vs Forecasted Inventory")
fig = px.line(merged, x=merged.index, y=["Actual", "Forecast"],
              labels={"value": "Inventory Level", "variable": "Legend"},
              color_discrete_sequence=["#041F3D", "#F4D35E"])
st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 Summary Statistics")
st.dataframe(merged.describe())

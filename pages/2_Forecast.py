import streamlit as st
import pandas as pd
from utils.forecasting_pipeline import run_prophet_forecast
from utils.visualization import plot_prophet_forecast, plot_forecast_table

st.set_page_config(page_title="Forecast", layout="wide")
st.title("🔮 Forecasting")

# Retrieve data
if "data" not in st.session_state:
    st.warning("⚠️ Please upload or load data from the Home page first.")
    st.stop()

df = st.session_state["data"]

# Forecast horizon selection
periods = st.slider("Select forecast period (days)", 30, 365, 180, 30)

# Run Prophet Forecast
st.info("Running Prophet model...")
forecast, model = run_prophet_forecast(df, periods)
st.success("✅ Prophet model completed successfully.")

# Display forecast visualization
st.subheader("📈 Prophet Forecast (Next {} Days Ahead)".format(periods))
fig = plot_prophet_forecast(model, forecast)
st.plotly_chart(fig, use_container_width=True)

# Display forecast table
st.subheader("📋 Forecast Table")
forecast_table = plot_forecast_table(forecast)
st.dataframe(forecast_table.head(15))

# Download forecast
csv = forecast_table.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Forecast CSV", csv, "prophet_forecast.csv", "text/csv")

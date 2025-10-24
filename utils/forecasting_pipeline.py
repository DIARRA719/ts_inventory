from prophet import Prophet
import pandas as pd
import streamlit as st

def run_prophet_forecast(df, periods):
    df_prophet = df.rename(columns={"Date": "ds", "ClosingStock": "y"})
    model = Prophet(
        seasonality_mode="additive",
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=periods, freq='D')
    forecast = model.predict(future)

    st.session_state["forecast"] = forecast
    return forecast, model

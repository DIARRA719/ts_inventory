import plotly.graph_objects as go
import pandas as pd

def plot_prophet_forecast(model, forecast):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=forecast["ds"], y=forecast["yhat"],
        mode="lines", name="Forecast", line=dict(color="#F4D35E", width=2)
    ))
    fig.add_trace(go.Scatter(
        x=forecast["ds"], y=forecast["yhat_lower"],
        mode="lines", line=dict(width=0), showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=forecast["ds"], y=forecast["yhat_upper"],
        mode="lines", fill="tonexty", name="Confidence Interval",
        fillcolor="rgba(244,211,94,0.2)", line=dict(width=0)
    ))
    fig.update_layout(
        template="plotly_white",
        title="Prophet Forecast — Predicted Inventory with Confidence Interval",
        xaxis_title="Date", yaxis_title="Predicted Closing Stock",
        title_font=dict(size=16)
    )
    return fig

def plot_forecast_table(forecast):
    forecast_table = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].rename(
        columns={"ds": "Date", "yhat": "Forecast", "yhat_lower": "Lower_CI", "yhat_upper": "Upper_CI"}
    )
    return forecast_table

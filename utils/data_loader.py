import pandas as pd

def load_sample_data():
    return pd.read_excel("data/sample_inventory.xlsx")

def load_uploaded_data(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    return df

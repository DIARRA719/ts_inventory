📦**AI Inventory Forecasting App**

**By Karen Delea**

A modern AI-powered Streamlit web application that forecasts inventory levels using Prophet, providing interactive visualizations, insights, and downloadable forecasts.

The app allows users to upload their own data or use a sample inventory dataset, visualize trends, generate future predictions, and explore a summary dashboard — all in a clean, professional interface.

🌟 **Key Features**

✅ Upload or use built-in sample inventory data (.xlsx supported)
✅ Generate Prophet forecasts for up to 365 days
✅ Visualize actuals vs. predicted values with confidence intervals
✅ Download forecasted results as CSV
✅ Interactive dashboard view with summary metrics
✅ Modern UI with your palette:

🟡 #F4D35E — Highlight color

🟢 #DDEE99 — Confidence intervals

🔵 #041F3D — Main theme color

**TS_INVENTORY/**
│
├── app.py                          # Main entry point (navigation)
├── pages/
│   ├── 1_Home.py                   # Upload data or use sample
│   ├── 2_Forecast.py               # Prophet forecasting
│   └── 3_Dashboard.py              # Results dashboard
│
├── utils/
│   ├── data_loader.py              # Load CSV/XLSX data
│   ├── forecasting_pipeline.py     # Prophet model logic
│   └── visualization.py            # Plotly charts
│
├── data/
│   └── sample_inventory.xlsx       # Example dataset
│
├── requirements.txt                # Python dependencies
└── .gitignore                      # Ignore models/data caches

📊 **How to Use**

1️⃣ Go to 🏠 Home Page — upload your inventory dataset or use the provided sample.
2️⃣ Switch to 🔮 Forecast Page — select forecast horizon (days) and run Prophet.
3️⃣ Explore 📊 Dashboard Page — compare actual vs forecasted inventory and view stats.
4️⃣ Download your forecast results for reporting.

🧮 **Model Information**
Model Used: Prophet

Captures trend, seasonality, and holiday effects

Robust to missing data and outliers

Outputs upper and lower confidence intervals

Example Metrics (from model testing):

**Model Information**
| Metric | Value |
| ------ | ----- |
| MAE    | 16.12 |
| RMSE   | 20.21 |
| MAPE   | 1.69% |
| R²     | 0.48  |

**🧠 Tech Stack**
| Category          | Tool                       |
| ----------------- | -------------------------- |
| Language          | Python 3                   |
| Web Framework     | Streamlit                  |
| Forecasting Model | Prophet                    |
| Visualization     | Plotly                     |
| Data Handling     | Pandas, NumPy              |
| File Support      | Excel (.xlsx via openpyxl) |


👩‍💻 About the Author

**Karen Delea**
Data Scientist | Data Analyst | Supply Chain & Business Analytics

🎓 Postgraduate in Data Science & Business Analytics — University of Texas at Austin (McCombs)

💼 Specialized in Power BI, Python, SQL, and AI Forecasting

🌐 Portfolio Website  https://sites.google.com/view/karenbello-portfolio/home?authuser=0

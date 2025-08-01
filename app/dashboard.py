import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import joblib
from src.forecasting import forecast_births
from src.utils import load_data

st.set_page_config(
    page_title='Scotland Birth Forecast',
    page_icon="📊",
    layout="wide"
)

# --- Sidebar Navigation ---
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("Use the sidebar to explore different tools in the app.")

# --- Main Title ---
st.title("📊 Birth Rate Forecasting in Scotland")

try:
    # --- User Input ---
    df = load_data()
    area = st.selectbox("🏥 Select NHS Board Area", df['NHS Board area'].unique())
    months = st.slider("🕒 Number of Months to Forecast", min_value=1, max_value=12, value=3)

    # --- Forecast Button ---
    if st.button("🔮 Forecast Births"):
        with st.spinner("Forecasting..."):
            forecast_df = forecast_births(area, months)
            st.success("Forecast completed!")
            
            st.subheader("📈 Forecasted Birth Rate")
            st.line_chart(forecast_df.set_index('date')['prediction'])

            st.subheader("📋 Forecast Data")
            st.dataframe(forecast_df, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 | Real-time Birth Rate Forecasting Dashboard for Scotland")
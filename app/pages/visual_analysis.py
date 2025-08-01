import streamlit as st
import pandas as pd
from src.utils import load_data
from src.visualizations import plot_forecast, plot_historical_trend, plot_heatmap_by_month
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visual Analysis", page_icon="🧪", layout="wide")
st.title("🧪 Visual Analysis of Birth Rates")

df = load_data()
area = st.selectbox("Select NHS Board Area", df['NHS Board area'].unique())

# Historical Trend
st.subheader("📉 Historical Trend")
fig1 = plt.figure()
plot_historical_trend(df, area)
st.pyplot(fig1)

# Heatmap
st.subheader("🌡️ Birth Heatmap by Month and Year")
fig2 = plt.figure()
plot_heatmap_by_month(df)
st.pyplot(fig2)

st.markdown("---")
st.caption("© 2025 | Scotland Birth Forecasting Project")

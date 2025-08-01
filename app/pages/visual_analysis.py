import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import load_data

st.set_page_config(page_title="Visual Analysis", page_icon="🧪", layout="wide")
st.title("🧪 Visual Analysis of Birth Rates")

try:
    # Load and prepare data
    df = load_data()
    area = st.selectbox("Select NHS Board Area", df['NHS Board area'].unique())

    # Filter data for selected area
    area_df = df[df['NHS Board area'] == area].copy()
    
    # Create date column
    area_df['Date'] = pd.to_datetime(area_df['Year'].astype(str) + '-' + 
                                   area_df['Month'].astype(str))
    area_df = area_df.sort_values('Date')

    # Historical Trend Plot
    st.subheader("📉 Historical Trend")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(area_df['Date'], area_df['Births occurring'], color='steelblue')
    ax1.set_title(f'Birth Rate Trend in {area}')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Number of Births')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

    # Heatmap
    st.subheader("🌡️ Birth Heatmap by Month and Year")
    
    # Create pivot table for heatmap
    pivot_data = df.pivot_table(
        values='Births occurring',
        index=pd.to_datetime(df['Year'].astype(str)).dt.year,
        columns=df['Month'],
        aggfunc='mean'
    )
    
    fig2, ax2 = plt.subplots(figsize=(12, 8))
    sns.heatmap(pivot_data, cmap='YlOrRd', annot=True, fmt='.0f', ax=ax2)
    ax2.set_title('Birth Rate Heatmap by Month and Year')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Year')
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.error("Error details:", str(e.__class__.__name__))

st.markdown("---")
st.caption("© 2025 | Scotland Birth Forecasting Project")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_historical_trend(df, area):
    """Plot historical birth rate trend for a specific NHS board area."""
    # Filter data for selected area
    area_df = df[df['NHS Board area'] == area].copy()
    
    # Create date column if not exists
    if 'Date' not in area_df.columns:
        area_df['Date'] = pd.to_datetime(area_df.apply(
            lambda x: f"{x['Year']}-{x['Month']}-01", axis=1
        ))
    
    # Handle different column names for births
    births_col = 'Births occurring' if 'Births occurring' in area_df.columns else 'Births'
    
    plt.figure(figsize=(12, 6))
    plt.plot(area_df['Date'], area_df[births_col], color='steelblue', linewidth=2)
    plt.title(f'Birth Rate Trend in {area}')
    plt.xlabel('Date')
    plt.ylabel('Number of Births')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

def plot_heatmap_by_month(df):
    """Create a heatmap showing birth rates by month and year."""
    df = df.copy()
    
    # Handle different column names for births
    births_col = 'Births occurring' if 'Births occurring' in df.columns else 'Births'
    
    # Create date column if needed
    if 'Date' not in df.columns:
        df['Date'] = pd.to_datetime(df.apply(
            lambda x: f"{x['Year']}-{x['Month']}-01", axis=1
        ))
    
    # Create pivot table for heatmap
    pivot_data = df.pivot_table(
        values=births_col,
        index=df['Date'].dt.year,
        columns=df['Month'],
        aggfunc='mean'
    )
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_data, cmap='YlOrRd', annot=True, fmt='.0f')
    plt.title('Birth Rate Heatmap by Month and Year')
    plt.xlabel('Month')
    plt.ylabel('Year')
    plt.tight_layout()

def plot_forecast(historical_data, forecast_data, area):
    """Plot historical data with forecast overlay."""
    plt.figure(figsize=(12, 6))
    
    # Plot historical data
    births_col = 'Births occurring' if 'Births occurring' in historical_data.columns else 'Births'
    plt.plot(historical_data['Date'], historical_data[births_col], 
            label='Historical', color='steelblue')
    
    # Plot forecast
    plt.plot(forecast_data['date'], forecast_data['prediction'], 
            label='Forecast', color='red', linestyle='--')
    
    plt.title(f'Birth Rate Forecast for {area}')
    plt.xlabel('Date')
    plt.ylabel('Number of Births')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
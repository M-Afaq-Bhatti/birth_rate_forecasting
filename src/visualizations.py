import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_forecast(df: pd.DataFrame, title: str = "Birth Forecast"):
    """
    Plots the forecasted birth rates using matplotlib.
    Expects a DataFrame with 'date' and 'prediction' columns.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['prediction'], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Predicted Births")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_historical_trend(df: pd.DataFrame, area: str):
    """
    Plots the historical birth trends for a given NHS Board area.
    """
    area_df = df[df['NHS Board area'] == area]
    plt.figure(figsize=(10, 4))
    plt.plot(area_df['date'], area_df['Births occurring'], color='steelblue')
    plt.title(f"Historical Births in {area}")
    plt.xlabel("Date")
    plt.ylabel("Births")
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def plot_heatmap_by_month(df: pd.DataFrame):
    """
    Plots a heatmap of average births by month and year.
    """
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    pivot = df.pivot_table(values='Births occurring', index='month', columns='year', aggfunc='mean')

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=True, fmt=".0f")
    plt.title("Average Births by Month and Year")
    plt.xlabel("Year")
    plt.ylabel("Month")
    plt.tight_layout()
    plt.show()

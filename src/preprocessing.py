import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, training=True, scaler=None):
    df = df.copy()

    # Rename column if needed and ensure it's a Series
    if 'Births occurring' in df.columns:
        df['Births'] = df['Births occurring'].astype(float)
        df.drop('Births occurring', axis=1, inplace=True)

    if 'Births' not in df.columns:
        raise ValueError("'Births' column is missing in the dataframe.")

    if 'Month' not in df.columns or 'Year' not in df.columns:
        raise ValueError("Both 'Month' and 'Year' columns must be present in the dataframe.")

    # Fill missing values in 'Births'
    df['Births'] = df['Births'].ffill().bfill()

    # Convert date with explicit format
    df['Date'] = pd.to_datetime(df.apply(
        lambda x: f"{x['Year']}-{x['Month']}-01", axis=1
    ), format='%Y-%B-%d', errors='coerce')
    
    df = df.sort_values('Date')

    # Create lag features
    df['Lag_1'] = df['Births'].astype(float).shift(1)
    df['Lag_2'] = df['Births'].astype(float).shift(2)
    df.dropna(subset=['Lag_1', 'Lag_2'], inplace=True)

    df['Month_Num'] = df['Date'].dt.month
    df['Year_Num'] = df['Date'].dt.year

    features = ['Lag_1', 'Lag_2', 'Month_Num', 'Year_Num']
    X = df[features]
    y = df['Births']

    # Scaling
    if training:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        if scaler is None:
            raise ValueError("Scaler must be provided when training=False")
        X_scaled = scaler.transform(X)

    # Return X_scaled, y, features DataFrame, and scaler
    return X_scaled, y, df[features + ['Births', 'Date', 'Month', 'Year']], scaler
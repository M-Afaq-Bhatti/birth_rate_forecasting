import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, training=True):
    df = df.copy()
    
    # Rename for consistency
    if 'Births' not in df.columns and 'Births occurring' in df.columns:
        df['Births'] = df['Births occurring']
    
    if 'Births' not in df.columns:
        raise ValueError("'Births' column is missing in the dataframe.")
    
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'] + '-01', errors='coerce')
    df = df.sort_values('Date')

    # Fill missing births
    df['Births'] = df['Births'].ffill().bfill()


    # Lag features
    df['Lag_1'] = df['Births'].shift(1)
    df['Lag_2'] = df['Births'].shift(2)

    # Time features
    df['Month_num'] = df['Date'].dt.month
    df['Month_sin'] = np.sin(2 * np.pi * df['Month_num'] / 12)
    df['Month_cos'] = np.cos(2 * np.pi * df['Month_num'] / 12)

    # Drop NA due to lags
    df.dropna(inplace=True)

    # One-hot encode area
    df = pd.get_dummies(df, columns=['NHS Board area'])

    y = df['Births']
    X = df.drop(columns=['Year', 'Month', 'Births', 'Date', 'Month_num'])

    if training:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Save scaler and feature names
        joblib.dump(scaler, 'scaler.pkl')
        joblib.dump(X.columns.tolist(), 'features.pkl')

        return X_scaled, y, df

    else:
        # Load fitted scaler and feature names
        scaler = joblib.load('scaler.pkl')
        expected_features = joblib.load('features.pkl')

        # Add missing columns with zeros
        for col in expected_features:
            if col not in X.columns:
                X[col] = 0
        
        # Drop extra columns not seen in training
        X = X[expected_features]

        X_scaled = scaler.transform(X)
        return X_scaled, y, df, scaler

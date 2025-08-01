import pandas as pd
import joblib
from src.data_ingestion import load_latest_data
from src.preprocessing import preprocess_data

def forecast_births(area, months):
    # Load model and scaler
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')

    # Step 1: Load full dataset
    df = load_latest_data()

    # Step 2: Filter only selected area
    area_df = df[df['NHS Board area'] == area].copy()

    print("DEBUG: area_df columns:", area_df.columns)
    print("DEBUG: area_df sample:\n", area_df.head())

    
    # Step 3: Preprocess data to get full feature matrix (same as in training)
    X_scaled, y, features_df = preprocess_data(area_df, training=False)

    # Step 4: Start with the last row of scaled features
    last_row_scaled = X_scaled[-1].reshape(1, -1)

    # Step 5: Get last known year and month (from features_df, NOT from scaler!)
    last_entry = features_df.iloc[-1]
    last_year = last_entry['Year']
    last_month = last_entry['Month']

    # Step 6: Generate predictions
    predictions = []
    dates = []

    for _ in range(months):
        # Predict next birth count
        pred = model.predict(last_row_scaled)[0]
        predictions.append(pred)

        # Calculate next date
        last_date = pd.to_datetime(f"{last_year}-{last_month}")
        next_date = last_date + pd.DateOffset(months=1)
        next_year = next_date.year
        next_month = next_date.month

        dates.append(next_date)

        # Simulate new input row
        new_row = {
            'Year': next_year,
            'Month': next_month,
            'NHS Board area': area,
            'Births': pred
        }

        # Append new row to the data
        area_df = pd.concat([area_df, pd.DataFrame([new_row])], ignore_index=True)

        # Reprocess features and update the last scaled row
        X_scaled, _, features_df = preprocess_data(area_df)
        last_row_scaled = X_scaled[-1].reshape(1, -1)

        last_year = next_year
        last_month = next_month

    # Return result
    forecast_df = pd.DataFrame({
        'Date': dates,
        'Predicted_Births': predictions
    })

    return forecast_df

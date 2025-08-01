import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import joblib
import pandas as pd
from src.data_ingestion import load_latest_data
from src.preprocessing import preprocess_data
from src.model import train_model

# Step 1: Load latest data
df = load_latest_data()

# Step 2: Preprocess data
X_scaled, y, df_features, scaler = preprocess_data(df, training=True)

# Step 3: Extract feature names before scaling
feature_names = df_features.drop(columns=['Births']).columns.tolist()

# Step 4: Train model
model, mae, r2 = train_model(X_scaled, y)

# Step 5: Save outputs
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(feature_names, 'feature_names.pkl')

# Step 6: Print metrics
print(f"MAE: {mae}")
print(f"R2: {r2}")

import sys
import os
import pandas as pd
import joblib

# Add root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_ingestion import load_latest_data
from src.preprocessing import preprocess_data
from src.model import train_model  # Make sure this version returns model, mae, r2

# Step 1: Load data
df = load_latest_data()

# Step 2: Preprocess data
# Step 2: Preprocess data
X_scaled, y, df_features, scaler = preprocess_data(df, training=True)

# Step 3: Save feature names BEFORE scaling
feature_names = df_features.drop(columns=['Births']).columns.tolist()
joblib.dump(feature_names, 'feature_names.pkl')

# Step 4: Train model
model, mae, r2 = train_model(X_scaled, y)

# Step 5: Save model and scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

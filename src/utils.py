import pandas as pd
from src.config import data_path, sheet_name

def load_data():
    try:
        return pd.read_excel(data_path, sheet_name=sheet_name, skiprows=4)
    except FileNotFoundError:
        raise Exception(f"❌ File not found at {data_path}.")
    except Exception as e:
        raise Exception(f"❌ Failed to load data: {e}")

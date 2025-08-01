import pandas as pd
from src.config import data_path, sheet_name

def load_latest_data(path=data_path, sheet=sheet_name):
    try:
        df = pd.read_excel(path, sheet_name=sheet, skiprows=4)
        df = df.dropna(how='all')  # Remove fully empty rows
        df.columns = [str(col).strip() for col in df.columns]

        if 'Year' not in df.columns or 'Month' not in df.columns or 'Births occurring' not in df.columns:
            raise ValueError("Required columns missing from the data.")

        df = df[df['Year'].apply(lambda x: str(x).isdigit())]
        df['Year'] = df['Year'].astype(int)

        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()

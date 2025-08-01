import pandas as pd
from datetime import datetime, timedelta
import os

# Path to your current data
DATA_PATH = 'D:/proj_1/birth_rate_forecasting/monthly-births-june-2025.xlsx'

def simulate_new_data():
    """
    Simulate a new row of birth data for the next month.
    """
    try:
        # Load existing data
        df = pd.read_excel(DATA_PATH, sheet_name='Table_3', skiprows=4)
    except Exception as e:
        print(f"❌ Failed to load existing data: {e}")
        return

    # Clean column names
    df.columns = [str(col).strip() for col in df.columns]
    df = df.dropna(subset=['Year', 'Month', 'Births occurring'])

    # Get latest date
    last_row = df.dropna(subset=['Year', 'Month']).iloc[-1]
    last_year = int(last_row['Year'])
    last_month_str = str(last_row['Month'])
    try:
        last_date = pd.to_datetime(f"{last_year} {last_month_str}")
    except:
        print("❌ Failed to parse last date.")
        return

    # Generate next month's date
    next_date = last_date + pd.DateOffset(months=1)
    next_year = next_date.year
    next_month = next_date.strftime('%B')

    # Simulate birth counts for each NHS Board
    areas = df['NHS Board area'].unique()
    new_rows = []
    for area in areas:
        simulated_births = int(df[df['NHS Board area'] == area]['Births occurring'].mean()) + int(pd.np.random.normal(0, 5))
        new_rows.append({
            'Year': next_year,
            'Month': next_month,
            'NHS Board area': area,
            'Births occurring': simulated_births
        })

    # Append new rows
    new_data = pd.DataFrame(new_rows)
    updated_df = pd.concat([df, new_data], ignore_index=True)

    # Save updated data
    with pd.ExcelWriter(DATA_PATH, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        updated_df.to_excel(writer, index=False, sheet_name='Table_3')

    print(f"✅ Data updated with new entries for {next_month} {next_year}.")

if __name__ == '__main__':
    simulate_new_data()

import pandas as pd

# Load the CSV file
df = pd.read_csv('data_raw/owid-co2-data.csv')

# Preview structure
print("Preview of the data:")
print(df.head())
print("\nList of columns:")
print(df.columns.tolist())

# List of European countries
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", 
    "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", 
    "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", 
    "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican"
]

# Filter for European countries
europe_df = df[df['country'].isin(european_countries)]

# Find the latest year in the dataset
latest_year = europe_df['year'].max()
print(f"\nLatest year in dataset: {latest_year}")

# Filter only the last 5 years
last_5_years = list(range(latest_year - 4, latest_year + 1))
recent_data = europe_df[europe_df['year'].isin(last_5_years)]

# Save the filtered data
recent_data.to_csv('data_final/european_co2_last5years.csv', index=False)

# Preview
print(f"\n✅ Cleaned data for years {last_5_years} saved to 'european_co2_last5years.csv'")
print("\nPreview of recent data:")
print(recent_data.head())

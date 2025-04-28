import pandas as pd

# Load the dataset, skipping the first few rows
df = pd.read_csv('data_raw/API_AG.LND.FRST.ZS_DS2_en_csv_v2_13350.csv', on_bad_lines='skip', skiprows=4)

# Drop any unwanted columns 
df = df.drop(columns=['Unnamed: 68'], errors='ignore')

# Check if the column names and rows are correct
print(df.head())

# List of European countries
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", 
    "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", 
    "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", 
    "Russian Federation", "San Marino", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkiye", "Ukraine", "United Kingdom", "Vatican"
]

# Filter for European countries
df_europe = df[df['Country Name'].isin(european_countries)]

# Filter for the last 5 years (2019-2023)
df_last_5_years = df_europe[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '2019', '2020', '2021', '2022', '2023']]

# Check the resulting DataFrame
print(df_last_5_years.head())

# Save the cleaned DataFrame to a CSV
df_last_5_years.to_csv('data_final/european_forest_data.csv', index=False)

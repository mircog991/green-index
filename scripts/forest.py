import pandas as pd

# Load the dataset, skipping the first few rows (already done)
df = pd.read_csv('/Users/user/Desktop/green-index/data/API_AG.LND.FRST.ZS_DS2_en_csv_v2_13350.csv', on_bad_lines='skip', skiprows=4)

# Drop any unwanted columns (e.g., 'Unnamed: 68')
df = df.drop(columns=['Unnamed: 68'], errors='ignore')

# Check if the column names and rows are correct
print(df.head())

# List of European country names or ISO codes (just an example, make sure to adjust this list)
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", 
    "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", 
    "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", 
    "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom"
]

# Filter for European countries
df_europe = df[df['Country Name'].isin(european_countries)]

# Filter for the last 5 years (2019-2023)
df_last_5_years = df_europe[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '2019', '2020', '2021', '2022', '2023']]

# Check the resulting DataFrame
print(df_last_5_years.head())

# Save the cleaned DataFrame to a CSV
#df_last_5_years.to_csv('/Users/user/Desktop/Project/final_european_forest_data.csv', index=False)

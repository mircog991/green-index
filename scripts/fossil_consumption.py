import pandas as pd

# Load CSV file, skipping metadata rows at the top
df = pd.read_csv("data_raw/Fossil_fuel_energy_consumption.csv", skiprows=4)

# List of European countries
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia",
    "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein",
    "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Romania", "Russian Federation", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
    "Sweden", "Switzerland", "Turkiye", "Ukraine", "United Kingdom", "Vatican City"
]

# Filter for European countries
df = df[df["Country Name"].isin(european_countries)]

# Keep only desired columns: metadata + 2019–2023
columns_to_keep = ["Country Name", "Country Code", "Indicator Name", "Indicator Code",
                   "2019", "2020", "2021", "2022", "2023"]
df = df[columns_to_keep]

# Drop rows where all values from 2019–2023 are NaN
df.dropna(subset=["2019", "2020", "2021", "2022", "2023"], how="all", inplace=True)

# Load coordinates
coords = pd.read_csv('data_final/european_country_coordinates.csv')

# Normalize column for merging
df['Entity'] = df["Country Name"].str.strip().str.lower()
coords['Entity'] = coords['Entity'].str.strip().str.lower()

# Merge latitude and longitude into the main data
df = pd.merge(df, coords, on='Entity', how='left')

# Drop the temporary 'Entity' column (optional)
df.drop(columns=['Entity'], inplace=True)

# Save to a new clean file
df.to_csv("data_final/fossil_consumption.csv", index=False)

print("Cleaned file saved as data_final/fossil_consumption.csv")


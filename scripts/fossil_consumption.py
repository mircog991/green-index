import pandas as pd

# Load CSV file, skipping metadata rows at the top
df = pd.read_csv("data_raw/Fossil_fuel_energy_consumption.csv", skiprows=4)

# List of European countries (ISO standard or custom set)
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia",
    "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein",
    "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
    "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"
]

# Filter for European countries
df = df[df["Country Name"].isin(european_countries)]

# Keep only columns we want: metadata + 2019–2023
columns_to_keep = ["Country Name", "Country Code", "Indicator Name", "Indicator Code",
                   "2019", "2020", "2021", "2022", "2023"]
df = df[columns_to_keep]

# Drop rows where all years from 2019-2023 are NaN
df.dropna(subset=["2019", "2020", "2021", "2022", "2023"], how="all", inplace=True)

# Save to a new clean file
df.to_csv("data_final/cleaned_europe_2019_2023.csv", index=False)

print("Cleaned file saved as cleaned_europe_2019_2023.csv")

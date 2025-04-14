import pandas as pd

# Load the CSV file
df = pd.read_csv('data_raw/estat_sdg_07_40_filtered_en.csv')

# Filter to keep only the last 5 years (2019–2023)
df_last_5_years = df[df['TIME_PERIOD'].isin([2019, 2020, 2021, 2022, 2023])]

# Rename columns
df_last_5_years = df_last_5_years.rename(columns={
    'Geopolitical entity (reporting)': 'country',
    'geo': 'iso_code',
    'TIME_PERIOD': 'year',
    'OBS_VALUE': 'value'
})

# Map ISO codes to country names
iso_to_country = {
    'AT': 'Austria', 'BE': 'Belgium', 'BG': 'Bulgaria', 'CY': 'Cyprus',
    'CZ': 'Czech Republic', 'DE': 'Germany', 'DK': 'Denmark', 'EE': 'Estonia',
    'ES': 'Spain', 'FI': 'Finland', 'FR': 'France', 'EL': 'Greece',
    'HR': 'Croatia', 'HU': 'Hungary', 'IE': 'Ireland', 'IT': 'Italy',
    'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 'MT': 'Malta',
    'NL': 'Netherlands', 'PL': 'Poland', 'PT': 'Portugal', 'RO': 'Romania',
    'SE': 'Sweden', 'SI': 'Slovenia', 'SK': 'Slovakia'
}

df_last_5_years['country'] = df_last_5_years['iso_code'].map(iso_to_country).fillna(df_last_5_years['country'])

# Final selection
df_final = df_last_5_years[['country', 'year', 'iso_code', 'value']]

# Save to CSV
df_final.to_csv('data_final/renewable_energy_consumption_estat_data.csv', index=False)

# Print preview
print("First few rows of the final DataFrame:")
print(df_final.head())

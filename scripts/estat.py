import pandas as pd

# Load the .tsv file into a DataFrame
df = pd.read_csv('/data/estat_sdg_07_11.tsv', sep='\t')

# Strip any leading or trailing whitespace from column names
df.columns = df.columns.str.strip()

# Split the 'freq,unit,geo\\TIME_PERIOD' column by commas into three parts
split_cols = df['freq,unit,geo\\TIME_PERIOD'].str.split(',', expand=True)

# Assign the split columns directly to the DataFrame
df[['freq', 'unit', 'geo']] = split_cols

# Drop the original combined column as it's no longer needed
df.drop('freq,unit,geo\\TIME_PERIOD', axis=1, inplace=True)

# Melt the DataFrame to have one column for years and one column for values
df_melted = df.melt(id_vars=['freq', 'unit', 'geo'], var_name='year', value_name='value')

# Filter to keep only the last 5 years (2019–2023)
df_last_5_years = df_melted[df_melted['year'].isin(['2019', '2020', '2021', '2022', '2023'])]

# Rename columns to match the final output
df_last_5_years = df_last_5_years.rename(columns={'freq': 'country', 'geo': 'iso_code'})

# Mapping of ISO codes to full country names (you need to customize this dictionary as needed)
iso_to_country = {
    'AT': 'Austria', 'BE': 'Belgium', 'BG': 'Bulgaria', 'CY': 'Cyprus',
    'CZ': 'Czech Republic', 'DE': 'Germany', 'DK': 'Denmark', 'EE': 'Estonia',
    'ES': 'Spain', 'FI': 'Finland', 'FR': 'France', 'GR': 'Greece',
    'HR': 'Croatia', 'HU': 'Hungary', 'IE': 'Ireland', 'IT': 'Italy',
    'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 'MT': 'Malta',
    'NL': 'Netherlands', 'PL': 'Poland', 'PT': 'Portugal', 'RO': 'Romania',
    'SE': 'Sweden', 'SI': 'Slovenia', 'SK': 'Slovakia'
    # Add more mappings as needed
}

# Replace ISO codes with full country names
df_last_5_years['country'] = df_last_5_years['iso_code'].map(iso_to_country)

# Select the desired columns: 'country', 'year', 'iso_code', 'value'
df_final = df_last_5_years[['country', 'year', 'iso_code', 'value']]

# Save the final DataFrame to a CSV file
#df_final.to_csv('/Users/user/Desktop/Project/final_estat_data.csv', index=False)

# Display the final DataFrame
print("First few rows of the final DataFrame with full country names:")
print(df_final.head())



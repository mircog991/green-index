import pandas as pd
import itertools

df = pd.read_csv('data_raw/modern-renewable-energy-consumption.csv')

df = df[df['Year'].between(2019, 2023)]

european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 
    'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 
    'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 
    'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 
    'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 
    'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 
    'Ukraine', 'United Kingdom', 'Vatican'
]


all_combinations = pd.DataFrame(list(itertools.product(european_countries, range(2019, 2024))),
                                columns=['Entity', 'Year'])

# Merge with your actual data
merged = pd.merge(all_combinations, df, on=['Entity', 'Year'], how='left')

# Fill NaNs in generation columns with 0
generation_columns = [
    'Other renewables (including geothermal and biomass) electricity generation - TWh',
    'Solar generation - TWh',
    'Wind generation - TWh',
    'Hydro generation - TWh'
]

merged[generation_columns] = merged[generation_columns].fillna(0)

# Fill Code column with empty string or 'N/A' if desired
merged['Code'] = merged['Code'].fillna('')


merged.to_csv('data_final/renewable-energy-generation.csv', index=False)


original_countries = df['Entity'].unique()
missing_countries = sorted(set(european_countries) - set(original_countries))
print("Missing countries in original data:")
print(missing_countries)
print(merged.head())
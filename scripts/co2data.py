import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv('/Users/user/Desktop/green-index/data/owid-co2-data.csv')

# Step 2: Preview structure
print("Preview of the data:")
print(df.head())
print("\nList of columns:")
print(df.columns.tolist())

# Step 3: List of European countries
european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
    'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary',
    'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro',
    'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
    'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
    'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican'
]

# Step 4: Filter for European countries
europe_df = df[df['country'].isin(european_countries)]

# Step 5: Find the latest year in the dataset
latest_year = europe_df['year'].max()
print(f"\nLatest year in dataset: {latest_year}")

# Step 6: Filter only the last 5 years
last_5_years = list(range(latest_year - 4, latest_year + 1))
recent_data = europe_df[europe_df['year'].isin(last_5_years)]

# Step 7: Save the filtered data
#recent_data.to_csv('/Users/user/Desktop/Project/european_co2_last5years.csv', index=False)

# Step 8: Preview
print(f"\n✅ Cleaned data for years {last_5_years} saved to 'european_co2_last5years.csv'")
print("\nPreview of recent data:")
print(recent_data.head())


import pandas as pd

country_coords = {
    'Albania': (41.1533, 20.1683),
    'Andorra': (42.5078, 1.5211),
    'Armenia': (40.0691, 45.0382),
    'Austria': (47.5162, 14.5501),
    'Azerbaijan': (40.1431, 47.5769),
    'Belarus': (53.7098, 27.9534),
    'Belgium': (50.5039, 4.4699),
    'Bosnia and Herzegovina': (43.9159, 17.6791),
    'Bulgaria': (42.7339, 25.4858),
    'Croatia': (45.1, 15.2),
    'Cyprus': (35.1264, 33.4299),
    'Czechia': (49.8175, 15.473),
    'Denmark': (56.2639, 9.5018),
    'Estonia': (58.5953, 25.0136),
    'Finland': (61.9241, 25.7482),
    'France': (46.6034, 1.8883),
    'Georgia': (42.3154, 43.3569),
    'Germany': (51.1657, 10.4515),
    'Greece': (39.0742, 21.8243),
    'Hungary': (47.1625, 19.5033),
    'Iceland': (64.9631, -19.0208),
    'Ireland': (53.1424, -7.6921),
    'Italy': (41.8719, 12.5674),
    'Kazakhstan': (48.0196, 66.9237),
    'Kosovo': (42.6026, 20.9020),
    'Latvia': (56.8796, 24.6032),
    'Liechtenstein': (47.166, 9.5554),
    'Lithuania': (55.1694, 23.8813),
    'Luxembourg': (49.8153, 6.1296),
    'Malta': (35.9375, 14.3754),
    'Moldova': (47.4116, 28.3699),
    'Monaco': (43.7384, 7.4246),
    'Montenegro': (42.7087, 19.3744),
    'Netherlands': (52.1326, 5.2913),
    'North Macedonia': (41.9981, 21.4254),
    'Norway': (60.472, 8.4689),
    'Poland': (51.9194, 19.1451),
    'Portugal': (39.3999, -8.2245),
    'Romania': (45.9432, 24.9668),
    'Russia': (61.524, 105.3188),
    'San Marino': (43.9333, 12.45),
    'Serbia': (44.0165, 21.0059),
    'Slovakia': (48.669, 19.699),
    'Slovenia': (46.1512, 14.9955),
    'Spain': (40.4637, -3.7492),
    'Sweden': (60.1282, 18.6435),
    'Switzerland': (46.8182, 8.2275),
    'Turkey': (38.9637, 35.2433),
    'Ukraine': (48.3794, 31.1656),
    'United Kingdom': (55.3781, -3.436),
    'Vatican': (41.9029, 12.4534)
}

# Build DataFrame with Latitude and Longitude already split
coords_df = pd.DataFrame([
    {'Entity': country, 'Latitude': lat, 'Longitude': lon}
    for country, (lat, lon) in country_coords.items()
])

# Save to CSV
coords_df.to_csv('data_final/european_country_coordinates.csv', index=False)


"""""

data = pd.read_csv('data_final/XXXXX')
coords = pd.read_csv('data_final/european_country_coordinates.csv')

# Optional: normalize casing just in case
data['Entity'] = data['Entity'].str.strip().str.lower()
coords['Entity'] = coords['Entity'].str.strip().str.lower()

# Merge latitude and longitude into your dataset
data_with_coords = pd.merge(data, coords, on='Entity', how='left')
"""
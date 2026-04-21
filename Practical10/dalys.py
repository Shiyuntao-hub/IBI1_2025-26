# 1. Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2. Locate the data file 
os.chdir('D:/IBI/IBI1_2025-2026/IBI1_2025-26/Practical10')  # Switch to the folder where the data is stored
print("Practical10:", os.getcwd())  # Verify if the path is correct
print("Files in the folder:", os.listdir())  # Confirm the CSV file exists

# 3. Read CSV data and check basic information
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
print("\nFirst 5 rows of data:")
print(dalys_data.head())  # Check data structure
print("\nBasic data information:")
print(dalys_data.info())  # Confirm no missing values and correct data types
print("\nData statistical description:")
print(dalys_data.describe())  # Understand the distribution of DALYs values



# 4. Show Year and DALYs for first 10 rows
first_10 = dalys_data.iloc[0:10, [2, 3]]
print("\n=== First 10 rows: Year & DALYs ===")
print(first_10)

# Comment: Year with maximum DALYs in Afghanistan's first 10 years
# Max DALYs in Afghanistan first 10 years: 1990
afghanistan_data = dalys_data.iloc[0:10]
max_year_afg = afghanistan_data.loc[afghanistan_data['DALYs'].idxmax(), 'Year']

# 5. Show all years for Zimbabwe using Boolean index
zimbabwe_bool = dalys_data['Entity'] == 'Zimbabwe'
zim_data = dalys_data.loc[zimbabwe_bool, ['Year', 'DALYs']]
print("\n=== Zimbabwe DALYs data ===")
print(zim_data)

# Comment: First and last year for Zimbabwe DALYs data
# First year: 1990
# Last year: 2019


# 6. Countries with max and min DALYs in 2019
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

country_max_2019 = data_2019.loc[data_2019['DALYs'].idxmax(), 'Entity']
country_min_2019 = data_2019.loc[data_2019['DALYs'].idxmin(), 'Entity']

print("\nCountry with maximum DALYs in 2019:", country_max_2019)
print("Country with minimum DALYs in 2019:", country_min_2019)

# Comment: Countries with max and min DALYs in 2019
# Max: [country_max_2019]
# Min: [country_min_2019]

# 7. Plot DALYs over time for the country with maximum 2019 DALYs
country_plot = dalys_data.loc[dalys_data['Entity'] == country_max_2019, ['Year', 'DALYs']]

plt.figure(figsize=(10, 5))
plt.plot(country_plot['Year'], country_plot['DALYs'], 'bo-', linewidth=1, markersize=4)
plt.xlabel('Year')
plt.ylabel('DALYs (rate from all causes)')
plt.title(f'DALYs Over Time - {country_max_2019}')
plt.xticks(rotation=-90)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# 8. Answer custom question (for question.txt)
# Question: Distribution of DALYs across all countries in 2019
data_2019_clean = data_2019.dropna()

plt.figure(figsize=(8, 5))
plt.boxplot(data_2019_clean['DALYs'], vert=True)
plt.title('Distribution of DALYs Across All Countries in 2019')
plt.ylabel('DALYs')
plt.grid(alpha=0.3)
plt.show()

# Calculate range between max and min DALYs in 2019
dalys_range_2019 = data_2019_clean['DALYs'].max() - data_2019_clean['DALYs'].min()
print("\nRange between max and min DALYs in 2019:", dalys_range_2019)
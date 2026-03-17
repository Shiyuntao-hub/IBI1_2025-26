import matplotlib.pyplot as plt
# Population datas
POP_data ={"UK":{"2020": 66.7, "2024":69.2}, "China":{"2020": 1426, "2024":1410}, "Italy":{"2020": 59.4, "2024":58.9}, 
           "Brazil":{"2020": 208.6, "2024":212.0}, "USA":{"2020": 331.6, "2024": 340.1}}

# Calculate growth rate
print("Population change 2020-2024:")
percent_change = {}
for country, data in POP_data.items():
    change= data["2024"] - data["2020"]
    growth_rate = (change / data["2020"]) * 100
    percent_change[country] = growth_rate
    print(f"{country}: {growth_rate:.2f}%")

#Rank
sorted_growth_rate = sorted(percent_change.items(), key=lambda x: x[1], reverse=True)
print("\nsorted from highest to lowest growth rate:")
for country, growth in sorted_growth_rate:
    print(f"{country}: {growth:.2f}%")

#max increase and max decrease
max_increase = max(percent_change, key=percent_change.get)
max_decrease = min(percent_change, key=percent_change.get)
print(f"\nCountry with highest growth: {max_increase}")
print(f"Country with lowest growth: {max_decrease}")

#Draw a column chart to visualize the population growth rates
plt.figure(figsize=(10, 5))
countries = list(percent_change.keys())
growth_rates = list(percent_change.values())
colors = ['green' if rate > 0 else 'red' for rate in growth_rates]
plt.bar(countries, growth_rates, color=colors)
plt.axhline(0, color='black') # Add a horizontal line at y=0
plt.xlabel('Countries') 
plt.ylabel('Population Growth Rate (%)')
plt.title('Population Growth Rates from 2020 to 2024')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
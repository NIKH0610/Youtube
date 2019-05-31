import pandas as pd
from matplotlib import pyplot as plt

countries_data = pd.read_csv('C:\\Users\\nikhi\\Desktop\\Data Visualization\\Youtube\\countries.csv')
US = countries_data[countries_data.country == 'United States']
China = countries_data[countries_data.country == 'China']

plt.xlabel = "Year"
plt.ylabel = "Population Growth (first year = 100)"
plt.title = "Percentage Growth"
plt.plot(US.year, US.population / US.population.iloc[0] * 100)
plt.plot(China.year, China.population / China.population.iloc[0] * 100)

plt.show()

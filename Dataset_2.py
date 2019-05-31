import pandas as pd
from matplotlib import pyplot as plt

countries_data = pd.read_csv('C:\\Users\\nikhi\\Desktop\\Data Visualization\\countries.csv')
US = countries_data[countries_data.country == 'United States']
China = countries_data[countries_data.country == 'China']

plt.xlabel = "Year"
plt.ylabel = "Population in millions"
plt.title = "US v/s China on Population"
plt.plot(US.year, (US.population / 10**6))
plt.plot(China.year, (China.population / 10**6))

plt.legend(['United States', 'China'])

plt.show()



#Compare the population grwoth in the US and China
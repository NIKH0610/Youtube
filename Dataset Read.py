import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv('C:\\Users\\nikhi\\Desktop\\Data Visualization\\sample_data.csv')
plt.xlabel = ("No Idea")
plt.ylabel = ("Who KNOWS,seriously!")
plt.title = ("Something of Something")
plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.legend(["Something", "Who knows"])
plt.show()


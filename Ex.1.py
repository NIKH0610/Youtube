import pandas as pd
from matplotlib import pyplot as plt

x = ("Jan", "Feb", "Mar", "Apr")
y = (2, 1, 4, 10)
z = (57, 62, 64, 68)
plt.plot (x, y)
plt.plot (x, z)
plt.xlabel("Months")
plt.ylabel("Values")
plt.title("Monthly Trend")
plt.legend(["Scrap Units", "Scrap Value in k INR"])

plt.show()
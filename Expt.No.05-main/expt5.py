import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# LINE PLOT
plt.plot([1,4,8,10])
plt.ylabel("Y-axis Numbers")
plt.xlabel("X-axis Numbers")
plt.show()

# BAR PLOT
names = ["WAD","DSBDA","DSA"]
values = [25,45,65]
plt.bar(names,values)
plt.show()

# SCATTER PLOT
names = ["WAD","DSBDA","DSA"]
values = [25,45,65]
plt.scatter(names,values)
plt.show()


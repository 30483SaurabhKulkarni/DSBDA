import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Line plot
plt.plot([1,4,8,10])
plt.ylabel("Y-axis Numbers")
plt.xlabel("X-axis Numbers")
plt.show()

# Bar plot
names = ["WAD","DSBDA","DSA"]
values = [25,45,65]
plt.bar(names,values)
plt.show()

# Pie plot
food = ["PIZZA","Burger","Sandwitch","Pasta"]
values = [24,56,78,34]
fig = plt.figure(figsize = (12,10))
plt.pie(values,labels = food)
plt.show()


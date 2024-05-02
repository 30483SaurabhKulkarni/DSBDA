import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("house.csv")

df

df.head(10)

df.info()

df.columns

df.describe

df.shape

df.isnull().sum()

sns.relplot(x='households',y='median_income',hue='total_rooms',data=df)
plt.show()

sns.relplot(x='population',y='median_income',hue='total_rooms',data=df)
plt.show()

sns.relplot(x='median_house_value',y='median_income',hue='total_rooms',data=df)
plt.show()


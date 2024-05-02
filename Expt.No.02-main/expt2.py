import pandas as pd

df = pd.read_csv("records.csv")

df

df.sort_values(["Salary"],axis=0, ascending=[True],inplace=True)

df

df.T

df.shape

df.size

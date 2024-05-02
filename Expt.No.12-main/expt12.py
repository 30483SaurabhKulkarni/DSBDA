import pandas as pd
import numpy as np

df = pd.read_csv("records.csv")

df

df.info()

# filling missing values - IMPUTATION
data = df
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())

data

# Imputation with additional column
data = df
data['SalaryMissing'] = data['Salary'].isnull()

data

# regression model
testdf = df[df['Salary'].isnull()==True]
traindf = df[df['Salary'].isnull()==False]
traindf.drop("Salary",axis=1,inplace = True)
testdf.drop("Salary",axis=1,inplace = True)

traindf

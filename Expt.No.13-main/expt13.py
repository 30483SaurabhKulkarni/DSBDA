import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

df =pd.read_csv('NFLX.csv')
print(df.head(6))
print(df.shape)

plt.figure(figsize=(16,8))
plt.title('Netflix')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(df['Close'])
plt.show()

df = df[['Close']]
print(df.head(4))

future_days = 50
df['Prediction'] = df[['Close']].shift(-future_days)
print(df.head(4))
print(df.tail(4))


x = np.array(df.drop(['Prediction'], 1))[:-future_days]
print(x)

y = np.array(df['Prediction'])[:-future_days]
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

tree = DecisionTreeRegressor().fit(x_train, y_train)

lr = LinearRegression().fit(x_train, y_train)

x_future = df.drop(['Prediction'], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
print(x_future)

tree_prediction = tree.predict(x_future)
print(tree_prediction)
print ()

lr_prediction = lr.predict(x_future)
print(lr_prediction)

Predictions = tree_prediction
valid = df[x.shape[0]:]
valid['Prediction'] = Predictions
plt.figure(figsize=(16,8))
plt.title('Model_tree')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close', 'Prediction']])
plt.legend(['Orig','Val','Pred'])
plt.show()

Predictions = lr_prediction
valid = df[x.shape[0]:]
valid['Prediction'] = Predictions
plt.figure(figsize=(16,8))
plt.title('Model_lr')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close', 'Prediction']])
plt.legend(['Orig','Val','Pred'])
plt.show()

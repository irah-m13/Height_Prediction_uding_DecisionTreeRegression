# -*- coding: utf-8 -*-
"""Height_prediction_using_DecisionTreeRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VMc2exsE-1cIVDqAYUIgTWhW3uwp0R1U

### *Importing Libraries*
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""### *Load Dataset from Local directory*"""

from google.colab import files
uploaded = files.upload()

"""### *Load Dataset*"""

dataset = pd.read_csv('dataset.csv')

"""### *Summarize Dataset*"""

print(dataset.shape)
print(dataset.head(5))

"""### *Segregate Dataset into Input X & Output Y*"""

x = dataset.iloc[:, :-1].values
x

y = dataset.iloc[:, -1].values
y

"""### Splitting dataset to test model

"""

from sklearn.model_selection import train_test_split
 x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state= 0)

"""### Training dataset using Decision tree"""

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(x_train, y_train)

"""### *Visualizing Linear Regression results*"""

x_val = np.arange(min(x_train), max(x_train), 0.01)
x_val = x_val.reshape(len(x_val), 1)
plt.scatter( x_train,y_train , color="red")
plt.plot(x_val, model.predict(x_val), color = 'black')
plt.title("Height Prediction using Decision Tree")
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()

"""### *Prediction  """

y_pred = model.predict(x_test)

from sklearn.metrics import r2_score,mean_squared_error
# root mean square error
mse = mean_squared_error(y_test, y_pred)
rmse  = np.sqrt(mse)
print("Root Mean Square Error :" , rmse)
#r2score
r2score = r2_score(y_test, y_pred)
print("R2Score : ",r2score*100)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt




# DATAFRAME
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv') # dataframe
nyc.columns = ['Date', 'Temperature', 'Anomaly'] #columns
nyc.Date = nyc.Date.floordiv(100)




# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split( nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11)






# TRAINING ALGO 
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)








# PREDICT WITHIN TRAIN/TEST DATA
predicted = linear_regression.predict(X_test)
expected = y_test

# # check every 5th element
# for p, e in zip(predicted[::5], expected[::5]):  
#     print(f'predicted: {p:.2f}, expected: {e:.2f}')








# FUTURE PREDICTIONS 
def predict( year ): # y = mx + b
    return linear_regression.coef_ * year + linear_regression.intercept_
# print( "PREDICTING - 2022\t", predict(2022)  )







# GRAPHING REGRESSION LINE
axes = sns.scatterplot(data=nyc, x='Date', y='Temperature',
    hue='Temperature', palette='winter', legend=False)  
axes.set_ylim(10, 70)  # scale y-axis 
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
y = predict(x)
line = plt.plot(x, y)
plt.show()





import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



'''
15.16

    Reimplement the simple linear regression case study of Section 15.4 using the average
    yearly temperature data. How does the temperature trend compare to the average
    January high temperatures?


    RESPONSE:
        I graphed two lines; the line of regression as well as the mean of all data points. After the Year 1955, we can see a shift in output. Altogether, we see a gradual increase in temperature throughout the years.

        Prior to 1955, the anomalous highs are along with the average of our data-set.

        Subsequent to 1955, data points start to group above the average line and after the year 2000, it becomes even less common to fall below the average of 132 years.

        The anomaly column in our data-set seems to define itself as the positive/negative deviation from the average.
'''



# DATAFRAME
nyc = pd.read_csv('ave_yearly_temp_nyc_1895-2017.csv') # dataframe
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
for p, e in zip(predicted[::5], expected[::5]):  
    print(f'predicted: {p:.2f}, expected: {e:.2f}')





# FUTURE PREDICTIONS 
# y = mx + b
def predict( year ): 
    return linear_regression.coef_ * year + linear_regression.intercept_
# print( "PREDICTING - 2022\t", predict(2022) , "\n" )  # [55.95057235]








# GRAPHING OUTPUT
print( (nyc.describe()["Temperature"]).loc[['mean' , "max" , "min" ]] )
axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', hue='Temperature', palette='winter', legend=False)  
axes.set_ylim(10, 70)
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
y = predict(x)
slope_line = plt.plot(x, y)
mean_line = plt.plot(x, np.array([nyc["Temperature"].mean(),nyc["Temperature"].mean()]) )
plt.show()





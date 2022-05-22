import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
15.14 
    https://www.ncdc.noaa.gov/cag/global/time-series/globe/ocean/ytd/12/1880-2018
    
    Load and plot the dataset using Seaborn's regplot function. What trend do you see?

    RESPONSE:
        Similar to the prior exercise, the regression of temperatures over the years has increased. Ocean Temperatures are increasing over the years. From 2010 and on, we can see the plots exponentially growing but the line of regression won't curve as it is a linear equation in order to plot.

'''



# DATAFRAME
data = pd.read_csv('average_surface_temperature_anomalies.csv')
data.columns = ['Year', 'Temperature'] #columns

# # GRAPHING
sns.regplot( x = "Year", y = "Temperature", data = data )
plt.show()
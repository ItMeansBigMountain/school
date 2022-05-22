import pandas as pd
import numpy as np

# Create a Series from the list [7, 11, 13, 17]
output = pd.Series(  [7, 11, 13, 17]  )
print("\n\tA - Create a Series from the list [7, 11, 13, 17]" )
print( output , "\n--------------------------------" )


# Create a Series with five elements that are all 100.0
output= pd.Series( 100 , index= range(0,5,1) )
print("\n\tB - Create a Series with five elements that are all 100.0" )
print( output , "\n--------------------------------" )


# Create a Series with 20 elements that are all random numbers in the range 0 to 100  
output= pd.Series( np.random.randint( 0,100,(3) , dtype = "int64" ),)
print("\n\tC - Create a Series with 20 elements that are all random numbers in the range 0 to 100" )
print( output )
print( output.describe() )
print("\n--------------------------------")


# Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'
temperatures = pd.Series( np.array( [ 98.6, 98.9, 100.2 , 97.9] ) , index=['Julie', 'Charlie', 'Sam', 'Andrea'] , dtype="float64"  )
print("\n\tD - Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'" )
print( temperatures , "\n--------------------------------" )


# Form a dictionary from the names and values in Part (d), then use it to initialize a Series
dictionary = { name:temp   for name,temp in list(temperatures.iteritems()) }
temperatures = pd.Series( dictionary )
print("\n\tE - Form a dictionary from the names and values in Part (d), then use it to initialize a Series" )
print( temperatures , "\n--------------------------------" )

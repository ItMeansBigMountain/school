import matplotlib.pyplot as plt
import numpy as np
import statistics

# DATASET
ratings = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

# fetch frequency counts
values , frequencies = np.unique(ratings , return_counts=True)




# response statistics: minimum, maximum, range, mean, median, mode, variance, and standard deviation

minimum = min(frequencies)
maximum = max(frequencies)
output_range = maximum - minimum
mean = sum(frequencies) / len(frequencies)
median = statistics.median(frequencies)
mode = statistics.mode(frequencies)
variance = np.var(frequencies)
standard_deviation = np.std(frequencies)



print(f"{frequencies = }")
print( "minimum: " , minimum )
print( "maximum: " , maximum )
print( "range: " , output_range )
print( "mean: " , mean )
print( "median: " , median )
print( "mode: " , mode )
print( "variance: " , variance )
print( "standard_deviation: " , standard_deviation )
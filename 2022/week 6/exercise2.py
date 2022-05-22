import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd



# DATASET
ratings = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

# fetch frequency counts
values , frequencies = np.unique(ratings , return_counts=True)


# init values for chart
title = f'Food Rating Frequencies out of {len(ratings):} Students'
x_label = "Rating"
y_label = "Frequency"
sns.set_style('whitegrid')


# create bar chart
output_graph = sns.barplot( x=values , y=frequencies , palette="bright")

# set chart title
output_graph.set_title(title)


# set chart labels
output_graph.set( xlabel=x_label  , ylabel=y_label   )


# LIMIT VALUES DISPLAYED FROM Y AXIS
output_graph.set_ylim(   top=max(frequencies)*1.10   )



'''
# zip(output_graph.patches , frequencies) ----> TUPLE(tuples)

    (  <matplotlib.patches.Rectangle object at 0x7f73da2a3310>   , 3  ) 
    (  <matplotlib.patches.Rectangle object at 0x7f73da2970a0>   , 4  ) 
    (  <matplotlib.patches.Rectangle object at 0x7f73da2a3700>   , 8  ) 
    (  <matplotlib.patches.Rectangle object at 0x7f73da2a3910>   , 2  ) 
    (  <matplotlib.patches.Rectangle object at 0x7f73da2a3b20>   , 3  ) 
'''


# DISPLAY GRAPH
for bar , frequency in zip(output_graph.patches , frequencies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text = f"{frequency}\n{frequency/len(values):.3%}"
    output_graph.text(text_x , text_y , text , fontsize=11, ha="center" , va="bottom")


    # debug
    # print(text_x)
    # print(text_y)
    # print(text)
    # print()




plt.show()

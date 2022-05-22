"""

EXERCISE 13.8
    Use the pandas plotting you learned in (NLP)
    create a bar chart showing the tweet counts for Twitter’s trending topics in a city of your choice.


DECOMENTATION FROM twitter api GET trends/place
    The response is an array of trend objects that encode the name of the trending topic, the query parameter that can be used to search for the topic on Twitter Search, and the Twitter Search URL.

The tweet_volume for the last 24 hours is also returned for many trends if this is available.

"""


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

import trends



def barChart(city , x_arr , y_arr):
    # init values for chart
    title = f'Tweet Counts For Twitter’s Trending Topics in {city} within last 24 hours'
    x_label = "Topic"
    y_label = "Frequency"
    sns.set_style('whitegrid')

    # create bar chart
    output_graph = sns.barplot( x=x_arr , y=y_arr , palette="bright")

    # set chart title
    output_graph.set_title(title)

    # set chart labels
    output_graph.set( xlabel=x_label  , ylabel=y_label   )

    # LIMIT VALUES DISPLAYED FROM Y AXIS
    output_graph.set_ylim(   top=max(y_arr)*1.10   )

    # DISPLAY GRAPH
    for bar , frequency in zip(output_graph.patches , y_arr):
        text_x = bar.get_x() + bar.get_width()/2.0
        text_y = bar.get_height()
        text = f"{frequency}"
        output_graph.text(text_x , text_y , text , fontsize=11, ha="center" , va="bottom")
    output_graph.set_xticklabels(output_graph.get_xticklabels(),rotation = 30)
    plt.show()


def main():
    # fetch dict
    topics , area = trends.fetch_area()

    # create df
    cols = ["Topic" , "Count"]
    final_dataframe = pd.DataFrame(columns = cols)

    # sort for graph
    x_arr = []
    y_arr = []
    for q in topics:
        # add series to df
        final_dataframe = final_dataframe.append(  pd.Series( [q , topics[q] ] , index = cols) ,  ignore_index = True )

        if not topics[q] : continue
        x_arr.append(q)
        y_arr.append(topics[q])
    
    # display data
    print(final_dataframe)
    barChart(area , x_arr , y_arr)



main()
"""

EXERCISE 13.18
    - Use the search API to get 100 tweets on a topic of your choice.
    - Preprocess the tweets
    - investigate and use TextBlob’s lowerstrip utility function to remove all punctuation and convert the text to lowercase letters
    - Display the original and cleaned version of each tweet.
    - Save the tweets to a CSV file.
"""


import tweepy
import textblob.utils as tu
import pandas as pd
from textblob import TextBlob


# AUTH
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""

# OAUTH
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True  )


# twitter object
screen_name = "MarketWatch"
tweets = api.user_timeline(screen_name = screen_name ,count=100 , tweet_mode = "extended")


# create dataframe
cols = ["Original" , "Cleaned" , "Sentiment"]
final_dataframe = pd.DataFrame(columns = cols)




for t in range(0 , len(tweets) , 1):
    # tweet text
    text  = tweets[t]._json['full_text']

    # clean data   
    clean_text = ""
    text_arr = text.split()
    for x in range(0,len(text_arr) , 1):
        # remove urls (could speed up proccess by looking for only last item but that is user specific ) 
        if "http" not in  text_arr[x] :
            clean_text += f"{text_arr[x]} ".strip("\n")
    
    # remove punctuation
    clean_text =  tu.lowerstrip(clean_text , all=True)


    # add series to df as we clean 
    final_dataframe = final_dataframe.append(  pd.Series( [text,clean_text,TextBlob(clean_text).sentiment] , index = cols) ,  ignore_index = True )




# write csv file 
final_dataframe.to_csv(f"{screen_name}.csv", sep='\t', encoding='utf-8')



# display dataframe 
print(final_dataframe)
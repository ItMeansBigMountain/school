import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests




'''
    Exercise 13.2
         - Look at 10,000 tweets and determine the percentage of tweets that begin with RT 
'''


 
#  open file of 10,000 tweets and convert to RAM object
tweets_file = open("Stream_Output_File.json" , "r")
tweets_JSON = json.loads(tweets_file.read())
tweets_file.close()



retweets = []
original_tweets = []
for i in range(0 , len(tweets_JSON) , 1):
    first_word = tweets_JSON[i]['tweet'].split()[0]
    
    if first_word == "RT":
        retweets.append( tweets_JSON[i]  )
    else:
        original_tweets.append( tweets_JSON[i]  )




percentage_of_retweets = f"{len(retweets) / len(tweets_JSON):.0%}"
print(f"{len(retweets)} retweets")
print(f"{len(original_tweets)} original tweets")
print(f"percentage of retweets: {percentage_of_retweets}")

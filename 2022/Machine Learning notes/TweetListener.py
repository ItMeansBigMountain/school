import tweepy
from textblob import TextBlob
import json



# AUTH
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""



'''
    TLDR - import into scope to stream tweets and save them to json...


USAGE
    from TweetListener import TweetListener
    STREAM = TweetListener( stream_output_file_name ) # leave blank for console only
    STREAM.filter(track=search , threaded=true)
    STREAM.sample(threaded=true)


DISCONNECTING
    when exiting the stream
        - While loop 
        - time.sleep( Refresh_Rate )
        - if STREAM.tweet_count > LIMIT : STREAM.disconnect()


PARAMETERS

    # STREAM.filter( PARAMS )
        # follow
        # track
        # locations
        # filter_level
        # languages
        # stall_warnings
        # threaded

    # STREAM.sample( PARAMS )
        # languages
        # stall_warnings
        # threaded



TWITTER SEARCH PARAMERS
    - python twitter        | finds both Python and Twitter
    - python OR twitter     | finds either one in their respective pool
    - python ?              | finds tweets asking questions about python
    - python - functions    | finds tweets about python , excluding functions
    - python :)             | finds tweets about python , positive sentiment
    - python :(             | finds tweets about python , negative sentiment
    
    - since:2018-09-01      | finds tweets since date
    - near:"New York City   | finds tweets geolocated near New York City

    - from:nasa             | finds tweets writted from nasa 
    - to:nasa               | finds tweets writted to nasa








'''

class TweetListener(tweepy.Stream):
    def __init__(self,   file_name=None , limit=10 ):
        # INDEXING
        self.tweet_count = 0
        self.TWEET_LIMIT = limit
    
        # JSON OUTPUT
        self.file = None
        self.file_name = file_name
        self.json_output = []

        # LIVE DATA ANALYSIS
        self.analysis_file = None
        self.analysis = {}

        # INIT PARENT OBJECT
        super().__init__(consumer_key , consumer_secret , access_key , access_secret)





    # ON READY
    def on_connect(self):
        if self.file_name:
            self.file = open( f"{self.file_name}.json" , "w" )
            self.analysis_file = open( f"{self.file_name}_analysis.json" , "w" )
        print("connection started...")
    




    # ON TWEET RECIEVED
    def on_status(self, status):

        try:
            tweet_text = status.extended_tweet.full_text
        except:
            tweet_text = status.text

        # ADD TO OBJECT JSON ATTRIB
        self.json_output.append(
                {
                    "tweet":status.text ,
                    "index": self.tweet_count,
                    "truncated": status.truncated,
                    "Language": status.lang,
                    "username": status.user.screen_name
                }
        )

        # update live sentiment analysis
        total_pol = 0
        total_sub = 0
        for x in range(0,len(self.json_output),1):
            tweet_sentiment = TextBlob( self.json_output[x]['tweet']  ).sentiment
            total_pol += tweet_sentiment.polarity
            total_sub += tweet_sentiment.subjectivity
        self.analysis['average_polarity'] = total_pol / len(self.json_output)
        self.analysis['average_subjectivity'] = total_sub / len(self.json_output)
        
        


        # CONSOLE DISPLAY OUTPUT
        # print(f"Screen name: {status.user.screen_name}")
        # print(f"Index: {self.tweet_count}")
        # print(f"Language: {status.lang}")
        # print(f"Status: {tweet_text}\n")

        # print(f"\n\nSentiment so far: {self.analysis}\n")


        self.tweet_count += 1
        return self.tweet_count <= self.TWEET_LIMIT


    # DISCONNECT -  call STREAM.disconnect() manually from outter scope
    def on_disconnect(self):
        captured_json = json.dumps(self.json_output ,indent = 4)
        analysis_json = json.dumps(self.analysis)
        
        self.file.write(captured_json)
        self.file.close()

        self.analysis_file.write( analysis_json  )
        self.analysis_file.close()








# DRIVER CODE
def main():
    
    # USER INPUT
    print("\n- ENTER 0 FOR STREAM OF ALL RECENT TWEETS")
    print("- Please enter search parameter\nUse ' | ' to seperate search relativity  ")
    search = input("\n> ").split("|")
    if len(search) < 1: print("INVALID SEARCH PARAMETER"); return




    # Sample all real-time tweets
    if search[-1] == '0' and len(search) == 1:
        STREAM = TweetListener(  )
        STREAM.sample()
        
        # disconnect after time
        import time 
        time_allotted = int(input("How many seconds do you want to scan for?: "))
        time.sleep(time_allotted)
        print(STREAM.tweet_count)
        STREAM.disconnect()



    # Filter realtime Tweets by keyword
    else:
        STREAM = TweetListener( "Stream_Output_File" )
        STREAM.filter(track=search , threaded=True  )
        

        # gather tweets until limit
        import os
        import time
        limit = int(input("How many tweets would you like to scan? "))
        while STREAM.tweet_count < limit:
            print( f"{STREAM.tweet_count} tweets" )
            print( f"Sentiment thus far: {STREAM.analysis}" )
            time.sleep(5)
            os.system("clear")



        STREAM.disconnect() 


if __name__ == "__main__":
    main()
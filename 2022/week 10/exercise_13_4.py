import tweepy




'''
    Exercise 13.4
         - Get the ID, name, screen name, and description of a twitter account of interest 
'''




# AUTH
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""

# OAUTH
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True  )



# fetch twitter account
user_info = api.get_user(screen_name="elonmusk")



# display data
print( user_info.id )
print( user_info.name )
print( user_info.screen_name )
if len(user_info.description):
    print(user_info.description)
else:
    print("description N/A")

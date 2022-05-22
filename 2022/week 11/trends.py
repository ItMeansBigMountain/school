from time import sleep
import tweepy


# AUTH
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""

# OAUTH
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True  )




def fetch_global():
    global_trends = api.get_place_trends(1)
    all_trends = {}
    for x in global_trends:
    # 'trends', 'as_of', 'created_at', 
        for i in x['trends']:
            # 'name', 'url', 'promoted_content', 'query', 'tweet_volume'
            print( i['name'] ,  i['tweet_volume']  )
            all_trends[i['name'] , i['tweet_volume']]

    return all_trends

def fetch_area():
    availabe_countries = api.available_trends()
    for x in range(0,len(availabe_countries),1):
        NAME = availabe_countries[x]['name']
        WOEID = availabe_countries[x]['woeid']
        print( f"{NAME} : {WOEID}"  )
    print("# United States : 23424977") # DEBUG
    print("# Tel Aviv? : 1968212")      # DEBUG
    print("# Kyiv? : 924938")           # DEBUG
    user_input = int( input("\nPlease enter id number for area\n>"))
    area_choice = None
    for x in availabe_countries:
        if x["woeid"] == user_input:
            area_choice = x["name"]
    try:
        selected_trends = api.get_place_trends(user_input)
        all_trends = {}
        for x in selected_trends:
            for i in x['trends']:
                all_trends[i['name']] =  i['tweet_volume']
        return all_trends , area_choice
    except Exception as e:
        return {"error": "invalid parameters"} , area_choice




# United States : 23424977
# Venezuela : 23424982

if __name__ == "__main__":
    print(fetch_area())
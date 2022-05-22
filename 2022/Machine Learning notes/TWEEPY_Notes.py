import tweepy 
import pprint
import TweetListener




# AUTH
auth = tweepy.OAuthHandler(TweetListener.consumer_key, TweetListener.consumer_secret)
auth.set_access_token(TweetListener.access_key, TweetListener.access_secret)
api = tweepy.API(auth , wait_on_rate_limit=True  )






# USER LOOK UP  Tweepy.get_user()
'''
user = api.get_user(screen_name='nehauri')
print(  user.
['_api', '_json', 'id', 'id_str', 'name', 'screen_name', 'location', 'profile_location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'follow_request_sent', 'notifications', 'translator_type', 'withheld_in_countries', 'suspended', 'needs_phone_verification', 'parse', 'parse_list', 'timeline', 'friends', 'followers', 'follow', 'unfollow', 'list_memberships', 'list_ownerships', 'list_subscriptions', 'lists', 'follower_ids',
'''






# SEARCH QUERY TWEETS
'''
search = api.search_tweets( q="single mothers" , count = 100 )
print(search.__dir__())
['_max_id', '_since_id', 'refresh_url', 'completed_in', 'query', 'count', 'next_results', 'parse', 'max_id', 'since_id', 'ids', 'clear', 'copy', 'append', 'insert', 'extend', 'pop', 'remove', 'index', 'reverse', 'sort', '''






# STREAMING OBJECT
STREAM = tweepy.Stream(TweetListener.consumer_key, TweetListener.consumer_secret , TweetListener.access_key, TweetListener.access_secret)

print(STREAM)

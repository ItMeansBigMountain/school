import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests




'''
    Exercise 13.1
        - Look at 10,000 tweets. Look at each tweets lang property.
        - Count and display the number of tweets in each language.
'''







 
#  open file of 10,000 tweets and convert to RAM object
tweets_file = open("Stream_Output_File.json" , "r")
tweets_JSON = json.loads(tweets_file.read())
tweets_file.close()




# BCP-47 language tag interpertation
url = "https://partnerhub.warnermediagroup.com/getting-started/automated-content-delivery/languages"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

cleaned_language_map = {
    "en":"english" ,
    "und": "undetermined",
    "in":"indonesian",
    "es":"espnol" ,
    "de":"german" ,
    "pt":"portuguese" ,
    "ht":"hatian-french" ,
    "fr":"french" ,
    "et":"etheiopian" ,
}
for table in soup.find_all('table'):
    for row in table.find_all('tr'):
        clean_row_elements = [ e.get_text(strip=True).lower() for e in  row.find_all('p')  ]
        if len(clean_row_elements):
            cleaned_language_map[clean_row_elements[1]] =  clean_row_elements[0] 
            # print( clean_row_elements )        






#  FILTER TWEETS FOR LANGUAGES OF TWEETS
language_sorted_tweets = {}
for i in range( 0  , len(tweets_JSON) , 1  ):
    if not tweets_JSON[i]['Language'] in language_sorted_tweets:
        language_sorted_tweets[tweets_JSON[i]['Language']] = [ tweets_JSON[i]['tweet']  ]
        continue
    language_sorted_tweets[tweets_JSON[i]['Language']].append(  tweets_JSON[i]['tweet']  )
    





# CLEAN DATA WITH FULL LANGUAGE NAME AND TWEETS IN THE LANGUAGE
master_output = {}
for BCP_47 in language_sorted_tweets:
    # print(language_sorted_tweets[BCP_47])
    master_output[ cleaned_language_map[BCP_47]  ] =  language_sorted_tweets[BCP_47]   







# DISPLAY 
for language in master_output:
    print( language , len(master_output[language])   )




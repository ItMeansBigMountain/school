import requests
from bs4 import BeautifulSoup
from textblob import TextBlob , Word
from textblob.sentiments import NaiveBayesAnalyzer
from textatistic import Textatistic




'''
12.7
download from 3 different news sites a current news article on the same topic.

Perform readability assessments on each of the three articles
    - determine which sites are the most readable

Display
    - average words per sentence
    - average characters per word
'''


def fetch_readability_of_article(url):
    # FETCH
    data = requests.get( url  )

    # HTML
    html_data = BeautifulSoup( data.text , features="html.parser" )

    # STRIPPED TEXTS
    text = html_data.get_text(strip=True)

    # TEXATISTIC object
    readability = Textatistic(text)
    readability_dict = readability.dict()

    # WORD / CHAR COUNTS
    counts = {
        "words_per_sentence" : readability_dict['word_count'] // readability_dict['sent_count'] ,
        "chars_per_word" :  readability_dict['char_count'] // readability_dict['word_count'] ,
    }
    

    # EXTRACT READABILITY
    return  readability_dict , counts







# DRIVER CODE


# INIT VARIABLES
facebook_Congress_article_urls = {
    'nbc': 'https://www.nbcnews.com/politics/congress/facebook-whistleblower-tell-congress-social-network-accountable-no-one-n1280786',

    'fox' : 'https://www.foxbusiness.com/politics/facebook-whistleblower-frances-haugen-live-testimony',

    'abc' : 'https://abcnews.go.com/ABCNews/live-updates/live-updates-Facebook/?id=80401245'
}
readability_output = {} 
averages = {}
count_averages = {}
score_total = 0
count_total = 0

# build meta data
for newsSation in facebook_Congress_article_urls:
    fetch_output = fetch_readability_of_article( facebook_Congress_article_urls[newsSation] )
    readability_output[newsSation] = fetch_output[0]

    count_averages[newsSation] = fetch_output[1]

    # get averages of scores and counts of complex words
    score_average = sum([
        readability_output[newsSation]['dalechall_score'],
        readability_output[newsSation]['fleschkincaid_score'],
        readability_output[newsSation]['gunningfog_score'],
        readability_output[newsSation]['smog_score']
    ]) / 4
    count_average = sum([
        readability_output[newsSation]['notdalechall_count'],
        readability_output[newsSation]['polysyblword_count']
    ]) / 2

    # add average to total pool for later comparison
    averages[newsSation] = {"score_average" : score_average , "count_average": count_average}
    score_total += score_average
    count_total += count_average




# FIND MINIMUM OF (AVERAGE SCORE PERCENTILE ) / (COMPLEX WORDS COUNT TOTAL AVERAGE)
# the idea is to divide the rating of readability in comparison to rest by the amount of complex words's compared ratios... because something can have a low rating but shorted in comparison to other passages but many complex words.

ratings = []
for i in range(0 , len(averages.keys()) , 1 ):
    item_rating = ( (averages[list(averages.keys())[i]]['score_average'] / score_total  ) / (averages[list(averages.keys())[i]]['count_average'] / count_total  ) , list(averages.keys())[i])
    ratings.append(item_rating)













# OUTPUT
from pprint import pprint
pprint(readability_output)
print("\n Easiest Read Compared to rest of corpus : " ,", ".join([i[1] for i in sorted(ratings)] ))

print("\n\n CHAR COUNTS / AVERAGE WORDS PER SENTENCE")
pprint( count_averages )





import requests
from bs4 import BeautifulSoup
from textblob import TextBlob , Word
from textblob.sentiments import NaiveBayesAnalyzer

'''
12.3
download a web page for a current news article and create a TextBlob.

Display the sentiment for
    - the entire TextBlob
    - each Sentence

'''




# FETCH
data = requests.get( "https://time.com/6121931/frances-haugen-facebook-whistleblower-profile/"  )

# HTML
html_data = BeautifulSoup( data.text , features="html.parser" )

# STRIPPED TEXTS
text = html_data.get_text(strip=True)


# BLOB object
blob = TextBlob(text)


# EXTRACT SENTIMENT 

entire_page_sentiment = blob.sentiment
each_sentences_sentiment = [ s.sentiment for s in blob.sentences ]


# OUTPUT
print('ENTIRE PAGE SENTIMENT: ' , entire_page_sentiment , end='\n\n\tEACH SENTENCE\n')
for x in each_sentences_sentiment:
    print(x )





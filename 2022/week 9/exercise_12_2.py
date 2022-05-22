import requests
from bs4 import BeautifulSoup
from textblob import TextBlob , Word
from textblob.sentiments import NaiveBayesAnalyzer

'''
12.2
TEXTBLOB - Sentences and Words, and extract its noun phrases
'''



# FETCH
data = requests.get( "https://www.python.org/about/gettingstarted/"  )

# HTML
html_data = BeautifulSoup( data.text , features="html.parser" )

# STRIPPED TEXTS
text = html_data.get_text(strip=True)


# BLOB object
blob = TextBlob(text)


# EXTRACT DATA
senteces = blob.sentences
words = blob.words
noun_phrases = blob.noun_phrases





# output
print(data)
print(f"{ len(blob.sentences) = }")
print(f"{ len(blob.words) = }")
print(f"{ len(blob.noun_phrases) = }")


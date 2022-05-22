from textblob import TextBlob , Word
from textblob.sentiments import NaiveBayesAnalyzer

blob_tags_dict = {
    "NN" : 'Single Noun',
    "VBZ" : 'Third Person Verb',
    "DT" : 'Determiner',
    "JJ" : 'Adjective',
    "MNP" : 'Proper Noun',
    "IN" : 'Preposition',
}


text = 'Today is a rainy day. I hope tomorrow is nicer.'
blob = TextBlob(text  )

'''


# print(blob.words )
# print(blob.tags )
# print(blob.noun_phrases )
# print(blob.sentences )
# print(blob.sentiment)




# SENTIMENT ANLALYZATION positive / negative
blob = TextBlob(text , analyzer=NaiveBayesAnalyzer())
for sentence in blob.sentences:
    print( sentence.sentiment  )
 

# SENTIMENT ANLALYZATION subjectivity / polarity
blob = TextBlob(text  )
for sentence in blob.sentences:
    print( sentence.sentiment  )





# SPELL CHECKING
word = Word("thrye")
spellCheck = word.spellcheck()
print(spellCheck, '<---------')


sentence = TextBlob("tihs mesagge is spelld incorectli")


correct_word = word.correct()
correct_sentence = sentence.correct()
print(correct_word)
print(correct_sentence)





# COUNTING WORD FREQUENCIES

text = 'I wish i knew about text blob word counts before this class... i have already stumbled upon this package when i was makeing the twitter text sentiment analysis and found this lib on stack overflow. I remember being so confused about initializing the text blob and where its imported from... once i learned about how imports work... classes started to make more sense as each file is technically a class. so we import the file and then use the functions as we do with a class. I realized that from using Unity game engine. Now coming back to TextBlob and how we first initialize the variable, then look into the class data type and all methods it provides.'



import pandas
import matplotlib.pyplot as plt

# word counts
sentence = TextBlob(text)
counted_words = sentence.word_counts.items()


# output
df = pandas.DataFrame( counted_words , columns =['word' , 'counts'] )
axes = df.plot.bar(x='word' , y='counts' , legend=False)
print( df  )
plt.show()




'''




# EXTRACT TEXT BODY DATA
from textatistic import Textatistic

readability = Textatistic("this is a test! I cant believe i didnt know about this sooner")

print( readability.dict()  )
# output
{'char_count': 49,
 'dalechall_score': 6.710530769230769, # EDUCATION LEVEL 4th grade to college (16th grade)
 'flesch_score': 102.53230769230771,
 'fleschkincaid_score': 2.187692307692309, # education grade lvl
 'gunningfog_score': 5.2, # education grade lvl
 'smog_score': 3.1291, #years of education to understand text
 'notdalechall_count': 2, #number of hard words
 'polysyblword_count': 0, # 3+ sylable words
 'sent_count': 1,
 'sybl_count': 14,
 'word_count': 13}




# LOOK INTO SARCASM DETECTION 








# import pprint ; pprint.pprint( readability.dict() )
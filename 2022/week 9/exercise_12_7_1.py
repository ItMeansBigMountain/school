from wordcloud import WordCloud
import imageio
import requests
from bs4 import BeautifulSoup




'''
12.7.1
create a word cloud for each of the 3 articles

. Reflect in a few sentences,
what are the similarities between the word clouds? Any striking differences?
	
	HOMEWORK ANSWER
		The topic is about facebook's privacy issues dealt in a public congress meeting. It makes sense that "whistleblower" is on all three sites. The same goes for the company name; facebook. A noticable observation , though I am not very political, I notced how fox news used the word "privacy" a lot which makes sense as conservatives are more into their reserved rights.

'''



def create_cloud(newsStation , url):	
	# IMPORT PICTURE
	image = imageio.imread("fb.png")
	
	# FETCH TEXT
	data = requests.get( url  )
	
	# HTML
	html_data = BeautifulSoup( data.text , features="html.parser" )
	
	# STRIP TEXT HTML
	text = html_data.get_text(strip=True)
	
	
	# CREATE CLOUD OBJECT
	cloud = WordCloud( width=100 , height=1000, colormap='prism' , mask=image , background_color='black')
	
	# PRODUCE PICTURE
	cloud = cloud.generate(text)
	
	# RETURN PICTURE
	cloud = cloud.to_file( f"12_7_1_{newsStation}.png" ) 






# driver code
facebook_Congress_article_urls = {
	'nbc': 'https://www.nbcnews.com/politics/congress/facebook-whistleblower-tell-congress-social-network-accountable-no-one-n1280786',

	'fox' : 'https://www.foxbusiness.com/politics/facebook-whistleblower-frances-haugen-live-testimony',

	'abc' : 'https://abcnews.go.com/ABCNews/live-updates/live-updates-Facebook/?id=80401245'
}

for key , value in facebook_Congress_article_urls.items():
	create_cloud(key , value)
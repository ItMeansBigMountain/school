"""

EXERCISE 13.9
    determine the locations for which Twitter has trending topics. Pick one of the locations and display its trending-topics list.

    create a wordcloud

"""



from trends import fetch_area
from wordcloud import WordCloud
import imageio



def create_cloud(data):	
    # IMPORT PICTURE
    image = imageio.imread("exercise_13.9_bullVSbear.jpg")
    
    
    # CREATE CLOUD OBJECT
    cloud = WordCloud( width=100 , height=1000, colormap='prism' , mask=image , background_color='black' , collocations=False)

    # populate text string for wordCloud input
    text = ""
    for item in data[0]:
        if data[0][item]:
            text += item * (data[0][item] // 1000)

    
    # PRODUCE PICTURE
    cloud = cloud.generate(text)
    
    # RETURN PICTURE
    cloud = cloud.to_file( f"exercise_13.9.png"  ) 









# main 

data = fetch_area()
create_cloud(data)
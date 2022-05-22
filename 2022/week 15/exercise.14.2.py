import random
import requests
import time


'''
14.2 Use code from 14.1 to perform all of the downloads without threading. Do 1 at a
time in a loop. Compare the time difference for downloading 50 images. Which one was
faster?
'''


# USER AGENT COOKIES ENABLED
headers = {
    'User-Agent': '',
    'From': 'testing@gmail.com'
}


# INDEX OF PICTURES
amount = 50
random_id_arr = random.sample(range(1, 100), amount)


# EXECUTION TIME START
t0 = time.time()


# FETCH DATA ONE BY ONE
for x in range(0, amount, 1):
    id = random_id_arr[x]
    data = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id}")
    url = data.json()["url"]

    # save image
    data = requests.get(url, headers=headers)
    with open(f"exercise_14_2_pictures/{id}.jpg", 'wb') as image:
        image.write(data.content)
        print(f"Save image {random_id_arr[x]}")


# EXECUTION TIME STOP
t1 = time.time()
print(f"EXECUTION TIME: {t1-t0}")

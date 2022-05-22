import queue
import threading
import random
import requests
import time


'''
14.1: Create a Python program that can multiple download images from a URL at once.
Do this by using a Queue and multiple threads. When you put an image URL into the
queue, a thread should pick it up, send a GET request to the URL, and download/save
the image. There is template code with comments to help you.
'''


# USER AGENT COOKIES ENABLED
headers = {
    'User-Agent': '',
    'From': 'testing@gmail.com'
}


def save_image(url, id):
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        with open(f"exercise_14_1_pictures/{id}.jpg", 'wb') as image:
            image.write(r.content)
    # DEBUG
    else:
        with open(f"{id}.html", 'wb') as image:
            image.write(r.content)


def download(queue):
    # FETCH DATA
    id = queue.get()  # blocks until an item is put into the queue
    result = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id}")
    url = result.json()["url"]

    # SAVE DATA
    save_image(url, id)
    queue.task_done()
    print(f"Save image {id}")


def main():
    # INIT QUEUE
    work_queue = queue.Queue()

    # INDEX OF PICTURES
    amount = 50
    random_id_arr = random.sample(range(1, 100), amount)

    # ADD INDEX TO QUEUE
    for x in range(0, amount, 1):
        work_queue.put(random_id_arr[x])

    # POP FROM QUEUE AND START THREAD
    working_threads = []
    while not work_queue.empty():
        t = threading.Thread(target=download, args=(work_queue,))
        t.start()
        working_threads.append(t)
        print(f"thread {working_threads.index(t)} starting...")

    # WAITING FOR COMPLETIONS
    for thread in working_threads:
        thread.join()
        print(f"thread {working_threads.index(thread)} complete!")


if __name__ == "__main__":
    # EXECUTION TIME START
    t0 = time.time()

    # MAIN FUNCTIONALITY
    main()

    # EXECUTION TIME STOP
    t1 = time.time()
    print(f"EXECUTION TIME: {t1-t0}")

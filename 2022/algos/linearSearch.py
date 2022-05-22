import numpy as np




def linear_search(key , data):
    for x in range(0 , len(arr) , 1):
        if data[x] == key:
            return x
    return -1






arr = np.random.randint(0,100 , 100)
search = 26
found_index = linear_search(search , arr)


print(f"SEARCHING: {search}")
print(arr)
print(found_index)
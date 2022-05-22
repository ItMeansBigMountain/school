import numpy as np

def insertionSort(data):
    for i in range( 1 , len(data) , 1):
        current = data[i]
        backwards = i
        while backwards > 0 and data[backwards-1] > current:
            data[backwards]  = data[backwards-1]
            backwards -= 1
        data[backwards] = current
        print(data)
    return data




# driver code
arr = np.random.randint(0,100 , 10)
print(arr)

arr = insertionSort(arr)
print(arr)
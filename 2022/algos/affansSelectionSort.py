import numpy as np





def selectionSort( data ):

    for x in range( 0 , len(data) , 1):
        for y in range( x+1 , len(data) , 1):
            if data[x] > data[y]:
                temp = data[x]
                data[x] = data[y]
                data[y] = temp
    return data







# Driver code

arr = np.random.randint(0,100 , 20)
print(arr)

arr = selectionSort( arr )
print(arr)
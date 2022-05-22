import numpy as np



def selectionSort( data ):

    for x in range( 0 , len(data) -1 , 1):
        # init smallest number
        smallest_item_index = x
        for y in range( x+1 , len(data) , 1): #every number in list
            if data[smallest_item_index] > data[y]: #compared to each item yonder...
                smallest_item_index = y #if smaller than smallest, replace smallest value
        data[smallest_item_index] , data[x] = data[x] , data[smallest_item_index] # place @ front
    return data






# Calling functions down here
arr = np.random.randint(0,100 , 20)
print(arr)

arr = selectionSort( arr )
print(arr , "----")
import numpy as np 



def binary_search(data, key , low , high):
    if key == -1:
        print("good bye")
        exit()

    if low == high:
        if data[low] == key:
            return low
        else:
            return -1
    else:
        middle = (low + high + 1) // 2           
        
        # DEBUG
        print(remaining_elements(data, low, high))
        print('   ' * middle, end='') 
        print(' * ') 

        if key == data[middle]:                                   
            return middle
        elif key < data[middle]: 
            return binary_search(data, key, low, middle-1 )     
        else:                 
            return binary_search(data, key, middle + 1, high )     
        middle = (low + high + 1) // 2  

def remaining_elements(data, low, high):
    """Display remaining elements of the binary search."""
    return '   ' * low + ' '.join(str(s) for s in data[low:high + 1])








data = np.random.randint(10, 91, 15)
data.sort()
print('\n' ,  data)

# user input
search_key = int(input('Enter an integer value (-1 to quit): ')) 

# perform search
location = binary_search(data, search_key , 0 , len(data)-1 )
print("LOCATION : " , location)

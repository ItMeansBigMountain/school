import numpy as np

# MUST BE SORTED
def binary_search(key , data):
    lowest = 0
    highest = len(data) -1
    middle = middle = (lowest + highest + 1) // 2
    location = -1
    while lowest <= highest and location == -1:
        print( data[lowest:highest] , data[middle] ) 
        if key == data[middle]:
            location = middle
        elif key < data[middle] :
            highest = middle - 1
        elif key > data[middle] :
            lowest = middle + 1 
        middle = (lowest + highest + 1) // 2
    return location 





# driver code
arr = np.random.randint(0,100 , 20) ; arr.sort() 
search = 25
found_index = binary_search( search , arr)


print(f"SEARCHING: {search}")
# print(arr)
print(found_index)
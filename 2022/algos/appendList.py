import numpy as np

def insert(list, n):
    index = len(list)
    # Searching for the position
    for i in range(len(list)):
      if list[i] > n:
        index = i
        break
  
    # Inserting n in the list
    if index == len(list):
      list = list[:index] + [n]
    else:
      list = list[:index] + [n] + list[index:]
    return list

debug_arr = sorted(np.random.randint(0 , 100 , 10))
print(debug_arr)
debug_arr = insert( debug_arr , 36)
print(debug_arr);exit()


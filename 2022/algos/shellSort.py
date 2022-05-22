import numpy as np  


def shellSort(arr):
    gap = len(arr) // 2 # initialize the gap
 
    while gap > 0:
        i = 0
        j = gap
         
        # check the array in from left to right
        # till the last possible index of j
        while j < len(arr):
     
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
         
            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:
 
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
        gap //= 2
    return arr

debug_arr = np.random.randint(0 , 100 , 10)
print(debug_arr)
debug_arr = shellSort(debug_arr)
print(debug_arr);exit()

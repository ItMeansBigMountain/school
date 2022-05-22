# sorting algorithms copy pasted from geeksforgeeks

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end
      

def insertionSort(arr):
   for i in range(1, len(arr)):
      j = i-1
      nxt_element = arr[i]
# Compare the current element with next one
   while (arr[j] > nxt_element) and (j >= 0):
      arr[j+1] = arr[j]
      j=j-1
   arr[j+1] = nxt_element


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


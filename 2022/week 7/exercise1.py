import numpy as np





problem_1 = '''
def mystery(a,b):
    if b ==1:
        return a
    else:
        return a + mystery(a, b -1 )
print(mystery(2, 10))
'''
def mystery(a,b):
    # print(a,b)
    if b ==1:
        return a
    else:
        debug = a + mystery(a, b -1 )
        # print(f"{debug = }")
        # return debug
        return a + mystery(a, b -1 )
# print(mystery(2, 10));exit()








problem_2 = """
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n)
"""
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
# print( sum(5)  );exit()







problem_3 = """
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
        if key == data[middle]:                                   
            return middle
        elif key < data[middle]: 
            return binary_search(data, key, low, middle-1 )     
        else:                 
            return binary_search(data, key, middle + 1, high )     
        middle = (low + high + 1) // 2  
"""
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

        # youre just checking and then checking again with a step back in one of the variables... If you find it in one of them then the recursion should stop and then carry on with the first stack of functions' logic path 

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









#  problem 4
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

# debug_arr = sorted(np.random.randint(0 , 100 , 10))
# print(debug_arr)
# debug_arr = insert( debug_arr , 36)
# print(debug_arr);exit()





# problem 4
def shellSort(arr):
    gap = len(arr) // 2 # initialize the gap
 
    while gap > 0:
        i = 0
        j = gap
        
        while j < len(arr):
     
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
            k = i

            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
        gap //= 2
    return arr

# debug_arr = np.random.randint(0 , 100 , 10)
# print(debug_arr)
# debug_arr = shellSort(debug_arr)
# print(debug_arr);exit()






# problem 4
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
        # for every outer iteration, go through each 
        for j in range(0, n-i-1):
            # print( arr[j] > arr[j + 1])
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print( n-i-1)
            # print(  arr[j], arr[j+1]   )
            # print(arr)
            # print()
    return arr
# debug_arr = np.random.randint(0 , 100 , 10)
# print(debug_arr)
# debug_arr = bubbleSort(debug_arr)
# print(debug_arr);exit()










def main():

    # problem 1
    print("************************\tProblem 11.1\t************************")
    print(problem_1)
    print(
"""
The point of this algorithim is to recursively add a total
as the function completes the stack to reach the base case in order to multiply 
a * b

- "a" represents the number we would like to add
- "b" represents how many times we will add "a" to itself due to returning "a + (a+(a+(...)))"

- First extend down to the base case then add two as it crawls back up the ladder.

"""
    )








    # problem 2
    print("\n\n************************\tProblem 11.2\t************************")
    print(problem_2)
    print(
"""
LOGIC ERROR: n is never decremented by -1... thus the function will call itself forever, returning n each time.

CORRECTION: In the second return statement, we need to resolve (n - 1) within the recursive call's parameters.

    ex: return n + sum(n-1)

"""
    )




    # problem 3
    print("\n\n************************\tProblem 11.8\t************************")
    print(problem_3 )
    # BINARY SEARCH     
    data = np.random.randint(10, 91, 15)
    data.sort()
    print('\n' ,  data)

    # user input
    search_key = int(input('Enter an integer value (-1 to quit): ')) 

    # perform search
    location = binary_search(data, search_key , 0 , len(data)-1 )
    print("LOCATION : " , location)


    # problem 4
    print("\n\n************************\tProblem 11.20\t************************")
    print(
"""
DETERMINE BIG-O NOTATION FOR LISTED ALGOS

    ● Get or set an item by index in a Python list.
        ex: arr[0] = "new value" \tOR\t foo = arr[0]
        
        One computation ---> O(1)


    ● Insert a new value in order in a Python sorted list.
        ex: 
            INSERT: 36
            [7, 20, 47, 51, 68, 71, 71, 72, 74, 94]
            [7, 20, 36, 47, 51, 68, 71, 71, 72, 74, 94]
                     ^
        Linear iteration ---> O(n)


    ● Shell short an array.
        ex:
            [35 64 47 50  5 82 94 50 48 53]
            [ 5 35 47 48 50 50 53 64 82 94]
        
        Tripple nested loop ---> O(n* log2n)
                                 O(n2)


    ● Bubble sort an array.
        ex:
            [61 58 39 86 87 20 28 93 96 39]
            [20 28 39 39 58 61 86 87 93 96]
        
        Nested For Loops ---> O(n2)



"""
    )






if __name__ == '__main__':
    main()

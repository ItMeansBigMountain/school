import random

def main():
    exArray = []
    for x in range (1, 5000):
        randomInt = random.randint(1, 1000)
        exArray.append(randomInt)
    #print(exArray)
    print('Sequential Search')
    sequentialSearch(exArray, 999)
    insertionSort(exArray)  ### binary search needs list elements to be sorted
    print('------------------------------------------------------------------------------- \n')
    #print(exArray)
    print('Binary Search')
    binarySearch(exArray, 999)

def sequentialSearch(array, searchVal):
    x = 0
    comparisons = 0
    found = False
    while found == False and x < len(array):
        comparisons = comparisons + 1
        if array[x] == searchVal:
            found = True
            print('The value being searched for is: ', searchVal)
            print('The value is found at position: ', x + 1)
            print('It took this many comparisons to find: ', comparisons)
        else:
            x = x + 1

    if searchVal not in array:
        print('The value being searched for is: ', searchVal)
        print('Value not found')


def insertionSort(array):
    for x in range(1, len(array)):
        valueToSort = array[x]
        while array[x - 1] > valueToSort and x > 0:
            array[x], array[x - 1] = array[x - 1], array[x]
            x = x - 1

def binarySearch(array, searchVal):
    lowIndex = 0
    highIndex = len(array) - 1
    Found = False
    comparisons = 0
    while lowIndex <= highIndex and Found == False:
        midIndex = (lowIndex + highIndex) // 2
        comparisons += 1
        if searchVal == array[midIndex]:
            Found = True
            print('The value being searched for is: ', searchVal)
            print('The value is found at position: ', midIndex + 1)
            print('It took this many comparisions to find: ', comparisons)
        elif searchVal > array[midIndex]:
            lowIndex = midIndex + 1
        else:
            highIndex = midIndex - 1

    if searchVal not in array:
            print('The value being searched for is: ', searchVal)
            print('Value not found')
       
main()
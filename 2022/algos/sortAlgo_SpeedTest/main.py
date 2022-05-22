# This homework showcases that you understand how to create class methods and how to decorate them with another function
# This program will create and sort a list of 2000 random integers using bubble sort, merge sort, and insertion sort
# The sorting methods of the Sorter class will be decorated using a function that will measure the time it takes for the 
# sorting functions to execute, and the amount of memory they use


import random
import benchmark
import algorithims 
import copy


class Sorter():
    '''class Sorter takes an array to construct, and then provides 3 sorting algorithm methods
    that are decorated with benchmark.measure_performance'''
    
    def __init__(self, array):  
        self.array = array


    @benchmark.measure_performance
    def bubble_sort(self):
        algorithims.bubbleSort(self.array)
    

    @benchmark.measure_performance
    def merge_sort(self):
        algorithims.mergeSort(self.array)

    
    @benchmark.measure_performance
    def insertion_sort(self):
        algorithims.insertionSort(self.array)




def main():
    # create a list of 2000 random integers
    array = [random.randint(0, 100) for i in range(2000)]
    
    sorter = Sorter(array) # create an instance of the sorter object with the array 
    
    print(f'\nSorting and Benchmarking Random Integer Array with length: {len(array)}\n')
    
    # call the sorting methods
    sorter.bubble_sort()
    sorter.merge_sort()
    sorter.insertion_sort()

if __name__ == "__main__":
    main()
    

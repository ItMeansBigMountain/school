
import random

def main():
	saddle = [[], #element 0 of saddle which is a list/array itself
			[], #element 1 of saddle
			[], #element 2 of saddle
			[], #etc
			[],
			[],
			[]]
	
	rows = 0 #initalize rows variable
	while rows < len(saddle): # loop to write values into all elements of saddle array
		for x in range(len(saddle)): #making rows of data for saddle array
			randomNum = random.randint(0, 99) #get random numbers 0-99
			saddle[x].append(randomNum) #write random numbers into element x of row x
			x += 1 #increment x in the for loop
		rows += 1 #increment rows in the while loop
		
	for x in range(len(saddle)):  #loop to print saddle array       
		print(saddle[x]) #prints each element of saddle on its own line
		x+=1 #increment x 


	getRowMin(saddle) #call the next functions
	print('---------------------------\n')
	getColMax(saddle)

def getRowMin(array): #get lowest value(s) in row
	for x in range(len(array)): #loop to get lowest values from each array element
		lowRowValue = min(array[x])
		print (lowRowValue)

def getColMax(array):
	for y in range(0,len(array)):
		arr = []
		for x in array:
			arr.append(x[y])
		maxo = max(arr)
		print(maxo)


main()
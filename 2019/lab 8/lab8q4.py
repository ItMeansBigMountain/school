# display data:
# 	average of arr

import random

def main():
	data = []
	for i in range(1,101):
		data.append(int(random.randint(0,999)))
	print(data)

	low = getLow(data)
	high = getHigh(data)
	total = getTotal(data)
	average = getAVG(data)

	print('\nLOWEST:' , data[low])
	print('HIGEST:', data[high])
	print('TOTAL:', total)
	print('AVERAGE:' , average)

def getLow(data):
	lowIndex = 0
	for x in range(1,len(data)):
		if data[lowIndex] > data[x]:
			lowIndex = x
	return lowIndex

def getHigh(data):
	highIndex = 0
	for x in range(1,len(data)):
		if data[highIndex] < data[x]:
			highIndex = x
	return highIndex

def getTotal(data):
	total = 0
	for x in range(0,len(data)):
		total += data[x]
	return total

def getAVG(data):
	average = (getTotal(data) / len(data))
	return average


main()


# OUTPUT

# [85, 799, 364, 519, 168, 614, 499, 374, 525, 61, 990, 120, 595, 947, 261, 128, 779, 622, 628, 438, 197, 709, 362, 786, 281, 633, 378, 670, 496, 668, 69, 272, 634, 562, 94, 890, 25, 772, 531, 281, 661, 295, 376, 872, 973, 189, 791, 871, 68, 902, 852, 64, 166, 452, 23, 306, 926, 630, 662, 594, 625, 719, 570, 332, 219, 658, 707, 588, 859, 729, 769, 375, 250, 481, 243, 921, 568, 350, 735, 753, 90, 659, 267, 343, 948, 317, 976, 739, 340, 694, 580, 476, 549, 421, 929, 248, 778, 970, 9, 965]

# LOWEST: 9
# HIGEST: 990
# TOTAL: 52248
# AVERAGE: 522.48
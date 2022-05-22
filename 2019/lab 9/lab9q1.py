scores = [] 
for x in range(0,9):
	scores.append(int(input('Type in a scores: ')))
print(scores)

for x in range(len(scores)-1 , 0 , -1): #Start second to the last so you can compare to right
	for y in range(x): #whatever index it is in the list, do a condition
		if scores[y] > scores[y+1]:#check to see if 
			temp = scores[y] #placeholer since we are gonna change a number before the iteration
			scores[y] = scores[y+1]
			scores[y+1] = temp

print(scores)
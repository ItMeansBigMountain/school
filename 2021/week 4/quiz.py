def averageScores():
    scores = open("scores.txt"  ,  'r')
    scores_arr = scores.readlines()
    
    clean_data = []
    for x in range(0 , len(scores_arr) , 1):
        clean_data.append(int(scores_arr[x].rstrip()))
    scores.close()

    counter = 0
    total = 0
    while counter < len(clean_data):
        total += clean_data[counter]
        counter+=1
    return total / counter 


# OUTPUT
output = averageScores()
print(output)




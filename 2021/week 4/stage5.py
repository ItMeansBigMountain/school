def displayScores(scoreArray):
    print("The current test scores are:")
    for i in range(len(scoreArray)-1):
        print(float(scoreArray[i]), end= "%, ")
    print(float(scoreArray[len(scoreArray)-1]), end = "%\n")
    



def dropLowest( grades , minimum ):
    grades.remove(minimum)
    new_grades = []
    for x in range(len(grades)):
        new_grades.append(grades[x])

    return new_grades












def findMin(scoreArray):
    """Finds the minimum value in list passed by parameter"""
    num = scoreArray[0]
    for x in range(1 , len(scoreArray) , 1):
        if num > scoreArray[x]:
            num = scoreArray[x]
    return float(num)

def findMax(scoreArray):
    """Finds the maximum value in list passed by parameter"""
    num = scoreArray[0]
    for x in range(1 , len(scoreArray) , 1):
        if num < scoreArray[x]:
            num = scoreArray[x]
    return float(num)

def getMean(scores):
    total = 0
    for x in range(0, len(scores)  , 1):
        total += scores[x]
    return total / len(scores)

def findMedian(grades):
    median = None

    temp = []
    for x in range(0 , len(grades) , 1):
        temp.append(grades[x])

    temp.sort()

    # finds middle points || even or odd
    if len(temp) % 2 == 0:
        first_end = temp[:len(temp)//2][-1]
        second_start = temp[len(temp)//2:][0]
        median = (first_end + second_start) / 2
    else:
        midPoint = round(   len(temp) / 2  - 0.5     )
        median = temp[midPoint]
    return median


def getScores():
    test_scores = []
    with open("scores.txt" , "r" ) as file:
        file_arr = file.readlines()
        for x in range(len(file_arr)):
            test_scores.append(int(file_arr[x].rstrip()))
    return test_scores




def saveScores(test_scores):
    with open("updatedScores.txt." , "a" ) as file:
        for x in range(len(test_scores)):
            file.write( f'{test_scores[x]}\n'  )










def main():
    testScores = getScores()


    displayScores(testScores)
    
    print()
    
    minimum = findMin(testScores)
    print("Lowest Score: ", int(minimum))
    maximum = findMax(testScores)
    print("Highest Score: ", int(maximum))
    avg = getMean(testScores)
    print("Average: ", avg)
    median = findMedian(testScores)
    print("Median: ", median)

    

    new_grades = dropLowest( testScores , minimum )
    print("\nAfter droping the test score. ")
    displayScores(new_grades)
    avg = getMean(new_grades)
    print("Average: ", avg)
    median = findMedian(new_grades)
    print("Median: ", median)

    # saving test scores into new file
    saveScores(new_grades)

main()




# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework\week4>stage5.py
# The current test scores are:
# 95.0%, 74.0%, 98.0%, 76.0%, 84.0%, 89.0%, 92.0%, 74.0%

# Lowest Score:  74
# Highest Score:  98
# Average:  85.25
# Median:  86.5

# After droping the test score.
# The current test scores are:
# 95.0%, 98.0%, 76.0%, 84.0%, 89.0%, 92.0%, 74.0%
# Average:  86.85714285714286
# Median:  89
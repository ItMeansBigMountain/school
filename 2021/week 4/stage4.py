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





def main():
    testScores = [90,85,52,74,95,100,78]
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


main()




# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework\week4>stage4.py
# The current test scores are:
# 90.0%, 85.0%, 52.0%, 74.0%, 95.0%, 100.0%, 78.0%

# Lowest Score:  52
# Highest Score:  100
# Average:  82.0
# Median:  85

# After droping the test score.
# The current test scores are:
# 90.0%, 85.0%, 74.0%, 95.0%, 100.0%, 78.0%
# Average:  87.0
# Median:  87.5



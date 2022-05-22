def main():
   
    print('\n**  Osama Chamout **\n') # Display author's name
# Decalre Varibles

    endProgram = "no"
    while endProgram == "no":
        totalScores = 0
        averageScores = 0
        counter = 0
        number = 0
        score = 0
        number = getNumber()
        totalScores = getScores(number)
        averageScores = getAverage(totalScores, number)
        printAverage (averageScores)
        endProgram = input("Do you want to end program? (Enter yes or no) " )
       
# this function will calculate the average score
def getAverage(totalScores, number):
    averageScores = totalScores / number
    return averageScores

# this function will ask for number of students that took the test
def getNumber():
    number = int(input("How many students took the test: "))
    while number <2 or number > 30:
        print('Class Size Error! Please enter class size (2-30 students)')
        number = int(input("How many students took the test: "))
    return number

# this function will will produce the total Scores
def getScores(number):
    totalScores = 0
    for counter in range(1, number + 1):
        score = float(input("Enter their score: "))
        while score < 0 or score > 100:
            print('Test score percentage needs to be between 0 and 100!')
            score = float(input("Enter their score: "))
        totalScores = totalScores + score
    return totalScores

#this function will give the average score

def printAverage(averageScores):
   print("the average test score is " + str(averageScores))

# call main

main()
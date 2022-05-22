#The main function
def main():
    endProgram = 'no'
    print()
    while endProgram == 'no':
        option = 0

        print ("\nEnter 1 to enter in new data and store to file")
        print ("Enter 2 to display data from the file")
        option = int(input("Enter now ->"))
        print()


# Declare Varibles
        pints = [0]*7
        totalPints = 0
        averagePints = 0
       
# function calls
        if option == 1:
            pints = getPints(pints)
            totalPints = getTotal(pints, totalPints)
            averagePints = getAverage(totalPints, averagePints)
            writeToFile(averagePints, pints)
        elif option == 2:
            readFromFile(averagePints, pints)
           
# endprogram option
        endProgram = input("Do you want to end program? (Enter no or yes): ")
        while not (endProgram == 'yes' or endProgram == 'no'):
            print ("Please enter a yes or no")
            endProgram = input("Do you want to end program? (Enter no or yes): ")



#The get pints fucntion
def getPints(pints):
    counter = 0
    while counter < 7:       #operation looping
        pints[counter] = int(input("Enter pints collected: "))
        counter = counter + 1
    return pints

# The get total function
def getTotal(pints, totalPints):
    counter = 0
    while counter < 7:
        totalPints = totalPints + pints[counter]
        counter = counter + 1
    return totalPints


# The get average function
def getAverage(totalPints, averagePints):
    averagePints = float(totalPints) / 7
    return averagePints

# The Write to file function
def writeToFile(averagePints, pints):
    outFile = open('blood.txt', 'a')
    outFile.write('Pints Each Hour\n')
    counter = 0
    while counter < 7:
        outFile.write(str(pints[counter]) + '\n')
        counter = counter + 1
    outFile.write('Average Pints')
    outFile.write(str(averagePints) + '\n\n')
    outFile.close()
           
# The read from file function
def readFromFile(averagePints, pints):
    inFile = open('blood.txt', 'r')
    str1 = inFile.read()
    print(str1)
    pints = inFile.read()
    print (pints)
    print()
    str2 = inFile.read()
    print (str2)
    averagePints = inFile.read()
    print (averagePints)
    inFile.close()
       
# Call Main
main()
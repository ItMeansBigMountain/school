def main():
    print('\n**  Osama Chmaout **\n') # Display author's name
    endprogram = 'no'
    while endprogram == 'no':

    # Declare Variables
        pints = []
        totalPints = 0
        averagePints = 0
        highPints = 0
        lowPints = 0


        # call funtions
        pints = getPints(pints)
        totalPints = getTotal(pints,totalPints)
        averagePints = getAverage(totalPints,averagePints)
        highPints = getHigh(pints,highPints)
        lowPints = getLow(pints, lowPints)
        displayInfo(averagePints, highPints, lowPints)

        endprogram = input ('Do you want to end program? (Enter yes or no): ')
        while not (endprogram == 'yes' or endprogram == 'no'):
            print('Please enter yes or no')
            endprogram = input('Do you want to end program? (Enter yes or no): ')

# getPints
def getPints(pints):
    for x in range(0,7):
        print(x+1)
        pints.append(int(input('Enter pints collected: ')))
    return pints

#get total
def getTotal(pints, totalPints):
        counter = 0
        while counter < 7:
            totalPints += int(pints[counter])
            counter = counter + 1
        return totalPints
       
# get Average
def getAverage(totalPints, averagePints):
    averagePints = float(totalPints) / 7
    return averagePints

# get High
def getHigh(pints, highPints):
    highPints = pints[0]
    counter = 0
    while counter < 7:
        if pints[counter] > highPints:
            highPints = pints[counter]
        counter = counter + 1
    return highPints


# get Low
def getLow(pints, lowPints):
    lowPints = pints[0]
    counter = 0
    while counter < 7:
        if pints[counter] < lowPints:
            lowPints = pints[counter]
        counter = counter + 1
    return lowPints

# Display Info
def displayInfo(averagePints, highPints, lowPints):
    print ('The average amount of pints are' , averagePints)
    print('The highest amount of pints are' , highPints)
    print('The lowest amount of pints are' , lowPints)

# call main
main()
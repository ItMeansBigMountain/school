print('\n**  Osama Chmaout **\n')
def main():

#declaring Variables
    endProgram = "no"       #program ends when user types no
    notGreenCost = [0] * 12
    goneGreenCosts = [0] * 12 # array to hold 12 elements
    savings = [0] * 12
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    option = 0
    while endProgram == "no":       #loop
       
# Function calls
        option = int(input())
        if option == 1:         #Module will call if user inputs 1
            getNotGreen(notGreenCost, months)
            getGoneGreen(goneGreenCosts, months)
            energySaved(notGreenCost, goneGreenCosts, savings)
        elif option == 2:       #Module will call if user inputs 2
            displayInfo(notGreenCost, goneGreenCosts, savings, months)
        elif option == 3:       #Module will call if user inputs 3
            writeToFile(months, savings)
        elif option == 4:       ##Module will call if user inputs 4
            readFromFile(months, savings)
           
        print("Do you want to end the program? Yes or no")      #asks to end program
        endProgram = input()


def writeToFile(months, savings):
    savingsFile = open("savings1.txt", 'a')     #open savings1.txt  
    savingsFile.write("Savings")                # write savingFile as Savings
    counter = 0
    while counter < 12:                     # 12 time loop
        savingsFile.write(months[counter])
        savingsFile.write(savings[counter])
        counter += 1
    savingsFile.close()                     # close savingsFile

# Function read from file
def readFromFile(months, savings):
    savingsFile = open("savings1.txt") #open savings.txt
    for x in savingsFile:
        print(x)
    savingsFile.close()         #close savingsFile

# Function get not green
def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 12:         # 12 time loop
        print("Enter NOT GREEN energy costs for " + months[counter])
        notGreenCost[counter] = input()     #user input
        counter += 1

# function get gone green
def getGoneGreen(goneGreenCosts, months):
    counter = 0
    while counter < 12:     #12 time loop
        print("Enter GONE GREEN energy costs for " + months[counter])
        goneGreenCosts[counter] = input() #user input
        counter += 1

# fucntion energy Saved
def energySaved(notGreenCost, goneGreenCosts, savings):
    counter = 0
    while counter < 12:     # loops 12 times
        savings[counter] = int(notGreenCost[counter] - goneGreenCosts[counter])  #Calculation needed for savings amount
        counter += 1

# Function display info
def displayInfo(notGreenCost, goneGreenCosts, savings, months):
    counter = 0
    while counter < 12: #12 time loop
        print("Information for " + months[counter])
        print("Savings $" + savings[counter])
        print("Not Green Costs $" + notGreenCost[counter])
        print("Gone Green Costs $" + goneGreenCosts[counter])
        counter += 1
main()


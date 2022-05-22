#######################################################
# Class:      CIS-1400
# Assignment: Week 06 
# File:       Homework-06.py
# Purpose:    test score calculator 
#######################################################
def main():
    print('\n**  Osama Chmaout **\n') # Display author's name

# Declare Local Variables
    endprogram = 'no'
    while endprogram == 'no':
        notGreenCost=[]
        goneGreenCost=[]
        savings=[]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

#function calls
        notGreenCost = getNotGreen(notGreenCost, months)
        goneGreenCost = getGoneGreen(goneGreenCost, months)
        savings = energySaved(notGreenCost, goneGreenCost, savings)
        displayInfo(notGreenCost, goneGreenCost, savings, months)
        endprogram =  input("Do you want to end program? Yes or No")
    


#Get not Green
def getNotGreen(notGreenCost,months): 
    counter=0
    while(counter<12):
        print("Enter NOT GREEN energy costs for",months[counter])
        notGreenCost.append(float(input())) #Taking REAL input as float type
        counter=counter+1
    return notGreenCost

#Get gone green
def getGoneGreen(goneGreenCost,months): #getGoneGreen module
    counter=0
    print('\n-----------------------------------\n')
    while(counter<12):
        print("Enter GONE GREEN energy costs for",months[counter])
        goneGreenCost.append(float(input()))    #Taking REAL input as float type
        counter=counter+1
    return goneGreenCost

#Get Save energy
def energySaved(notGreenCost,goneGreenCost,savings): #energySaved module
    counter=0
    while(counter<12):
        savings.append(float(notGreenCost[counter]-goneGreenCost[counter]))  #calculating savings
        counter=counter+1
    return savings

#Dispaly info
def displayInfo(notGreenCost,goneGreenCost,savings,months): #display module
    counter=0
    while(counter<12):
        print("Information for",months[counter])
        print("Savings $",savings[counter])
        print("Not Green Costs $",notGreenCost[counter])
        print("Gone Green Costs $",goneGreenCost[counter])
        print()
        counter=counter+1

# call main
main()

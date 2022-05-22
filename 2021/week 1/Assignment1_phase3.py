##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name: Affan Fareed
##Date: 9/21/2021


# INPUT
quarters = int(input("Enter a number of Quarters: "))  * 25 / 100
dimes = int(input("Enter a number of Dimes: "))  *  10 / 100
nickels = int(input("Enter a number of Nickles: "))  * 5   / 100
pennies = int(input("Enter a number of Pennies: "))  * 1 / 100

# ALGO
CHANGE = quarters + dimes + nickels + pennies

leftover = CHANGE * 100

quarters = leftover // 25
leftover = round(leftover % 25)

dimes = leftover // 10
leftover = round(leftover % 10)

nickels = leftover // 5
leftover = round(leftover % 5)

pennies = leftover // 1
leftover = round(leftover % 1)

# DISPLAY
print(f"Number of coins for ${round(CHANGE , 2)} in change is: \n")
print(f"Quarters: {int(quarters)}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")


# output
# Enter a number of Quarters: 30
# Enter a number of Dimes: 4
# Enter a number of Nickles: 6
# Enter a number of Pennies: 19
# Number of coins for $8.39 in change is:

# Quarters: 33
# Dimes: 1
# Nickels: 0
# Pennies: 4
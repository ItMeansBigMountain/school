##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name: Affan Fareed
##Date: 9/21/2021

# INPUT
CHANGE = int(input("Enter the amount of change to convert: "))


# ALGO
leftover = CHANGE

quarters = leftover // 25
leftover = leftover % 25

dimes = leftover // 10
leftover = leftover % 10

nickels = leftover // 5
leftover = leftover % 5

pennies = leftover // 1
leftover = leftover % 1

# DISPLAY
print(f"Number of coins for {CHANGE} cents in change is: \n")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")


# # OUTPUT
# Enter the amount of change to convert: 143
# Number of coins for 143 cents in change is:

# Quarters: 5
# Dimes: 1
# Nickels: 1
# Pennies: 3
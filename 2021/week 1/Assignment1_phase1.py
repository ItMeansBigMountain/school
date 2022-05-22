##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name: Affan Fareed
##Date: 9/21/2021


# INPUT
CHANGE = 97


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



# OUTPUT
# Number of coins for 97 cents in change is:

# Quarters: 3
# Dimes: 2
# Nickels: 0
# Pennies: 2

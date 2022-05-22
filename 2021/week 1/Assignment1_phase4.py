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

twenties = leftover // 2000
leftover = round(leftover % 2000)

tens = leftover // 1000
leftover = round(leftover % 1000)

fives = leftover // 500
leftover = round(leftover % 500)

ones = leftover // 100
leftover = round(leftover % 100)

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
print(f"Twenties: {int(twenties)}")
print(f"Tens: {int(tens)}")
print(f"Fives: {int(fives)}")
print(f"Ones: {int(ones)}")
print(f"Quarters: {int(quarters)}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")


# output
# Number of coins for $27.91 in change is:

# Twenties: 1
# Tens: 0
# Fives: 1
# Ones: 2
# Quarters: 3
# Dimes: 1
# Nickels: 1
# Pennies: 1
# The user will input the number of inches 
# convert a specific number of inches in to an equivalent number of combined yards, feet, and inches.

# INPUT
inches_input = int(input('How many inches are in your measurement: '))


# PROCCESSING
leftover = inches_input

yards =  leftover //  (12 * 3 ) 
leftover = leftover % 36

feet =  leftover //  12 
leftover = leftover % 12

inches =  leftover //  1
leftover = leftover % 1



# DISPLAY
print(f'{yards = }')
print(f'{feet = }')
print(f'{inches = }')



# OUTPUT
# How many inches are in your measurement: 175
# yards = 4
# feet = 2
# inches = 7

# C:\Users\affan\Desktop\SchoolHomework\week1>
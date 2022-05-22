# input
num = int(input("Please enter a number to see if its perfect or not: "))



# Go through every number from 1 --> num
#  check if it perfectly goes into it
# if it does, add to num_sum
# check if num sum == the user input
num_sum = 0
for y in range(1 , num , 1):
    if num % y == 0:
        num_sum += y

if num_sum  == num:
    print('PERFECT!')
else:
    print("imperfect...")




# output
# NOTE: seperated by different scenarios...

# Please enter a number to see if its perfect or not: 28
# PERFECT!


# Please enter a number to see if its perfect or not: 14
# imperfect...
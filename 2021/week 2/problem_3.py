
# input
maximum = int(input("please enter max number : "))

# algo
total = 0
for x in range( 1   , maximum+1  , 1  ):
    total += x

# display
print(f'The total from 1 to {maximum} is {total}')


# OUTPUT
# please enter max number : 255
# The total from 1 to 255 is 32640
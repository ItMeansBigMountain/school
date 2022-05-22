# INPUTS
amount = int(input("Please enter how many values you would like to check: "))
minimum = int(input("Value 1 : "))

# AGLO
for x in range( 1 , amount   , 1):
    next_val = int(input(f"Value {x+1} : "))
    if next_val < minimum:
        minimum = next_val

# DISPLAY
print(f"The smallest number in the set was: {minimum} ")



# # output
# Please enter how many values you would like to check: 3
# Value 1 : -99
# Value 2 : 5
# Value 3 : 9
# The smallest number in the set was: -99
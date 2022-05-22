amount = int(input("How many rows? "))


x = True
while amount > 0:
    for i in range(0,5,1):
        if x:
            print('x' , end=' ')
            x = False
        else:
            print('o' , end=' ')
            x = True
    print()
    amount -= 1


# output
# How many rows? 5
# x o x o x
# o x o x o
# x o x o x
# o x o x o
# x o x o x
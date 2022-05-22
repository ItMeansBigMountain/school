import time

# input
count = int(input("Please enter amount of sequences: "))


# algo
a = -1
b = 1
for x in range(  0 , count+1 , 1  ):
    c = a + b
    a = b
    b = c
    if c == 0:
        x -= 0
    else:
        print(c)




#output
# Please enter amount of sequences: 8
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
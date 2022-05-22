
for x in range(2 , 101 , 1):
    prime = True
    for y in range(2 , x , 1):
        if x % y == 0:
            prime = False
    if prime:
        print(x)


# output
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97
import random


x = random.randint(1 , 9)
y = random.randint(1 , 9)

# INPUT
answer = int(input(f"What is {x} * {y}? "))

# ALGO
lives = 3
while answer != x *y:
    lives -= 1
    if lives < 1:
        print("OUT OF LIVES!")
        break
    else:
        print("wrong...\n")
        answer = int(input(f"What is {x} * {y}? "))

# DISPLAY
if answer == x*y:
    print("right answer!")






# OUTPUT


# [FIRST TRY RIGHT ANSWER]
# What is 8 * 5? 40
# right answer!



# [WRONG THREE TIMES]
# What is 3 * 4? 1
# wrong...

# What is 3 * 4? 1
# wrong...

# What is 3 * 4? 1
# OUT OF LIVES!




# [WRONG FIRST TIME AND RIGHT THE NEXT TIME]
# What is 2 * 4? 1
# wrong...

# What is 2 * 4? 8
# right answer!


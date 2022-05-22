sentenel = 80
print(f'GRADE GOAL: {sentenel}')



# input
grade = float(input("Please enter grade (accepts decimal ex: 89.5):  "))


if round(grade) >=90:
    print("\nproccesed grade: A")
elif round(grade) >=80:
    print('\nproccesed grade: B')
elif round(grade) >=70:
    print('\nproccesed grade: C')
elif round(grade) >=60:
    print('\nproccesed grade: D')
elif round(grade) >=50:
    print('\nproccesed grade: F')


# algo
while round(grade) < sentenel :
    grade = float(input(f"\nYOU DIDNT GET A {sentenel}% OR BETTER!? \n\t try again.... \n what did you get now? :  "))
    if round(grade) >=90:
        print("\nproccesed grade: A")
    elif round(grade) >=80:
        print('\nproccesed grade: B')
    elif round(grade) >=70:
        print('\nproccesed grade: C')
    elif round(grade) >=60:
        print('\nproccesed grade: D')
    elif round(grade) >=50:
        print('\nproccesed grade: F')



# output
# NOTE :seperated by case scenarios


# [EXACT SCORE]
# GRADE GOAL: 80
# Please enter grade (accepts decimal ex: 89.5):  80

# proccesed grade: B

# C:\Users\affan\Desktop\SchoolHomework\week2>problem_11.py





# [ROUNDED SCORE]
# GRADE GOAL: 80
# Please enter grade (accepts decimal ex: 89.5):  79.5

# proccesed grade: B

# C:\Users\affan\Desktop\SchoolHomework\week2>problem_11.py



# [HIGHER THAN EXPECTED SCORE]
# GRADE GOAL: 80
# Please enter grade (accepts decimal ex: 89.5):  90

# proccesed grade: A

# C:\Users\affan\Desktop\SchoolHomework\week2>problem_11.py




# [RETRY UNTIL PASS]
# GRADE GOAL: 80
# Please enter grade (accepts decimal ex: 89.5):  70

# proccesed grade: C

# YOU DIDNT GET A 80% OR BETTER!?
#          try again....
#  what did you get now? :  50

# proccesed grade: F

# YOU DIDNT GET A 80% OR BETTER!?
#          try again....
#  what did you get now? :  66.5

# proccesed grade: D

# YOU DIDNT GET A 80% OR BETTER!?
#          try again....
#  what did you get now? :  99

# proccesed grade: A




def main():
    endprogram = False #endprogram variable
    while endprogram == False:
        print('\nArea Of A Circle: 1')
        print('Area Of A Rectangle: 2')
        print('Area Of A Triangle: 3')

        choice = input('Enter Choice To Begin Calculation (PRESS "4" TO EXIT): ')
        if choice == '4': 
            endprogram = True #kills program
        else:

            if choice == '1':
                circle()
            elif choice == '2':
                rectangle()
            elif choice == '3':
                triangle()
            else:
                print('Option not found...')


def circle():
    print('CIRCLE')
    pi = 3.14159
    radius = int(input('Enter radius of circle: '))
    radius = radius * radius
    area = pi * radius
    print('The area of your circle is: ' + str(area) , '<---------')
    

def rectangle():
    print('RECTANGLE')
    length = int(input('Enter length of rectangle: '))
    width = int(input('Enter width of rectangle: '))
    area = length * width
    print('The area of your rectangle is: ' + str(area), '<---------')

def triangle():
    print('TRIANGLE')
    base = int(input('Enter base length of triangle: '))
    height = int(input('Enter height of triangle: '))
    area = (base * height) * .5
    print('The area of your triangle is: ' + str(area) , '<---------')


main()


# output

# C:\Users\affan\Desktop\SchoolHomework>lab11q3.py

# Area Of A Circle: 1
# Area Of A Rectangle: 2
# Area Of A Triangle: 3
# Enter Choice To Begin Calculation (PRESS "4" TO EXIT): 1
# CIRCLE
# Enter radius of circle: 50
# The area of your circle is: 7853.974999999999 <---------

# Area Of A Circle: 1
# Area Of A Rectangle: 2
# Area Of A Triangle: 3
# Enter Choice To Begin Calculation (PRESS "4" TO EXIT): 2
# RECTANGLE
# Enter length of rectangle: 25
# Enter width of rectangle: 25
# The area of your rectangle is: 625 <---------

# Area Of A Circle: 1
# Area Of A Rectangle: 2
# Area Of A Triangle: 3
# Enter Choice To Begin Calculation (PRESS "4" TO EXIT): 3
# TRIANGLE
# Enter base length of triangle: 30
# Enter height of triangle: 5
# The area of your triangle is: 75.0 <---------

# Area Of A Circle: 1
# Area Of A Rectangle: 2
# Area Of A Triangle: 3
# Enter Choice To Begin Calculation (PRESS "4" TO EXIT): 4

# C:\Users\affan\Desktop\SchoolHomework>
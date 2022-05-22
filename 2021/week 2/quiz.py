def leapyear():
    # input
    year = int(input("Enter a year: "))


    # set leap_year false
    # check if divisable by 100 , if so.  check if divisable by 400, if so.  set leap year to true, else leave alone
    #  if not divisable by 100 ,  check if divisable by 4, if so.  set leap year to true, else leave alone

    leap_year = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    else:
        if year % 4 == 0:
            leap_year = True

    if leap_year:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')



    # output
    # Enter a year: 2008
    # 2008 is a leap year

    # C:\Users\affan\Desktop\SchoolHomework\week2>quiz.py
    # Enter a year: 2011
    # 2011 is not a leap year

def sum_of_inputs():
    # input
    num = int(input("please enter a positive number (negative numebrs will end the code) : "))

    # while user input is greater than 0, keep asking and adding the total.
    total = 0
    while num >= 0:
        total += num
        num = int(input("\nplease enter a positive number (negative numebrs will end the code) : "))


    # DISPLAY
    print(f'total: {total}')



    # output
    # please enter a positive number (negative numebrs will end the code) : 10

    # please enter a positive number (negative numebrs will end the code) : 10

    # please enter a positive number (negative numebrs will end the code) : 10

    # please enter a positive number (negative numebrs will end the code) : -10
    # total: 30
def main():
    userNum = int(input('Enter an integer here: '))
    while userNum <= 0:
        print('Invalid input, must be integer greater than 0')
        userNum = int(input('try again: '))
    print('The sum of all integers from 1 to',userNum,'is:',recursiveSum(userNum))

def recursiveSum(num):
    if num == 1:
        return 1
    else:
        return num + recursiveSum(num - 1)
        
        
main()
    

##>>> 
##=========== RESTART: C:/Users/hbx17/Desktop/python Code/Lab #13.py ===========
##Enter an integer here: -1
##Invalid input, must be integer greater than 0
##try again: 6
##The sum of all integers from 1 to 6 is: 21
##>>> 
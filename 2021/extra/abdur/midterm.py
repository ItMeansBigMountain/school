# problem 1
def bldcount(fileName):
    with open( fileName , 'r', encoding='utf-8') as f:
        firstLineStr = f.readline()
        bloodtypeArr = firstLineStr.split(' ')
        
        amountA = 0
        amountB = 0
        amountAB = 0
        amountO = 0
        amountOO = 0
        
        for x in range (len(bloodtypeArr)) :
            if bloodtypeArr[x] == 'A':
                amountA +=1
            elif bloodtypeArr[x] == 'B':
                amountB +=1
            elif bloodtypeArr[x] == 'AB':
                amountAB +=1
            elif bloodtypeArr[x] == 'O':
                amountO +=1
            elif bloodtypeArr[x] == 'OO':
                amountOO +=1

        if amountA == 0:
            amountA= 'no'
        elif amountB == 0:
            amountB= 'no'
        elif amountAB == 0:
            amountAB= 'no'
        elif amountO == 0:
            amountO= 'no'
        elif amountOO == 0:
            amountOO= 'no'
        
    print('There are {} patients of bloodtype A'.format(amountA))
    print('There are {} patients of bloodtype B'.format(amountB))
    print('There are {} patients of bloodtype AB'.format(amountAB))
    print('There are {} patients of bloodtype o'.format(amountO))
    print('There are {} patients of bloodtype oo'.format(amountOO))

# problem 2 
def password_check(newpassword , oldpassword ):
    valid = False


    numCount = 0
    notAnumber = 0
    for x in newpassword:
        try:
            number = int(x)
            numCount +=1
        except:
            notAnumber += 1





    if newpassword == oldpassword:
        valid = False
    elif len(newpassword) < 6 :
        valid = False

    elif numCount == 0:
        valid = False
    
    else:
        valid = True
    
    print(valid)
    return valid

# problem 3

def duplicate(FileName):
    with open( FileName , 'r', encoding='utf-8') as f:
        dupeCount = 0
        textArr = None

        AllArr = f.readlines()
        for x in AllArr:
            line = x.rstrip("\n")
            lineArr = line.split(' ')



# problem 4


def mySort(lst):
    #'sorts a lst in acending order'
    for i in range(len(lst)):
        for j in range (len(lst)+ 1):
            if lst[j]<lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    print(lst)




#calling functions down here

# Problem 1
# bldcount('bloodtype1.txt')

# problem 2
# password_check( 'E10-sff' , 'E10.sff' )
# password_check( 'E10sf' , 'E10.s2ff' )
# password_check( 'E10-s2ff' , 'E10-s2ff' )
# password_check( 'EFG-sTff' , 'E10.s2ff' )

# problem 3 
# duplicate('noDuplicates.txt')


# problem 4
mySort([5,2,4,1])
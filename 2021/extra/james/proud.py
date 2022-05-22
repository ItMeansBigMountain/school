##James Bailey
## 3/25/20
## Lab 9 Problem 2 - sorting names with selection sort

def main():
    names = []
    getNames(names)
    sortNames(names)
    print(names)


def getNames(array):
    alphabet = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
    for x in range(1,6):
        userInput = str(input('Enter a name here: '))
        while userInput[0] not in alphabet:
            print('Error, please enter a name')
            userInput = str(input('Try again: '))
        array.append(userInput.capitalize())
    return array

def sortNames(array):
    for x in range(len(array)-1):
        lowIndex = x
        for i in range(x, len(array)):
            if array[i] < array[lowIndex]:
                lowIndex = i
        array[x],array[lowIndex] = array[lowIndex],array[x]



main()
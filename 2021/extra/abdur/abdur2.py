#question 1
def avgOfWords(passage ):
    word_arr = passage.split() #this makes an array of all words in string
    sum_of_all = 0
    for x in word_arr:
        sum_of_all += len(x)
    avg = sum_of_all / len(word_arr)
    avg = round(avg , 2)
    return avg
def howManyTimes(passage , check):
    word_arr = passage.split()
    count=0
    for x in word_arr:
        if check == x:
            count += 1
    return count
def translatePassage(p):
    print( '\nThe average length of a word in the passage is {}\n'.format(  avgOfWords(p)  ) )
    
        #ASCII CODES KEY IS REPLACEABLE, VALUE IS REPLACE WITH
    table = { 10 : 32, 46 : 32, 44:32 , 59 : 32 } 
    exclude =  ('\n' , '.' , ',' , ';')

    newP = p.translate(table)
    print('\nThe passage after removing {}: \n{}'.format(exclude, newP)   )
    # print(len(newP))

    newP = newP.strip()
    print('\nThe passage after removing leading and trailing blank spaces is: \n{}'.format(newP))
    # print(len(newP))

    newP = newP.lower()
    print('\nThe passage in lowercase: \n{}'.format(newP))
    
    HM_it_was = howManyTimes(newP, 'was')
    print( '\nThe number of occurrences in the new passage of string "it was" : {}'.format(HM_it_was) )

    newP = newP.replace('was' , 'is')
    print('\nThe passage after replacing "was" with "is" :\n {}'.format(newP))

    listP = newP.split()
    print('\nThe list of words in the passage are: \n{}'.format(listP))

p = 'It was the best of times, it was the worst of times; it was the age of wisdom, it was the age of foolishness; it was the epoch of belief, it was the epoch of incredulity; it was ...'
translatePassage(p)


# question 2
def reverseInt(n):
     
    rev = 0
    
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10

    print(rev) 

    return rev
reverseInt(123)




# question 3
def mySort(Mylist):
    numList = []
    strList = []

    for x in Mylist:
        ItemType = type(x)
        if ItemType == type(1) or ItemType == type(0.1) :
            numList.append(x)
        else:
            strList.append(x)


    print('The original list: {}'.format(Mylist))
    print('List of strings: {}'.format(strList))
    print('List of numbers: {}'.format(numList))
lst = ['cats', 2, 'dog', 'bird', 3, 4]
mySort(lst)



# problem 4
def sortSentence(string):
    array = string.split()
    revArr = []
    array.sort()

    count = len(array) -1
    while count >= 0:
        revArr.append(array[count])
        count -= 1

    print(  ( array  , revArr  )  )
    return ( array  , revArr  )

string = 'hello world cow bat earth park cup mug cat dog'
sortSentence(string)



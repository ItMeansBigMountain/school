"""
Searching and Sorting Algorithims

Big O 
    

why?
    we need to use the best algos for time complexity so that we do not tax the computer so hard
    "better code" 
        readability / execution speed




VOCABULARY
    parallelize : multiple proccesors working at the same time

GOLDEN RATIO : 1.618


"""



# SIMPLE FUNCTION
def factorials(n):
    # product of all integers from number down to one.
    factorial = 1
    for number in range( n , 0 , -1  ):
        factorial *= number
    return factorial
# output = factorials(5)
# print(output)




# LAMBDA FACTORIAL RECURSION
fact = lambda x :  x * fact(x-1) if x > 0 else 1
# print(  fact(5)  )













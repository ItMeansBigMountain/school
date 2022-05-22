# UPPER CASE LETTERS AND REMOVE WHITESPACE FROM BOTH SIDES
def formatData(information: str)  :
    # capitalize
    information = information.upper()
    # remove whitespace
    information = information.strip()
    return information


# Concantinate to empty string after removing all whitespace and splitting str into arr
# FIRST NAME
def getFirstName(fullName: str):
    # remove whitespace
    fullName = fullName.strip()
    
    # split string into arr
    arr = fullName.split()

    # output will get concantinated with the first name
    output = ""
    output += arr[0][0].upper()
    for x in range( 1 , len(arr[0]) , 1 ):
        output += arr[0][x]
    return output


# Concantinate to empty string after removing all whitespace and splitting str into arr
# LAST NAME
def getLastName(fullName: str):
    # remove whitespace
    fullName = fullName.strip()
    
    # split string into arr
    arr = fullName.split()

    # output will get concantinated with the last name
    output = ""
    output += arr[1][0].upper()
    for x in range( 1 , len(arr[1]) , 1 ):
        output += arr[1][x]
    return output


# validates email bly first splitting str into 2 parts
# then checking the second part by splitting it into two other parts
# checking if this new variable's second half is a valid domain
def validateEmail(emailAddress: str):

    # clean data before conditionals
    emailAddress = emailAddress.strip()

    # SETUP VARIABLES
    valid = False
    valid_domains = ["com" , 'org' , "net"]
    arr = emailAddress.split("@")
    email_domain = arr[1].split(".")


    # check if @ sign spits the string into two parts
    if len(arr) != 2:
        return False
    
    # checks if second part of email string is formatted with only one period
    if len(email_domain) != 2:
        return False

    # iterate through valid domains and check if domain is valid
    for vd in valid_domains:
        if vd == email_domain[1]:
            valid = True

    # if the string survives the conditionals its valid
    return valid


# Iterates through phone number string to check if chars are places propperly 
# index variable will justify what item in the string is... conditionals check for exact symbol and if segments are digits
def validatePhoneNumber(number: str):
    # clean data before conditionals
    number = number.strip()

    # if length is off just stop it right here...
    if len(number) != 12:
        return False
    
    # iterate through the string and check with arithmatic conditionals
    for x in range(12):
        # FIRST SEGMENT
        if x < 3:
            if not  number[x].isdigit():
                return False
        # DIVIDER MUST BE A MINUS SIGN
        elif x == 3 :
            if number[x] != "-":
                return False
        # SECOND SEGMENT
        elif x < 7:
            if not  number[x].isdigit():
                return False
        # DIVIDER MUST BE A MINUS SIGN
        elif x == 7:
            if number[x] != "-":
                return False
        
    # survivor!
    return True


# iterate through the string with conditionals to check if the chars are valid
def validatePassword(password: str):

    # init variables
    symbol_arr = [  "!" , '@' , "#" , "$" , "%" , "^" , '&' , "*"  , "(" , ")" ]

    # clean data before conditionals
    password = password.strip()

    # password must be at least 10 digits
    if len(password) < 10:
        return False
    
    # CONDITIONAL BOOLEANS (all must be true to return true)
    lowercase = False
    uppercase = False
    digit = False
    symbol = False


    # iterate through str one by one and check its char type
    for x in range(0 , len(password) , 1):
        
        # ALPHABETIC CHAR
        if password[x].isalpha():
            # check upper
            if password[x].isupper():
                uppercase = True
            # check lower
            if password[x].islower():
                lowercase = True
        
        # NUMERIC CHAR
        elif password[x].isdigit():
            digit = True

        # JUSTIFIED SYMBOLS
        elif password[x] in symbol_arr:
            symbol = True

    # check if all booleans are true
    # if any are false return false.... if survives... its good!
    if lowercase == False:
        return False
    if uppercase == False:
        return False
    if digit == False:
        return False
    if symbol == False:
        return False
    return True







def test():
    print( "formatData()  : " ,  formatData(  "    The quick brown fox jumps over the lazy dog   "   )    )
    print( "getFirstName()  : " ,  getFirstName(  "Affan      Fareed   "   )    )
    print( "getLastName()  : " ,  getLastName(  "   Affan Fareed"   )    )
    print( "validateEmail()  : " ,  validateEmail(  "affan.fareed@gmail.com     "   )    )
    print( "validatePhoneNumber()  : " ,  validatePhoneNumber(  '630-923-2300     '   )    )
    print( "validatePassword()  : " ,  validatePassword(  '  ru aaaaaAaaaais24 '   )    )


if __name__ == '__main__':
    test()


# # OUTPUT
# formatData()  :  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
# getFirstName()  :  Affan
# getLastName()  :  Fareed
# validateEmail()  :  True
# validatePhoneNumber()  :  True
# validatePassword()  :  False

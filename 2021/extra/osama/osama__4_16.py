def main():
    alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z'] #declare an alphabet to organize the list of names
    names = [] #list of names empty for now

    getNames(names,alphabet) #function to retrieve names (go to  def getNames)
    sort_names(names, alphabet) #function to sort (go to  def sort_names)

    print('\nThe sorted names are:') #display sorted names
    for x in names:
        print(x)

    endprogram = False #endprogram variable
    while endprogram == False:
        value = input('\nEnter a name that you want to look up (press enter to end program): ')
        if value == '': #if value is left empty (Input 'enter')
            endprogram = True #kills program
        else:
            output = binary_search(names, value) #binary search returns position and count
            if output[0] == -1: #if search not found
                print('Name not found')
                print('Array lookups: ', str(output[1]))
            else: #if name is found
                print('Name Found: ', str(value))
                print('Position: ', str(output[0]))
                print('Array lookups: ', str(output[1]))

def getNames(names , alphabet):
    howmany = int(input('How many names will you enter? (numbers only): ')) #amount of names
    for x in range(0,howmany): #for loop with range of how many you want
        print(str(x+1))
        input_name = str(input('Type in a name: '))
        while input_name[0] not in alphabet: #validation to make sure name is an alphabetical element
            print('Invalid name input!') #if not then throw an error
            input_name = str(input('Type in a name: ')) #re enter value
        names.append(input_name) #add names to list if passed validation

def sort_names(names, alphabet):
    for i in range(len(names)):
        minposition = i #index in arr that will be judged
        
        for x in range(i,len(names)): #go through rest of array to swap (starts at names[i])

            render_name = names[x] #takes names next to minposition
            alphaChar = render_name[0] #takes first letter of the name
            alphapos = alphabet.index(alphaChar)#checks the alphabet to see where the letter was found

            render_name2 = names[minposition] #takes the name of original judged name
            alphaChar2 = render_name2[0] #takes first letter of minposition name
            alphapos2 = alphabet.index(alphaChar2) #checks the alphabet to see where the letter was found

            if alphapos == alphapos2: #checks to see if name next to minpos is same alpha-category
                alphaChar = render_name[1]# checks second letter
                alphapos = alphabet.index(alphaChar) #checks alphabet postion of second letter

                alphaChar2 = render_name2[1] #checks min postion second letter
                alphapos2 = alphabet.index(alphaChar2)#checks alphabet postion of second letter

            if alphapos < alphapos2: #if the names next to judged name comes before judged name, 

                minposition = x #basically this loop will go through the array and find the variable that should be next to orignal itirated index (names[i])

        temp = names[i] #temp is orignal itirated index
        names[i] = names[minposition] #whatever it was will become names[minposition]
        names[minposition] = temp  #whatever was next to the original will become temp... so it goes through the whole array to find its place.

def binary_search(arr, value): #takes arguments (names, user input search)

    # Set the initial values
    first = 0
    last = len(arr) - 1
    position = -1
    count = 0
    found = False

    # Search for the value
    while not found and first <= last:
        count += 1

        # Calculate the mid point
        middle = int((first + last) / 2)

        # If the value is found at the mid point...
        # if arr[middle] == value:
        if arr[middle] == value:
            found = True
            position = middle

        # Else if value is in the lower half...
        # elif arr[middle] > value:
        elif arr[middle] > value:
            last = middle - 1

        # Else if value is in the upper half...
        else:
            first = middle + 1

    # Return the position of the item, or -1 if it was not found
    # Return the count of iterations of loop
    return position, count

main()


# output

# How many names will you enter? (numbers only): 20
# 1
# Type in a name: Lisandra
# 2
# Type in a name: Daphne
# 3
# Type in a name: Jani
# 4
# Type in a name: Jerry
# 5
# Type in a name: Amy
# 6
# Type in a name: Min
# 7
# Type in a name: Vanetta
# 8
# Type in a name: Dillon
# 9
# Type in a name: Carroll
# 10
# Type in a name: Grover
# 11
# Type in a name: Jerri
# 12
# Type in a name: Siobhan
# 13
# Type in a name: Gizelle
# 14
# Type in a name: Izeah
# 15
# Type in a name: Woodrow
# 16
# Type in a name: Piper
# 17
# Type in a name: Glen
# 18
# Type in a name: Kimberly
# 19
# Type in a name: Terrance
# 20
# Type in a name: Marta

# The sorted names are:
# Amy
# Carroll
# Daphne
# Dillon
# Gizelle
# Glen
# Grover
# Izeah
# Jani
# Jerri
# Jerry
# Kimberly
# Lisandra
# Marta
# Min
# Piper
# Siobhan
# Terrance
# Vanetta
# Woodrow

# Enter a name that you want to look up (press enter to end program): Amy
# Name Found:  Amy
# Position:  0
# Array lookups:  4

# Enter a name that you want to look up (press enter to end program): Jerri
# Name Found:  Jerri
# Position:  9
# Array lookups:  1

# Enter a name that you want to look up (press enter to end program): Marta
# Name Found:  Marta
# Position:  13
# Array lookups:  5

# Enter a name that you want to look up (press enter to end program): Bob
# Name not found
# Array lookups:  4

# Enter a name that you want to look up (press enter to end program):


def getNames(names):
    for x in range(0,5):
        input_name = str(input('Type in a name (Make sure the first letter is capital please): '))
        while input_name[0] not in alphabet:
            print('Invalid name input!')
            input_name = str(input('Type in a name: '))
        names.append(input_name)

def sort(names, alphabet):
    for i in range(len(names)):
        minposition = i
        
        for x in range(i,len(names)):
            render_name = names[x]
            alphaChar = render_name[0]
            alphapos = alphabet.index(alphaChar)

            render_name2 = names[minposition]
            alphaChar2 = render_name2[0]
            alphapos2 = alphabet.index(alphaChar2)

            if alphapos == alphapos2:
                alphaChar = render_name[1]
                alphapos = alphabet.index(alphaChar)

                alphaChar2 = render_name2[1]
                alphapos2 = alphabet.index(alphaChar2)

            if alphapos < alphapos2:
                minposition = x

        temp = names[i]
        names[i] = names[minposition]
        names[minposition] = temp

alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
names = []
getNames(names)
sort(names, alphabet)
print(names)

# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework>lab9q2Alphabet.py
# Type in a name (Make sure the first letter is capital please): larry
# Type in a name (Make sure the first letter is capital please): lola
# Type in a name (Make sure the first letter is capital please): bob
# Type in a name (Make sure the first letter is capital please): affan
# Type in a name (Make sure the first letter is capital please): tim
# ['affan', 'bob', 'larry', 'lola', 'tim']
phonetic = {
    'A' : 2,
    'a' : 2,
    'B' : 2,
    'b' : 2,
    'C' : 2,
    'c' : 2,
    'D' : 3,
    'd' : 3,
    'E' : 3,
    'e' : 3,
    'F' : 3,
    'f' : 3,
    'G' : 4,
    'g' : 4,
    'H' : 4,
    'h' : 4,
    'I' : 4,
    'i' : 4,
    'J' : 5,
    'j' : 5,
    'K' : 5,
    'k' : 5,
    'L' : 5,
    'l' : 5,
    'M' : 6,
    'm' : 6,
    'N' : 6,
    'n' : 6,
    'O' : 6,
    'o' : 6,
    'P' : 7,
    'p' : 7,
    'Q' : 7,
    'q' : 7,
    'R' : 7,
    'r' : 7,
    'S' : 7,
    's' : 7,
    'T' : 8,
    't' : 8,
    'U' : 8,
    'u' : 8,
    'V' : 8,
    'v' : 8,
    'W' : 9,
    'w' : 9,
    'X' : 9,
    'x' : 9,
    'Y' : 9,
    'y' : 9,
    'Z' : 9,
    'z' : 9,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '0' : 0,
} #DICTIONARY TO REFER ALPHABET TO


number = input('Enter Phone Number phonetically: ')
string = ''
while len(number) < 12 or number[3] != '-': #validate if input less than 12 or 4 char isnt '-'
    print('ERROR: INVALID NUMBER ENTRY (ex: 555-GET-RICH)')
    number = input('Enter Phone Number phonetically: ')

for x in range(0,3): #add first three digits to string
    string += number[x]

counter = 0
for x in number:
    counter+=1
    if counter>3:  #making sure i dont add the first three char to string again
        if phonetic.get(x) == None: #since isnt in the dict 
            string+= '-' #i can add it if i want to and remove this
        else:
            string += str(phonetic.get(x))

print(string) #string is now fully concantinated. (did i spell that right?)


# OUTPUT

# C:\Users\affan\Desktop\SchoolHomework>lab12q6.py
# Enter Phone Number phonetically: 630-923-2300
# 630-923-2300

# C:\Users\affan\Desktop\SchoolHomework>lab12q6.py
# Enter Phone Number phonetically: 555-get-rich
# 555-438-7424

# C:\Users\affan\Desktop\SchoolHomework>lab12q6.py
# Enter Phone Number phonetically: 555-GET-FOOD
# 555-438-3663

# C:\Users\affan\Desktop\SchoolHomework>lab12q6.py
# Enter Phone Number phonetically: 555GETfood
# ERROR: INVALID NUMBER ENTRY (ex: 555-GET-RICH)
# Enter Phone Number phonetically: 2
# ERROR: INVALID NUMBER ENTRY (ex: 555-GET-RICH)
# Enter Phone Number phonetically: 6309232300
# ERROR: INVALID NUMBER ENTRY (ex: 555-GET-RICH)
# Enter Phone Number phonetically: iWantanA
# ERROR: INVALID NUMBER ENTRY (ex: 555-GET-RICH)
# Enter Phone Number phonetically: 630-923-RICH
# 630-923-7424

# C:\Users\affan\Desktop\SchoolHomework>
vowels = ['a', 'A', 'e', 'E', 'I', 'i', 'O', 'o', 'U', 'u']
vowel_count = 0
consonant = 0

sentence = input('Enter sentence here: ')

for x in sentence:
    if x == '.':
        pass
    elif x == ' ':
        pass
    elif x in vowels:
        vowel_count += 1
    elif x not in vowels:
        consonant += 1
    

print('\nVOWELS')
print(str(vowel_count), '\n')
print('CONSONANT')
print(str(consonant), '\n')


# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework>lab12q3.py     NORMAL SENTENCE
# Enter sentence here: hello my name is affan

# VOWELS
# 7

# CONSONANT
# 11

# C:\Users\affan\Desktop\SchoolHomework>lab12q3.py     TESTING PERIODS
# Enter sentence here: hello. my name. is affan.

# VOWELS
# 7

# CONSONANT
# 11

# C:\Users\affan\Desktop\SchoolHomework>lab12q3.py     TESTING NO SPACES
# Enter sentence here: hellomynameisaffan

# VOWELS
# 7

# CONSONANT
# 11


# same answer for all 3
def removeVowels(string):
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    output = ""
    for i in range(len(string)):
        if string[i] in vowels:
            pass
        else:
            output += string[i]
    return output




# calling function down here
print(removeVowels("lets see if this works"))
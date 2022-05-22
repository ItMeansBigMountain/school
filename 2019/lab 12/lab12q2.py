def main():
    sentence = input('Enter your sentence: ')
    capital_sentence = ''
    if sentence.find('.'): #looks for period so if not, just capitalize sentence
        print()
        for x in sentence.split('.'):
            try:
                if x[0].isspace(): #if theres a space in the beginning of the sentence
                    x = x[1 : : ] #removes first char from item in sentence.split arr
                    upper = x.capitalize()
                    capital_sentence += str(upper+'. ') #adds newly capatalized sentence to string
                else:
                    upper = x.capitalize()#doesnt remove the first letter, just capitalizes it
                    capital_sentence += str(upper+'. ') 
            except:
                pass #in case user adds period at end of sentence, ignore if operation cannot carry
        print(capital_sentence)
    else:
        sentence.capitalize()
        print()
        print(sentence)

main()


# OUTPUT

# C:\Users\affan\Desktop\SchoolHomework>lab12q2.py
# Enter your sentence: hello my name affan. i had such a productive day. the only issue was that the stocks dropped a bunch. after hours, it went back up. hopefully tomorrow they will rally again.

# Hello my name affan. I had such a productive day. The only issue was that the stocks dropped a bunch. After hours, it went back up. Hopefully tomorrow they will rally again.

# C:\Users\affan\Desktop\SchoolHomework>lab12q2.py
# Enter your sentence: hello.affan

# Hello. Affan.

# C:\Users\affan\Desktop\SchoolHomework>lab12q2.py
# Enter your sentence: hello my name is affan. i dont know how to code

# Hello my name is affan. I dont know how to code.

# C:\Users\affan\Desktop\SchoolHomework>lab12q2.py
# Enter your sentence: python cis 1400

# Python cis 1400.
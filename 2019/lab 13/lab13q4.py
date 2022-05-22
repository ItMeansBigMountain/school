def main():
    user_input = int(input('Please enter number you would like to amplify?> '))
    amplify = _amplify(user_input)
    print(amplify)

def _amplify(user_input):
    counted = 0
    while user_input > 0:
       counted =  counted + user_input
       user_input= user_input -  1
    return counted

main()


# Output

# C:\Users\affan\Desktop\SchoolHomework>lab13q4.py
# Please enter number you would like to amplify?> 25
# 325

# C:\Users\affan\Desktop\SchoolHomework>lab13q4.py
# Please enter number you would like to amplify?> 48
# 1176


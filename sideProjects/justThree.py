import random


print(
    """
    Welcome!
        Score two in to end the program!
        WRONG ANSWERS WILL PENTALIZE YOU   
    
    good luck.
    """
)




correct = 0
def game( correct ):
    secret = random.randint(0,1)
    print(f"SCORE: {correct}")
    user_guess = input("Please choose true or false: ").lower()
    if secret == 1 and user_guess.startswith("t"):
        print("point!")
        correct += 1
    elif secret == 0 and user_guess.startswith("f"):
        print("point!")
        correct += 1
    else:
        game(correct)
        correct -= 1

    if correct < 2:
        game(correct)



game(correct=correct)
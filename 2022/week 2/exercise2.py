import random



secret = random.randint(1,1000)

def guessing_game():
    global secret
    guess = int(input("Please guess a whole number between 1 - 1000: "))
    while guess != secret:
        if guess < secret:
            print("\nToo low!")
            guess = int(input("Please guess a whole number between 1 - 1000: "))
        elif guess > secret:
            print("\nToo high!")
            guess = int(input("Please guess a whole number between 1 - 1000: "))
    print("\n\nCongratulations!\n\n")

def main():
    running = True
    while running:
        guessing_game()
        end_game = input("Would you like to play again? y/n : ")
        if end_game[0].lower() == 'n':
            running = False






if __name__ == "__main__":
    main()

#######################################################
# Class:      CIS-1400
# Assignment: Week 15
# File:       programming project.py
# Purpose:    TicTacToe
#######################################################

print('\n**  Osama Chmaout **\n') #Display author's name

def main():
    endgame = 'no'
    while endgame == 'no':

        print('\nWelcome to our python game!')

        print('1 - Play game!')
        print('2 - View Game History!')
        print('3 - Search player history by date (format as : YYYY-MM-DD)')
        print('4 - Sort history by money earned by lowest payout')
        try:
            option = int(input('Please enter an option: '))
        except:
            print('\nERROR: User input is not a number... please input one of the options.')
            print('Resetting app...')
            main()

        if option == 1:
            import random

            player1_name = input('PLAYER ONE -- Please enter name for PLAYER 1: ')
            while player1_name == "" or any(str.isdigit(c) for c in player1_name):
                print("\nERROR: Player name cannot contain numbers.")
                player1_name = input('PLAYER ONE -- Please enter name for PLAYER 1: ')

            player2_name = input('PLAYER TWO -- Please enter name for PLAYER 2: ')
            while player2_name == "" or any(str.isdigit(c) for c in player2_name):
                print("\nERROR: Player name cannot contain numbers.")
                player2_name = input('PLAYER TWO -- Please enter name for PLAYER 2: ')

            print("\n The rules are simple! Please dont look at opponent's input!")
            print('We are playing Rock, Paper, Scissors!\n')

            games = best_of()

            player1_Wins = []
            player2_Wins = []
            p1_winner_earnings = 0
            p2_winner_earnings = 0


            while 0 < int(games):
                games -= 1
                print('\nPlayer One!')
                player1 = get_decision()
                print('\nPlayer Two!')
                player2 = get_decision()
            
                winner =  evaluate(player1,player2)
                if winner == 0:
                    games += 1
                    print('\nTie game, rematch!')
                    player1_Wins.append('TIE')
                    player2_Wins.append('TIE')
                elif winner == 1:
                    print('\nPlayer 1 wins!')
                    player1_Wins.append('WIN')
                    player2_Wins.append('LOSS')
                    p1_winner_earnings += random.randint(10,99)
                    print('Player one wins: $'+ str(p1_winner_earnings))
                elif winner == 2:
                    print('\nPlayer 2 wins!')
                    player1_Wins.append('LOSS')
                    player2_Wins.append('WIN')
                    p2_winner_earnings += random.randint(10,99)
                    print('Player two wins: $'+ str(p2_winner_earnings))

            check = check_winner(player1_Wins, player2_Wins, p1_winner_earnings, p2_winner_earnings)

            write(player1_Wins, player2_Wins , check, player1_name, player2_name)

        elif option == 2:
            try:
                read()
            except:
                print('\nERROR: No game history, Restting App')
                main()
    
        elif option == 3:
            search()
    
        elif option == 4:
            sort_by_earnings()
    
        else:
            print('\nERROR: Please choose one of the options above...')
            main()

        endgame = input('Do you want to end the program ("yes" / "no") ')
        if endgame == 'n':
            endgame = 'no'


def best_of():
    print('\nChoose match winning setting!')
    print('One game - 1')
    print('Two out of Three - 2')
    print('Three out of Five - 3')
    try:
        game = int(input('Please choose an option! '))
    except:
        print('\nERROR: option has to be a number')
        game = int(input('Please choose an option! '))
    nums = [1,2,3]
    while game not in nums:
        print('ERROR: Please choose one of the options')
        game = int(input('Please choose an option! '))

    if game == 1:
        pass
    elif game == 2:
        game = 3
    elif game == 3:
        game = 5
    return game

def get_decision():
    print('ROCK - 1')
    print('PAPER - 2')
    print('SCISSORS - 3')

    try:
        decision = int(input('Please choose an option! '))
    except:
        print('ERROR: Please choose one of the options')
        decision = int(input('Please choose an option! '))
    nums = [1,2,3]
    while decision not in nums:
        print('ERROR: Please choose one of the options')
        decision = int(input('Please choose an option! '))

    return decision

def evaluate(player1, player2):
    if player1 == 1 and player2 == 1:
        winner = 0
    elif player1 == 1 and player2 == 2:
        winner = 2
    elif player1 == 1 and player2 == 3:
        winner = 1

    elif player1 == 2 and player2 == 1:
        winner = 1
    elif player1 == 2 and player2 == 2:
        winner = 0
    elif player1 == 2 and player2 == 3:
        winner = 2

    elif player1 == 3 and player2 == 1:
        winner = 2
    elif player1 == 3 and player2 == 2:
        winner = 1
    elif player1 == 3 and player2 == 3:
        winner = 0

    else:
        print('Not a valid entry')

    return winner

def check_winner(player1_Wins, player2_Wins, p1_winner_earnings, p2_winner_earnings):
    player1Count = 0
    player2Count = 0

    for x in player1_Wins:
        if x == 'WIN':
            player1Count+=1
        else:
            pass
   

    for x in player2_Wins:
        if x == 'WIN':
            player2Count+=1
        else:
            pass
   
    if player1Count > player2Count:
        return 'PLAYER ONE WON: $' + str(p1_winner_earnings)
    else:
        return 'PLAYER TWO WON: $' + str(p2_winner_earnings)

def write(player1_Wins, player2_Wins , check, player1_name, player2_name):
    from time import gmtime, strftime

    f = open("RockPaperScissorsData.txt", "a")
    f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    f.write('\n')
    f.write(player1_name)
    f.write('\n')
    f.write(str(player1_Wins))
    f.write('\n')
    f.write(player2_name)
    f.write('\n')
    f.write(str(player2_Wins))
    f.write('\n')
    f.write(check)
    f.write('\n')
    f.write('-------------------------------------------\n')
    f.write('\n')
    f.close()

def read():
    f = open("RockPaperScissorsData.txt", "r")
    print('\n\nGAME HISTORY')
    print(f.read())
    f.close()

def search():

    arr = []

    try:
        f = open("RockPaperScissorsData.txt", "r")
        user_search = input('Please enter date (format as : YYYY-MM-DD): ')

        for x in f:
            arr.append(x)

        print('\n\nSearch results\n')
        for x in range(0,len(arr)):
            if user_search in arr[x]:
                print(arr[x].replace('\n',''))
                print(arr[x+1].replace('\n',''))
                print(arr[x+2].replace('\n',''))
                print(arr[x+3].replace('\n',''))
                print(arr[x+4].replace('\n',''))
                print(arr[x+5].replace('\n','') ,'\n')
            elif user_search not in arr[x]:
                pass

        f.close()
    
    except:
        print('\nERROR: No game history')
        print('RESETTING APP')
        main()

def sort_by_earnings():
    try:

        arr = []

        user_search = '$'

        f = open("RockPaperScissorsData.txt", "r")

        for x in f:
            arr.append(x)

        searchArr = []
        for x in range(0,len(arr)):
            if user_search in arr[x]:
                searchArr.append(arr[x].replace('\n',''))

        final = []
        for x in range(0,len(searchArr)):
            money_string = searchArr[x][-2] + searchArr[x][-1]
            final.append(int(money_string))

        # BUBBLE Sort
        n = len(final)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if final[j] > final[j+1] :
                    final[j], final[j+1] = final[j+1], final[j]


        print('\n\nSORTED GAME HISTORY FROM LOWEST EARNINGS TO HIGHEST\n')
        for x in range(len(final)):
            for y in range(len(arr)):
                if str(final[x]) in str(arr[y]):
                    print(arr[y-5].replace('\n',''))
                    print(arr[y-4].replace('\n',''))
                    print(arr[y-3].replace('\n',''))
                    print(arr[y-2].replace('\n',''))
                    print(arr[y-1].replace('\n',''))
                    print(arr[y].replace('\n',''))
                    print(arr[y+1].replace('\n',''))
                    print()

    except:
        print('\nERROR: No game history')
        print('RESETTING APP')
        main()



    f.close()

# call main
main()

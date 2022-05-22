def writefile():
    howmany = input('How many players played?: ')
    while True: #validation to check if howmany is int
        try:
            howmany = int(howmany)
            break
        except:
            print("You have to type a numerical value")
            howmany = input('How many players played?: ')

    players = []
    scores = []
    for x in range(0,howmany):
        print(x+1)
        
        playerName = input("Please enter player's NAME: ")
        while playerName.isdigit():#validation to check if playerName is alphabet Char
            print("ERROR: Please input a name...  I'm sure human names are not numbers.")
            playerName = input("Please enter player's NAME: ")
        players.append(playerName)

        playerScore = input("Please enter player's SCORE: ")
        while True: #validation to check if playerScore is int
            try:
                playerScore = int(playerScore)
                break
            except:
                print("You have to type a numerical value")
                playerScore = input("Please enter player's SCORE: ")
        scores.append(playerScore)

    ScoreSheet = open('ScoreSheet.txt' , 'w') #WRITING INTO txt FILE
    ScoreSheet.write('Player --------- Score\n')
    ScoreSheet.write('-----------------------\n\n')
    for x in range(len(players)):
        ScoreSheet.write("%s --------- %s\n" % (players[x], scores[x]))
    ScoreSheet.close()

def readfile():
    ScoreSheet = open('ScoreSheet.txt' , 'r') #READING txt FILE
    print('\n', str(ScoreSheet.read()))
    ScoreSheet.close()


def main():
    writefile()
    readfile()

main()


# OUTPUT    (validations are shown to check if input is an integer or string. Shown two different ways in code [try method works for int check because its running an error if alpha letter, isdigit() method checks to make sure the name is not purley numeric])

# C:\Users\affan\Desktop\SchoolHomework\lab10>golfScoreWrite.py
# How many players played?: affan
# You have to type a numerical value
# How many players played?: 3
# 1
# Please enter player's NAME: affan1
# Please enter player's SCORE: affan2
# You have to type a numerical value
# Please enter player's SCORE: 100
# 2
# Please enter player's NAME: 1College of dupage
# Please enter player's SCORE: 366a
# You have to type a numerical value
# Please enter player's SCORE: 98
# 3
# Please enter player's NAME: 24
# ERROR: Please input a name...  I'm sure human names are not numbers.
# Please enter player's NAME: carona virus
# Please enter player's SCORE: 999

#  Player --------- Score
# -----------------------

# affan1 --------- 100
# 1College of dupage --------- 98
# carona virus --------- 999
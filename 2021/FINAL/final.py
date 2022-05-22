from Player import *
from Enemy import *

import time
import random


'''
PROCEDURE

# each level will spawn blocks and you will freeze. 
# once all have spawned they shoot and you dodge.

... will run game if ran directly

'''




def hit(obj : Enemy, player:Player):
    # print(obj.getX() , player.getX())
    if obj.getX() in range( player.getX()-20 , player.getX() + 20 , 1  )  and obj.getY() in range( player.getY()-20 , player.getY() + 20 , 1  ) :
    # if obj.getX() == player.getX() and obj.getY() == player.getY():
        return True
    return False






# gets players direction
def getDirection(win:GraphWin, currentDirection):
    key = win.checkKey().lower()
    if key == "up":
        return "N"
    elif key == "down":
        return "S"
    elif key == "right":
        return "E"
    elif key == "left":
        return "W"
    else:
        return currentDirection






def spawnEnemies(win , amount):
    all_enemies = [  ]
    h_enemy = False
    # spawn enemies
    for x in range(  amount )  :

        # tecnique for random placement
        # choose random number to 100 and see what side its on (cant be 50)
        randy = random.randint(0,101)
        if randy > 50 :
            h_enemy = True
        elif randy < 50:
            h_enemy = False
        else:
            pass
        
        if h_enemy:
            enemy = Horizontal(win)
            all_enemies.append(enemy)
        else:
            enemy = Vertical(win)
            all_enemies.append(enemy)


    return all_enemies



def greeting():
    print("Made by Affan Fareed")
    print("Final project")
    for x in range(3):
        time.sleep(1)
        print("")
    easy = input("\nwould you like to play this game on hard mode? Y/n  :  ")
    if easy.lower().startswith("y"):
        print("cool!")
        return False , easy
    else:
        print("lame...")
        return True , easy




def playerBoundries(height , width , player : Player):
    # x
    if player.getX() >= width-20:
        return (True , "R")
    elif player.getX() <= 0:
        return (True , "L")
    
    # y
    if player.getY() >= height-20:
        return (True , "T")
    elif player.getY() <= 0:
        return (True , "B")

    return (False , "")




# MAIN GAME LOOP
if __name__ == '__main__':
    # INTRO
    easy , debug = greeting()




    # CHANGE SCREEN HEIGHT AND WIDTH IN ENEMY.PY AS WELL inside of the enemy object
    height = 600
    width = 600 
    


    win= GraphWin("Affan Fareed's impossible game", height, width)

    
    
    # player init
    player = Player(200, 300)
    player.draw(win)
    score = 0

    # enemy init
    easyMode_amount = 2
    all_enemies = spawnEnemies(win  ,  easyMode_amount  )
    

    # player lives set up  
    if easy:
        player.lives = 10
    else:
        player.lives = 50

    # play game as intended
    if debug.startswith("debug"):
        player.lives = 99999999999999999999
        if len(debug.split(" ")) > 1:
            easy = False
        else:
            easy = True


    # spawn timer
    timer = 0.0


    while not win.closed:

        # Check if player LOST
        if player.lives <= 0:
            win.setBackground("Red")
            print("\nSCORE:" , "Final score : " + str(round(score))  )
            time.sleep(5)
            exit()

        # handle player hitting the boundry
        collision = playerBoundries(height , width , player)
        if collision[0]:
            if collision[1] == "R" or collision[1] == "L":
                player.wallX(collision[1] , width)
            elif collision[1] == "T" or  collision[1] == "B":
                player.wallY(collision[1] , height)

        #NOTE added a try statement in graphics.py line 451 
        # so that we do not get an error when we interact with intro menu

        # player key stroke listener 
        direction = getDirection(win, player.getDirection())
        player.move(direction)


        # MOVING THE ENEMIES USING graphics.py --- polymorph
        for enemy in all_enemies:
            enemy.move(win)
            # collision detection
            if hit(enemy  ,  player):
                player.lives -= 1
                print(f"Lives left: {player.lives}")



        # change color of player
        color = "#"
        for x in range(0, 6 , 1):
            color += str(random.randint(0,9))
        player.body.setFill(color)

        

        # SPAWNING ENEMIES with time condition
        if timer > random.randint(1,3) :
            # RESET TIMER
            # DISPLAY AMOUNT ON ENEMIES
            # EXPONTIALLY INCREASE AMOUNT OF ENEMIES 
            # SPAWN RATE TIMER DECREASES
            # REACTION SPEED TIMER DECREASES
            timer = 0.0
            # print(f"{Enemy(win)}")

            if easy:
                #easy mode
                all_enemies +=   spawnEnemies(win ,  easyMode_amount ) 
            else:
                #hard mode
                all_enemies  +=   spawnEnemies(win  ,  Enemy(win).lvl  )  


            easyMode_amount += 1



        # game level progression math
        time.sleep(.1)
        timer += .1
        score += .1


        


        



    win.getMouse()
    win.close()
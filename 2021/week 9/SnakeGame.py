from Snake import *
from Mouse import *
from Powerup import *

import time
import random

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

def isEaten(obj, snake:Snake):
    bodyParts = snake.getParts()
    if obj.getX() == bodyParts[0].getX() and obj.getY() == bodyParts[0].getY():
        return True
    return False


def main():
    win = GraphWin("Snake Game", 600, 600)
    
    snake = Snake(300, 400)
    mouse = Mouse(win)
    pw = PowerUp(win)

    snake.draw(win)
    mouse.drawMouse(win)
    pw.drawpower_up_obj(win)

    while snake.alive:

        # check if mouse was eaten
        if isEaten(mouse, snake):
            mouse.eaten(snake, win)
            snake.appendBody(win)
            print(f"{mouse.miceEaten}")


        # check if powerup was eaten
        if isEaten(pw, snake):
            pw.eaten(snake, mouse ,  win)

            # checking for what color the powerup was
            if pw.collected == "Purple":
                mouse.miceEaten += 2
                print(f"{mouse.miceEaten}")
            elif pw.collected == "Magenta":
                mouse.miceEaten += random.randint(-3 , 5)
                print(f"mystery! -- {mouse.miceEaten}")
            elif pw.collected == "Red":
                count = 0
                i = 0
                while count < random.randint(25 , 100):
                    win.setBackground(pw.colors[i])
                    time.sleep(0.1111111)
                    count += 1
                    i += 1
                    if i > len(pw.colors)-1 :
                        i = 0
                    
                win.close()



        # get the direction of the player's object 0
        direction = getDirection(win, snake.getDirection())

        # get user input
        snake.move(direction, win)

        time.sleep(.1)


if __name__ == '__main__':
    main()
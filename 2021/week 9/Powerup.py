
from Mouse import *
from Snake import *
import random


class PowerUp(object):
    colors = [
        "Red",
        'Purple',
        "Magenta"
    ]

    current = None
    collected = None


    def __init__(self, win:GraphWin):
        self.__x = random.randrange(0, win.getWidth() - 20, 20)
        self.__y = random.randrange(0, win.getHeight() - 20, 20)
        self.power_up_obj = Rectangle(Point(self.__x, self.__y), Point(self.__x + 20, self.__y + 20))

    def __str__(self):
        return f"power_up_obj Location ({self.__x}, {self.__y})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def drawpower_up_obj(self, win: GraphWin):
        randy = random.randint(0,len(self.colors)-1)
        self.current = self.colors[randy]
        self.power_up_obj.setFill(self.current)
        self.power_up_obj.draw(win)

    def goodLocation(self, x, y, snake:Snake , mouse:Mouse):
        for part in snake.getParts():
            if part.getX() == x and part.getY() == y:
                return False
        
        if mouse.getX() == x and mouse.getY() == y:
            return False
        return True

    def eaten(self, snake:Snake, mouse:Mouse ,  win:GraphWin ):
        # Mouse.miceEaten += 1
        newX = random.randrange(0, win.getWidth() - 20, 20)
        newY = random.randrange(0, win.getHeight() - 20 , 20)
        while not self.goodLocation(newX, newY, snake , mouse):
            newX = random.randrange(0, win.getWidth() - 20, 20)
            newY = random.randrange(0, win.getHeight() - 20, 20)
        dx = newX - self.__x
        dy = newY - self.__y

        # set new attributes
        randy = random.randint(0,len(self.colors) - 1)
        self.collected = self.current
        self.current = self.colors[randy]
        self.power_up_obj.setFill(self.current)
        
        self.power_up_obj.move(dx, dy)
        self.__x = newX
        self.__y = newY








if __name__ == '__main__':
    win = GraphWin("power_up_obj Test", 600, 600)
    power_up_obj = powerup(win)
    snake = Snake(300, 400)
    snake.draw(win)
    power_up_obj.drawpower_up_obj(win)
    while not win.closed:
        win.getpower_up_obj()
        power_up_obj.eaten(snake, mouse , win)
        print(power_up_obj)






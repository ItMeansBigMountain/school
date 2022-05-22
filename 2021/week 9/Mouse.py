
from Snake import *
import random

class Mouse(object):

    miceEaten = 0

    def __init__(self, win:GraphWin):
        self.__x = random.randrange(0, win.getWidth() - 20, 20)
        self.__y = random.randrange(0, win.getHeight() - 20, 20)
        self.mouse = Rectangle(Point(self.__x, self.__y), Point(self.__x + 20, self.__y + 20))

    def __str__(self):
        return f"Mouse Location ({self.__x}, {self.__y})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def drawMouse(self, win: GraphWin):
        self.mouse.setFill("Blue")
        self.mouse.draw(win)

    def goodLocation(self, x, y, snake:Snake):
        for part in snake.getParts():
            if part.getX() == x and part.getY() == y:
                return False
        return True

    def eaten(self, snake:Snake, win:GraphWin):
        self.miceEaten += 1
        newX = random.randrange(0, win.getWidth() - 20, 20)
        newY = random.randrange(0, win.getHeight() - 20 , 20)
        while not self.goodLocation(newX, newY, snake):
            newX = random.randrange(0, win.getWidth() - 20, 20)
            newY = random.randrange(0, win.getHeight() - 20, 20)
        dx = newX - self.__x
        dy = newY - self.__y
        self.mouse.move(dx, dy)
        self.__x = newX
        self.__y = newY


if __name__ == '__main__':
    win = GraphWin("Mouse Test", 600, 600)
    mouse = Mouse(win)
    snake = Snake(300, 400)
    snake.draw(win)
    mouse.drawMouse(win)
    while not win.closed:
        win.getMouse()
        mouse.eaten(snake, win)
        print(mouse)

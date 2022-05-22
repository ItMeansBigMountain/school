
from BodyPart import *

class Snake(object):
    """Snake is based on a list of body parts"""

    def __init__(self, x, y, direction = "N"):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.alive = True
        self.__bodyParts = []  #List of body parts to build the snake
        self.__createBody() #function call to build head and all initial body parts

    def __createBody(self):
        head = BodyPart(self.__x, self.__y, color = color_rgb(255, 55, 0))
        self.__bodyParts.append(head)

        for i in range(1, 3):
            newPart = BodyPart(self.__x, self.__y + 20 * i)
            self.__bodyParts.append(newPart)

    def getDirection(self):
        return self.__direction

    def getParts(self):
        return self.__bodyParts

    def draw(self, win: GraphWin):
        for part in self.__bodyParts:
            part.draw(win)


    def move(self, direction, win:GraphWin):
        self.__direction = direction
        for i in range(len(self.__bodyParts) - 1 , 0, -1):
            self.__bodyParts[i].move(self.__bodyParts[i - 1].getDirection())
        self.__bodyParts[0].move(self.__direction)
        if self.detectCollision(win):
            self.alive = False

    def detectCollision(self, win:GraphWin):
        if self.__bodyParts[0].getX() < 0:
            return True
        elif self.__bodyParts[0].getX() >= win.getWidth():
            return True
        elif self.__bodyParts[0].getY() < 0:
            return True
        elif self.__bodyParts[0].getY() >= win.getHeight():
            return True

        for i in range(1, len(self.__bodyParts) ):
            if self.__bodyParts[0].getX() == self.__bodyParts[i].getX() \
                and self.__bodyParts[0].getY() == self.__bodyParts[i].getY():
                return True

        return False


    def appendBody(self, win:GraphWin):
        lastX = self.__bodyParts[-1].getX()
        lastY = self.__bodyParts[-1].getY()
        size = self.__bodyParts[-1].getSize()
        direction = self.__bodyParts[-1].getDirection()

        if direction == "N":
            newPart = BodyPart(lastX, lastY + size)
        elif direction == "S":
            newPart = BodyPart(lastX, lastY - size)
        elif direction == "E":
            newPart = BodyPart(lastX - size, lastY)
        else:
            newPart = BodyPart(lastX + size , lastY)

        newPart.draw(win)
        self.__bodyParts.append(newPart)




if __name__ == '__main__':
    win = GraphWin("Snake Test Window", 600, 600)
    snake = Snake(300, 400)
    snake.draw(win)
    counter = 0
    while snake.alive:
        direction = getDirection(win, snake.getDirection())
        snake.move(direction, win)
        counter += 1
        time.sleep(.1)
        if counter % 10 == 0:
            snake.appendBody(win)


    win.getMouse()
    win.close()
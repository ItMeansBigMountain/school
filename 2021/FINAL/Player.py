from graphics import *

class Player(object):

    def __init__(self, x, y, size = 20, color = color_rgb(153, 255, 51), direction = "N"):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__direction = direction
        self.color = color
        self.lives = 0
        self.body = Rectangle(Point(self.__x, self.__y),
                              Point(self.__x + self.__size, self.__y + self.__size))



    def wallX(self , side , width):
        if side == "R":
            self.body.move(-1 * self.__size, 0)
            self.__x -= self.__size
        elif side == "L":
            self.body.move(self.__size, 0)
            self.__x += self.__size

    def wallY(self, side , height):
        if side == "T":
            self.body.move(0, -1 * self.__size)
            self.__y -= self.__size
        elif side == "B":
            self.body.move(0, self.__size)
            self.__y += self.__size


    # return string instead of memory location
    def __str__(self):
        output = f"BP Location({self.__x}, {self.__y})"
        return output

    # retrive private variables outside the class
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getDirection(self):
        return self.__direction

    def getSize(self):
        return self.__size


    def draw(self, win:GraphWin):
        """Draw a body part"""
        self.body.setFill(self.color)
        self.body.draw(win)

    def move(self, direction):
        self.__direction = direction
        if self.__direction == "N":
            self.body.move(0, -1 * self.__size)
            self.__y -= self.__size
        elif self.__direction == "S":
            self.body.move(0, self.__size)
            self.__y += self.__size
        elif self.__direction == "W":
            self.body.move(-1 * self.__size, 0)
            self.__x -= self.__size
        else:
            self.body.move(self.__size, 0)
            self.__x += self.__size



def getDirection(win:GraphWin, currentDirection):
    """get a key from the directional arrows and translate it into a direction"""
    key = win.checkKey().lower()
    if key == "up":
        return "N"
    elif key == "down":
        return "S"
    elif key == "left":
        return "W"
    elif key == "right":
        return "E"
    else:
        return currentDirection




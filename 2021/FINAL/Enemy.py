from Player import *
import random

class Enemy(object):
    lvl = 1
    sides = [10 , 575]
    __size = 20
    ScreenWidth = 600
    ScreenHeigth = 600

    def __init__(self, win:GraphWin ):
        Enemy.lvl += 1

    def __str__(self):
        return f" Amount of Enemies : {Enemy.lvl}"

    def getSize(self):
        return self.__size





class Horizontal(Enemy):
    
    def __init__(self, win:GraphWin):
        super().__init__( win )
        self.__x = random.choice(super().sides)
        self.__y = random.randint(50 , 550)
        self.body = Rectangle(Point(self.__x, self.__y), Point(self.__x + super().getSize(), self.__y + super().getSize()))
        self.draw(win)

        if self.__x == super().sides[1] :
            self.direction = 'W'
        else:
            self.direction = ""



    def __str__(self):
        return f"Horizontal Enemy Location ({self.__x}, {self.__y})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


    def draw(self, win: GraphWin):
        self.body.setFill("Blue")
        self.body.draw(win)

    def goodLocation(self, x, y, player:Player):
        if player.getX() == x and part.getY() == y:
            return False
        else:
            return True


    def move(self , win:GraphWin):

        # if self.__x == super().sides[1] :
        #     self.direction = ""
        # else:
        #     self.direction = 'W'


        if self.direction == "N":
            self.body.move(0, -1 * super().getSize())
            self.__y -= super().getSize()
        elif self.direction == "S":
            self.body.move(0, super().getSize())
            self.__y += super().getSize()
        elif self.direction == "W":
            self.body.move(-1 * super().getSize(), 0)
            self.__x -= super().getSize()
        else:
            self.body.move(super().getSize(), 0)
            self.__x += super().getSize()



class Vertical(Enemy):
    
    def __init__(self, win:GraphWin):
        super().__init__( win )
        self.__x = random.randint(50 , 550)
        self.__y = random.choice(super().sides)
        self.body = Rectangle(Point(self.__x, self.__y), Point(self.__x + super().getSize(), self.__y + super().getSize()))
        self.draw(win)

        if self.__y == super().sides[0] :
            self.direction = "S"
        else:
            self.direction = 'N'



    def __str__(self):
        return f"Vertical Enemy Location ({self.__x}, {self.__y})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


    def draw(self, win: GraphWin):
        self.body.setFill("Blue")
        self.body.draw(win)

    def goodLocation(self, x, y, player:Player):
        if player.getX() == x and part.getY() == y:
            return False
        else:
            return True


    def move(self , win:GraphWin):

        # if self.__y == super().sides[0] :
        #     self.direction = "S"
        # else:
        #     self.direction = 'N'

        if self.direction == "N":
            self.body.move(0, -1 * super().getSize())
            self.__y -= super().getSize()
        elif self.direction == "S":
            self.body.move(0, super().getSize())
            self.__y += super().getSize()
        elif self.direction == "W":
            self.body.move(-1 * super().getSize(), 0)
            self.__x -= super().getSize()
        else:
            self.body.move(super().getSize(), 0)
            self.__x += super().getSize()

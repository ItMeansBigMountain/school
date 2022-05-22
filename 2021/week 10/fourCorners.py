from graphics import *
import time
import random

class RecursiveGraphic(object):
    
    def __init__(self, win: GraphWin):
        self.startWidth = 250
        self.startHeight = 200
        self.tlX = win.getWidth() // 2 - self.startWidth // 2
        self.tlY = win.getHeight() // 2 - self.startHeight // 2


    # DRAWING HELPER FUNCTIONS
    def drawSquare(self, tlX, tlY, thisWidth , thisHeight, win):
        square = Rectangle(Point(tlX, tlY), Point(tlX + thisWidth, tlY + thisHeight))
        square.setFill(self.randomColor())
        square.draw(win)

    def randomColor(self):
        color = "#"
        for i in range(0,6,1):
            color += str(random.randint(0,9))
        return color



    # RECURSIVE STRATEGY
    def drawRectangles(self, win):
        self.drawCenterRectangle(win)

        self.drawTopLeft( win )
        self.drawTopRight( win )
        self.drawBottomRight( win )
        self.drawBottomLeft( win )
        


    # SQUARE PLACEMENT
    def drawCenterRectangle(self, win):
        rect = Rectangle(Point(self.tlX, self.tlY), Point(self.tlX + self.startWidth, self.tlY + self.startHeight))
        rect.setFill("Black")
        rect.draw(win)

    def drawTopLeft(self,   win:GraphWin):
        self.startWidth = self.startWidth // 2
        self.startHeight = self.startHeight // 2
        newCenterX = self.tlX - (self.startWidth // 2)  
        newCenterY = self.tlY - (self.startHeight // 2)  
        self.tlX = newCenterX - self.startWidth // 2
        self.tlY = newCenterY - self.startHeight // 2
        self.drawSquare(self.tlX, self.tlY, self.startWidth,  self.startHeight, win)

        # RECURSION
        if self.startWidth > 3 and self.startHeight > 3   :
            print(  "drawTopLeft"  )
            time.sleep(0.025)
            self.drawTopRight( win)
            # self.drawBottomLeft( win)
            self.drawTopLeft( win)
            # # self.drawBottomRight( win)
        else:
            self.__init__(win)


    def drawTopRight(self,   win:GraphWin):
        self.startWidth = self.startWidth // 2
        self.startHeight = self.startHeight // 2
        newCenterX = self.tlX + (self.startWidth)  
        newCenterY = self.tlY - (self.startHeight // 2)  
        self.tlX = newCenterX + self.startWidth
        self.tlY = newCenterY - self.startHeight // 2
        self.drawSquare(self.tlX, self.tlY, self.startWidth,  self.startHeight, win)

        # RECURSION
        if self.startWidth > 3 and self.startHeight > 3   :
            print("drawTopRight")
            time.sleep(0.025)
            # self.drawBottomRight( win)
            # self.drawTopLeft( win)
            self.drawTopRight( win)
            # # self.drawBottomLeft( win)
        else:
            self.__init__(win)

    def drawBottomLeft(self,   win:GraphWin):
        self.startWidth = self.startWidth // 2
        self.startHeight = self.startHeight // 2
        newCenterX = self.tlX - (self.startWidth // 2)  
        newCenterY = self.tlY + self.startHeight  
        self.tlX = newCenterX - self.startWidth // 2
        self.tlY = newCenterY + self.startHeight
        self.drawSquare(self.tlX, self.tlY, self.startWidth,  self.startHeight, win)

        # RECURSION
        if self.startWidth > 3 and self.startHeight > 3   :
            print("drawBottomLeft")
            time.sleep(0.05)
            time.sleep(0.025)
            # self.drawTopLeft( win)
            # self.drawBottomRight( win)
            self.drawBottomLeft( win)
            # # self.drawTopRight( win)
        else:
            self.__init__(win)

    def drawBottomRight(self,   win:GraphWin):
        self.startWidth = self.startWidth // 2
        self.startHeight = self.startHeight // 2
        newCenterX = self.tlX + self.startWidth 
        newCenterY = self.tlY + self.startHeight  
        self.tlX = newCenterX + self.startWidth 
        self.tlY = newCenterY + self.startHeight
        self.drawSquare(self.tlX, self.tlY, self.startWidth,  self.startHeight, win)

        # RECURSION
        if self.startWidth > 3 and self.startHeight > 3   :
            print("drawBottomRight")
            time.sleep(0.025)
            # self.drawTopRight( win)
            # self.drawBottomLeft( win)
            # # self.drawTopLeft( win)
            self.drawBottomRight( win)
        else:
            self.__init__(win)




def main():
    win = GraphWin("Recursive Rectangles", 1000, 650)
    rg = RecursiveGraphic(win)
    rg.drawRectangles(win)
    win.getMouse()
    win.close()




if __name__ == '__main__':
    main()
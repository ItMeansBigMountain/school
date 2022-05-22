from graphics import *
import time
import random

# joyce helped with understanding that we were looking at recursive Quadrants built on the graph

# emily was the cute chem/physics/calc semester... yikes


class RecursiveGraphic(object):
    
    def __init__(self, win: GraphWin):
        self.startWidth = 250
        self.startHeight = 200
        self.tlX = win.getWidth() // 2 - self.startWidth // 2
        self.tlY = win.getHeight() // 2 - self.startHeight // 2
        self.threashold = 3



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
        height = self.startWidth
        width = self.startHeight

        self.drawCenterRectangle(win)

        self.drawTL(Point(self.tlX  , self.tlY ), width , height , win)
        self.drawTR(Point(self.tlX + (self.startWidth + (self.startWidth //2)) , self.tlY ), width , height , win)
        self.drawBR(Point(self.tlX + (self.startWidth + (self.startWidth //2)) , self.tlY + self.startHeight ) , width , height , win)
        self.drawBL(Point(self.tlX , self.tlY + self.startHeight ) , width , height , win)

    # SQUARE PLACEMENT
    def drawCenterRectangle(self, win): #center square
        rect = Rectangle(Point(self.tlX, self.tlY), Point(self.tlX + self.startWidth, self.tlY + self.startHeight))
        rect.setFill("Black")
        rect.draw(win)

    def drawTL(self , oldCorner: Point, oldHeight , oldWidth , win:GraphWin):
        # division math
        newX = oldCorner.getX() - (oldWidth//2)
        newY = oldCorner.getY() - (oldHeight//2)
        newCorner = Point(  newX , newY  )

        # draw shape
        rect = Rectangle( newCorner  , oldCorner )
        rect.setFill(self.randomColor())
        rect.draw(win)

        # RECURSION (calling the function is doing math)
        # time.sleep(.05)

        self.drawTR( Point(oldCorner.getX() + (oldWidth//4)  , newCorner.getY()   ) , oldHeight // 2 , oldWidth //2 , win)

        if oldHeight > self.threashold and oldWidth > self.threashold   :
            self.drawBL( Point(newCorner.getX()   , oldCorner.getY()   ) ,  oldHeight // 2 , oldWidth //2 , win)
            self.drawTL( newCorner , oldHeight // 2 , oldWidth //2 , win)
            
    def drawTR(self , oldCorner: Point, oldHeight , oldWidth , win:GraphWin):
        newX = oldCorner.getX() - (oldWidth//2)
        newY = oldCorner.getY() - (oldHeight//2)
        newCorner = Point(  newX , newY  )

        rect = Rectangle( newCorner  , oldCorner )
        rect.setFill(self.randomColor())
        rect.draw(win)

        # time.sleep(.05)

        # RECURSION ISSUE !!! THIS IS BOTTOM RIGHT AND ACTS AS TOP RIGHT
        self.drawBR(  Point( newCorner.getX()  + oldWidth // 2 +  ((oldWidth//2)*.5) , newCorner.getY()  + (oldHeight//2)    ) , oldHeight // 2 , oldWidth//2 , win)
        

        if oldHeight > self.threashold and oldWidth > self.threashold   :
            self.drawBR( Point( oldCorner.getX() + (oldWidth//4)    , newCorner.getY() - (oldHeight//4)  ) ,  oldHeight // 2 , oldWidth//2 , win)
            self.drawTL( Point( oldCorner.getX()    , newCorner.getY() - (oldHeight//4)  ) ,  oldHeight // 4 , oldWidth//4 , win)
            self.drawTR( newCorner ,  oldHeight // 2 , oldWidth//2 , win)
            
    def drawBL(self , oldCorner: Point, oldHeight , oldWidth , win:GraphWin):
        newX = oldCorner.getX() - (oldWidth//2)
        newY = oldCorner.getY() + (oldHeight//2)
        newCorner = Point(  newX , newY  )

        rect = Rectangle( newCorner  , oldCorner )
        rect.setFill(self.randomColor())
        rect.draw(win)

        # time.sleep(.05)
        # RECURSION
        self.drawTL( Point( newCorner.getX() , newCorner.getY() + oldHeight )  , oldHeight // 2 , oldWidth //2 , win)

        self.drawBR( Point( oldCorner.getX() + oldWidth//4  , oldCorner.getY() + (oldHeight//2)   ) , oldHeight // 2 , oldWidth//2 , win)
        if oldHeight > self.threashold and oldWidth > self.threashold   :
            self.drawBL( newCorner , oldHeight // 2 , oldWidth//2 , win)
            self.drawTL( Point( newCorner.getX()    , newCorner.getY() - (oldHeight//2)  ) ,  oldHeight // 2 , oldWidth//2 , win)

    def drawBR(self , oldCorner: Point, oldHeight , oldWidth , win:GraphWin):
        newX = oldCorner.getX() - (oldWidth//2)
        newY = oldCorner.getY() + (oldHeight//2)
        newCorner = Point(  newX , newY  )

        rect = Rectangle( newCorner  , oldCorner )
        rect.setFill(self.randomColor())
        rect.draw(win)

        # time.sleep(.05)
        # RECURSION
        

        if oldHeight > self.threashold and oldWidth > self.threashold   :
            self.drawBR(  Point( oldCorner.getX() + (oldWidth//4)  , oldCorner.getY()  + (oldHeight//2)    ) , oldHeight // 2 , oldWidth//2 , win)
            self.drawTR( Point( oldCorner.getX() + (oldWidth//4)  , oldCorner.getY()    ) , oldHeight // 2 , oldWidth//2 , win)
            self.drawBL( newCorner , oldHeight // 2 , oldWidth//2 , win)
        
        




def main():
    win = GraphWin("Recursive Rectangles", 1000, 650)
    rg = RecursiveGraphic(win)
    rg.drawRectangles(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
from graphics import *
import time

def drawSquare(tlx, tly, height , width, win):
    square = Rectangle(Point(tlx, tly), Point(tlx + width, tly + height))
    square.setFill("Black")
    square.draw(win)


def drawSquares(win:GraphWin):
    height = win.getHeight() // 3
    width = win.getWidth() // 3
    tlX = win.getWidth() // 4 - height // 4
    tlY = win.getHeight() // 4 - width // 4
    drawSquare(tlX, tlY, height , width, win) #draw center square

    drawTL(Point(win.getWidth() // 2, win.getHeight() // 2), height , width, win)
    drawTR(Point(win.getWidth() // 2, win.getHeight() // 2), height , width, win)
    drawBL(Point(win.getWidth() // 2, win.getHeight() // 2), height , width, win)
    drawBR(Point(win.getWidth() // 2, win.getHeight() // 2), height , width, win)


def drawTL(oldCenter: Point, height , width, win:GraphWin):
    thisHeight = height // 3
    thisWidth = width // 3
    newCenterX = oldCenter.getX() - ( width )
    newCenterY = oldCenter.getY() - ( height )
    tlx = newCenterX - thisWidth  
    tly = newCenterY - thisHeight  
    drawSquare(tlx, tly, thisHeight , thisWidth, win)
    if thisHeight > 3 or thisWidth > 3:
        drawTR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawTL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawBL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        # drawBR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)




def drawTR(oldCenter: Point, height , width, win:GraphWin):
    thisHeight = height // 3
    thisWidth = width // 3
    newCenterX = oldCenter.getX() + width // 4
    newCenterY = oldCenter.getY() - height
    tlx = newCenterX - thisWidth
    tly = newCenterY - thisHeight
    drawSquare(tlx, tly, thisHeight, thisWidth, win)

    if thisHeight > 3 or thisWidth > 3:
        drawTR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawTL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        # drawBL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawBR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)





def drawBL(oldCenter: Point, height , width, win:GraphWin):
    thisHeight = height // 3
    thisWidth = width // 3
    newCenterX = oldCenter.getX() - thisWidth * 3
    newCenterY = oldCenter.getY() + thisHeight 
    tlx = newCenterX - thisWidth 
    tly = newCenterY - thisHeight
    drawSquare(tlx, tly, thisHeight , thisWidth, win)

    if thisHeight > 3 or thisWidth > 3:
        # drawTR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawTL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawBL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawBR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)





def drawBR(oldCenter: Point, height , width, win:GraphWin):
    thisHeight = height // 3
    thisWidth = width // 3
    newCenterX = oldCenter.getX() + thisWidth //2
    newCenterY = oldCenter.getY() + thisHeight //2
    tlx = newCenterX - thisWidth
    tly = newCenterY - thisHeight
    drawSquare(tlx, tly, thisHeight , thisWidth, win)

    if thisHeight > 3 or thisWidth > 3:
        drawTR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        # drawTL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawBL(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)
        drawBR(Point(newCenterX, newCenterY), thisHeight , thisWidth, win)




def main():
    win = GraphWin("Triangle", 900, 900)
   # win.setBackground("Black")
    drawSquares(win)


    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
from graphics import *





class Shape:
    def __init__(self , numSides, shapeName, nameAnchor, messageAnchor ):
        self.__numSides = numSides
        self.__shapeName = shapeName
        self.__nameAnchor = nameAnchor
        self.__messageAnchor = messageAnchor

    def displayName(self , Window):
        t = Text(self.__nameAnchor, self.__shapeName)
        t.setTextColor('black')
        t.draw(Window)

    def displayNumSides(self , Window):
        t = Text(self.__messageAnchor, f"A {self.__shapeName} has {self.__numSides} sides.  ")
        t.setTextColor('black')
        t.draw(Window)







# children of superclass Shape
class Square(Shape):
    def __init__(self , nameAnchor, messageAnchor  ):
        Shape.__init__(self , 4 , "Square" ,  nameAnchor, messageAnchor   )

    def drawShape(self , Window):
        print("Square!")
        sq = Rectangle( Point(50,50), Point(250,250) )
        sq.setFill('black')
        sq.draw( Window )









class Ball(Shape):
    def __init__(self , nameAnchor, messageAnchor  ):
        Shape.__init__(self , 0 , "Ball" ,  nameAnchor, messageAnchor   )

    def drawShape(self , Window):
        print("circle!")
        cloud = Circle(  Point(450,150) , 100 )
        cloud.setFill( 'black' )
        cloud.draw(Window)









class Triangle(Shape):
    def __init__(self , nameAnchor, messageAnchor  ):
        Shape.__init__(self , 3 , "Triangle" ,  nameAnchor, messageAnchor   )

    def drawShape(self , Window):
        print("Three Angles!")
        # slant1 = Line(   Point( 150  ,  350  )   , Point( 250  ,  500  )  )   
        # slant2 = Line(   Point( 250  ,  500  )   , Point( 75  ,  500  )  )   
        # slant3 = Line(  Point( 75  ,  500  )   ,  Point( 150  ,  350  )  )   

        poly = Polygon(Point( 150  ,  350  ), Point( 250  ,  500  ) , Point( 75  ,  500  ))
        poly.setFill("black")
        poly.draw(Window)






class Octagon(Shape):
    def __init__(self , nameAnchor, messageAnchor  ):
        Shape.__init__(self , 8 , "Octagon" ,  nameAnchor, messageAnchor   )

    def drawShape(self , Window):
        print("Eight Sides!")

        poly = Polygon(
            Point( 425  ,  350  ),
            Point( 450  ,  350  ) ,
            Point( 500  ,  400  ),
            Point( 500  ,  450  ),
            Point( 450  ,  500  ) ,
            Point( 400  ,  500  ),
            Point( 350  ,  450  ),
            Point( 350  ,  400  ),
            Point( 400  ,  350  ),
        )
        poly.setFill("black")
        poly.draw(Window)
















def main():
    win = GraphWin("Shape Test", 600, 600)
    l1 = Line(Point(300, 0), Point(300, 600))
    l2 = Line(Point(0, 300), Point(600, 300))
    l1.draw(win)
    l2.draw(win)


    shapes = []
    shapes.append(   Square(Point(50, 20) , Point(100, 280))   )
    shapes.append(Ball(Point(350, 20), Point(400, 280))) 
    shapes.append(Triangle(Point(50, 320), Point(100, 570)))  
    shapes.append(Octagon(Point(350, 320), Point(400, 570))) 

    for shape in shapes:
        shape.displayName(win)
        shape.displayNumSides(win)
        shape.drawShape(win)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()



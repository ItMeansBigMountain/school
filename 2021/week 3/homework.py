##Program: House Functions
##Name: Affan Fareed
## Date: 9/21/2021
#-------------------------------------------------------------#





# NOTE importing graphics file....
from graphics import *

# NOTE importing time sleep functionality
from time import sleep

# NOTE importing rundom number generation functionality
from random import randint





def house_base(window):
    b = Rectangle(Point(100,300), Point(900,625))
    b.setFill('grey')
    b.draw(window)

def rooftop(window):
    r = Polygon(Point(100,300), Point(500,1), Point(900,300))
    r.setFill('grey')
    r.draw(window)

def door(window):
    # door
    d = Rectangle(Point(400,450), Point(600,625))
    d.setFill('black')

    # knob
    knob = Circle(Point(575,550), 10)
    knob.setFill('white')


    d.draw(window)
    knob.draw(window)

def window(window , x , y):
    d = Rectangle( x , y )
    d.setFill('light blue')

    # if you add a dot after variables, you see all the attribs in it.
    # we can replace half as it rolls through a calculatio
        # i did this because i didnt want to make a new variable
    # we get half of x and add it to x's real value


    # VERTICAL WINDOW LINE
    half =    (x.y.real / 4)   -31
    half = int(x.x.real + half ) 
    half_point = Point( half, int(y.y.real)  )
    VERTICAL = Line(   half_point  , Point(y.x.real - 50,  y.y.real-100  )  )   
    

    # HORIZONTAL WINDOW LINE
    HORIZONTAL = Line(  Point( x.x.real ,    x.y.real + 50  ) , Point(y.x.real ,  y.y.real - 50   )  )   
    

    # draw lines and rectangle
    d.draw(window)
    HORIZONTAL.draw(window)
    VERTICAL.draw(window)




def chimney(window):
    c = Rectangle(Point(100,625), Point(25,100))
    c.setFill('brown')
    c.draw(window)


def cloud( window ,  xp_threashhold , yp_threashold , black):
    # RANDOM PLACEMENT FOR SMOKE WITHIN THREASHOLDS
    xp = randint(  xp_threashhold ,  xp_threashhold + 5 )
    yp =  randint( yp_threashold ,   yp_threashold +50 )
    # ALTERNATING FROM WHITE AND BLACK CLOUD
    if black:
        cloud = Circle(Point(xp,yp), 50)
        cloud.setFill('black')
        cloud.draw(window)
        time.sleep(0.1)
        yp -= 10
        return False
    else:
        cloud = Circle(Point(xp,yp), 50)
        cloud.setFill('white')
        cloud.draw(window)
        time.sleep(0.1)
        yp -= 10
        return True




# YOU CAN FIT FUNCTIONS THAT BLIP OBJECTS ONTO THE PAGE WITHIN THE ANIMATION LOOP
# MAKE SURE THE BLIP FUNCTION HAS PARAMETERS THAT ALLOW IT'S PLACEMENT 
def animation(window , counter):
    
    # RESTRAINTS FOR THE SMOKE TO BLIP AROUND IN THE LOOP
    smoke_xp_threashhold = 50
    smoke_yp_threashold = 100

    # animation loop
    black = False
    while counter >= 0:

        # chimney smoke
        black = cloud( window,  smoke_xp_threashhold , smoke_yp_threashold , black)

        # loop duration iteration
        counter -= 1




def main(): 

    win = GraphWin("My House", 1000, 650)
    win.setBackground('light blue')

    # house base
    house_base(win)

    # rooftop
    rooftop(win)

    # door
    door(win)

    # left window
    x = Point(200, 325)
    y = Point(300, 425)
    window(win , x  , y  )

    # right window
    x = Point(600, 325)
    y = Point(700, 425)
    window(win , x  , y  )

    # chimney
    chimney(win)




    # animation loop
    animation(win , 50)




    # interaction with user
    t = Text(Point(500, 500), "Click to enter...")
    t.setTextColor('white')
    t.draw(win)

    #wait for user input
    win.getMouse()

    t = Text(Point(500, 600), "lol sorry... party's full")
    t.setTextColor('white')
    t.draw(win)

    t = Text(Point(500, 600), "lol sorry... party's full")
    t.setTextColor('white')
    t.draw(win)

    #wait for user input
    win.getMouse()


    t = Text(Point(750, 500), "Click here before I call the cops.")
    t.setTextColor('white')
    t.draw(win)


    #END PROGRAM
    win.getMouse()
    win.close()





































# ##Call To The Main
main()



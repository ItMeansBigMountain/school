class Car(object):
    def __init__(self, year , make , model):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__currentSpeed = float(0)


    def accelerate(self , speed) :
        self.__currentSpeed += float(speed)

    def brake(self) :
        self.__currentSpeed -= 5

    def __str__(self):
        return f"Year: {self.__year} \nMake: {self.__make}\nSpeed: {self.__currentSpeed}"








# carz = Car(2011 , "Honda" , "Civic")
# print(carz)


# carz.accelerate(10)
# print(carz)

# carz.brake()
# print(carz)


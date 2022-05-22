class Car():
    def __init__(self, YearModel, make):
        self.YearModel = YearModel
        self.make = make
        self.speed = 0

    def accessors(self):
        return '{} {}\t{} MHP'.format(self.make, self.YearModel, self.speed)

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0
        return self.speed

car1 = Car(2011,'Honda')



for x in range(5):
    print(car1.accelerate())

print('CAR CONDITION AFTER FIVE ACCELERATIONS: ')
print(car1.accessors())


for x in range(5):
    print(car1.brake())

print('CAR CONDITION AFTER FIVE BRAKES: ')
print(car1.accessors())


# C:\Users\affan\Desktop\SchoolHomework>lab14q2.py
# 5
# 10
# 15
# 20
# 25
# CAR CONDITION AFTER FIVE ACCELERATIONS:
# Honda 2011      25 MHP
# 20
# 15
# 10
# 5
# 0
# CAR CONDITION AFTER FIVE BRAKES:
# Honda 2011      0 MHP

# C:\Users\affan\Desktop\SchoolHomework>



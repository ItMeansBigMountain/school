print("Affan\nFareed")
import random
import math
import time

#input
milesDriven = (float(input('Enter Miles Driven: ')))
gallonsUsed = (float(input('Enter Gallons Used: ')))
#processing
mpg = milesDriven / gallonsUsed
#output
print('your miles per gallon is '+ format(mpg, '.1f') +' Miles Per Gallon!\n')
#PROGRAM OUTPUT

#Affan
#Fareed
#Enter Miles Driven: 250
#Enter Gallons Used: 10
##your miles per gallon is 25.0 Miles Per Gallon!



money = math.floor((random.random() * 10000))
dice_1= int(random.randint(1,7))
dice_2= int(random.randint(1,7))
dice_3= int(random.randint(1,7))
dice_4= int(random.randint(1,7))

player = str(dice_1+dice_2)
computer = str(dice_3+dice_4)
emotionly = []
emotionly.append("Frantically")
emotionly.append("Dramatically")
emotionly.append("Confidentally")
emotionly.append("Unwillingly")
x = random.randint(0,3)
roll_feels = emotionly[x]
answer = input('wanna play dice? ')
print('too bad you didnt have a choice if you said', str(answer) +'...')
input('press enter to roll')
print('***you', roll_feels, 'roll the dice...***')
time.sleep(2)
print('YOU GOT')
print(dice_1)
print(dice_2)
print('TOTAL---> '+player)
print('\nI GOT')
print(dice_3)
print(dice_4)
print('TOTAL---> '+computer)
if int(player)>int(computer):
	print("\nyou won...")
	print('I guess I owe you', '$'+str(money)+'...')
else:
	print('\nYOU LOST')
	print('GIVE ME $'+str(money)+'!')


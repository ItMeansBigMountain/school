import random
import time 
import math


money = 1000
outcome = 0

def bet():
	wager = input('Place your bets!!!: ')
	while float(wager) < 0 or float(wager) > float(money):
		print('ERROR: Invalid Bet Placed...\n')
		wager = input('Place your bets!!!')
	return wager


def dice(wager, money):
	win = 0
	loss = 0
	dice_1= int(random.randint(1,7))
	dice_2= int(random.randint(1,7))
	dice_3= int(random.randint(1,7))
	dice_4= int(random.randint(1,7))

	player = str(dice_1+dice_2)
	computer = str(dice_3+dice_4)
	emotionly = ['Frantically','Dramatically','Confidentally','Unwillingly']
	x = random.randint(0,3)
	roll_feels = emotionly[x]
	input('press enter to roll')
	print('*** You', roll_feels, 'roll the dice... ***')
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
		wager = (math.floor((random.random() * int(wager)))) * 10
		win = int(wager) + money
		print('I guess I owe you', '$'+str(wager)+'...')
		return win
	else:
		print('\nYOU LOST')
		wager = (math.floor((random.random() * int(wager)))) * 10
		loss = money - int(wager)
		loss = loss * -1
		print('GIVE ME $'+str(wager)+'!')
		return loss




loop = 'a'
while loop != 'Q':

	wager = bet()
	outcome = dice(wager, money)
	money += int(outcome)

	print('\nYou have $' + str(money), '\n')

	if money > 0:
		loop = input('Play again? Press Q to quit...')
	else:
		loop = 'Q'



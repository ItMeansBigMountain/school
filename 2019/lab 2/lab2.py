import math

def tip():
	foodCost = float(input('Enter The cost of your meal: $'))
	tip = foodCost * .15
	tax = foodCost * .07
	total = foodCost + tip + tax

	print('\n-----RECEIPT-----\n')
	
	print('Meal cost: $' + str('{0:.2f}'.format(foodCost)))
	print('Tip (15%): $' +str('{0:.2f}'.format(tip)))
	print('Local Tax (7%): $' + str('{0:.2f}'.format(tax)))
	print('Total Cost: $' + str('{0:.2f}'.format(total)))
	print('-----------------')
	pass

def tempreture():
	# f = ((9/5)*c + 32)
	print('0 : Celcius ---> Fahrenheit')
	print('1 : Fahrenheit ---> Celcius')
	choice = float(input('Please choose Tempreture Scale Conversion: '))

	if choice == 0:
		celcius = float(input('Enter Tempreture in Celcius: '))
		fahrenheit = ((9/5) * celcius + 32)
		print(str('{0:.1f}'.format(fahrenheit))+'°F')
	elif choice == 1:
		fahrenheit = float(input('Enter Tempreture in Fahrenheit: '))
		celcius = ((fahrenheit-32) * (5/9))
		print(str('{0:.1f}'.format(celcius))+'°C')
	pass



print('0 : Tip and tax calculator...')
print('1 : Tempreture Scale Conversion...\n')
runModule = int(input('Please Choose Module To Run: '))
if runModule == 0:
	tip()
elif runModule == 1:
	tempreture()


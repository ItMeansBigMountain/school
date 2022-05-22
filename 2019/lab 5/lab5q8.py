#input
print('0 : Celcius ---> Fahrenheit')
print('1 : Fahrenheit ---> Celcius')
choice = float(input('Please choose Tempreture Scale Conversion: '))

#processing
if choice == 0:
	range_start = int(input('Enter the first tempreture in range of calculation (Celcius): '))
	range_end = int(input('Enter the last tempreture in range of calculation (Celcius): '))

	for celcius in range(range_start,range_end+1):
		fahrenheit = ((9/5) * celcius + 32)
		print( str(celcius) + '°C ---> ' +  str('{0:.1f}'.format(fahrenheit))+'°F')#output

elif choice == 1:
	range_start = int(input('Enter the first tempreture in range of calculation (Fahrenheit): '))
	range_end = int(input('Enter the last tempreture in range of calculation (Fahrenheit): '))

	for fahrenheit in range(range_start,range_end+1):
		celcius = ((fahrenheit-32) * (5/9))
		print(str(fahrenheit) + '°F ---> ' +str('{0:.1f}'.format(celcius))+'°C') #output



# OUTPUT

# C:\Users\Affan Fareed\Desktop\SchoolHomework>lab5q8.py
# 0 : Celcius ---> Fahrenheit
# 1 : Fahrenheit ---> Celcius
# Please choose Tempreture Scale Conversion: 0
# Enter the first tempreture in range of calculation (Celcius): -10
# Enter the last tempreture in range of calculation (Celcius): 10
# -10°C ---> 14.0°F
# -9°C ---> 15.8°F
# -8°C ---> 17.6°F
# -7°C ---> 19.4°F
# -6°C ---> 21.2°F
# -5°C ---> 23.0°F
# -4°C ---> 24.8°F
# -3°C ---> 26.6°F
# -2°C ---> 28.4°F
# -1°C ---> 30.2°F
# 0°C ---> 32.0°F
# 1°C ---> 33.8°F
# 2°C ---> 35.6°F
# 3°C ---> 37.4°F
# 4°C ---> 39.2°F
# 5°C ---> 41.0°F
# 6°C ---> 42.8°F
# 7°C ---> 44.6°F
# 8°C ---> 46.4°F
# 9°C ---> 48.2°F
# 10°C ---> 50.0°F

# C:\Users\Affan Fareed\Desktop\SchoolHomework>lab5q8.py
# 0 : Celcius ---> Fahrenheit
# 1 : Fahrenheit ---> Celcius
# Please choose Tempreture Scale Conversion: 0
# Enter the first tempreture in range of calculation (Celcius): 0
# Enter the last tempreture in range of calculation (Celcius): 20
# 0°C ---> 32.0°F
# 1°C ---> 33.8°F
# 2°C ---> 35.6°F
# 3°C ---> 37.4°F
# 4°C ---> 39.2°F
# 5°C ---> 41.0°F
# 6°C ---> 42.8°F
# 7°C ---> 44.6°F
# 8°C ---> 46.4°F
# 9°C ---> 48.2°F
# 10°C ---> 50.0°F
# 11°C ---> 51.8°F
# 12°C ---> 53.6°F
# 13°C ---> 55.4°F
# 14°C ---> 57.2°F
# 15°C ---> 59.0°F
# 16°C ---> 60.8°F
# 17°C ---> 62.6°F
# 18°C ---> 64.4°F
# 19°C ---> 66.2°F
# 20°C ---> 68.0°F

# C:\Users\Affan Fareed\Desktop\SchoolHomework>lab5q8.py
# 0 : Celcius ---> Fahrenheit
# 1 : Fahrenheit ---> Celcius
# Please choose Tempreture Scale Conversion: 0
# Enter the first tempreture in range of calculation (Celcius): 10
# Enter the last tempreture in range of calculation (Celcius): 35
# 10°C ---> 50.0°F
# 11°C ---> 51.8°F
# 12°C ---> 53.6°F
# 13°C ---> 55.4°F
# 14°C ---> 57.2°F
# 15°C ---> 59.0°F
# 16°C ---> 60.8°F
# 17°C ---> 62.6°F
# 18°C ---> 64.4°F
# 19°C ---> 66.2°F
# 20°C ---> 68.0°F
# 21°C ---> 69.8°F
# 22°C ---> 71.6°F
# 23°C ---> 73.4°F
# 24°C ---> 75.2°F
# 25°C ---> 77.0°F
# 26°C ---> 78.8°F
# 27°C ---> 80.6°F
# 28°C ---> 82.4°F
# 29°C ---> 84.2°F
# 30°C ---> 86.0°F
# 31°C ---> 87.8°F
# 32°C ---> 89.6°F
# 33°C ---> 91.4°F
# 34°C ---> 93.2°F
# 35°C ---> 95.0°F
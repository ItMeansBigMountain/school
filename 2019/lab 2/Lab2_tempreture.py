#input
print('0 : Celcius ---> Fahrenheit')
print('1 : Fahrenheit ---> Celcius')
choice = float(input('Please choose Tempreture Scale Conversion: '))

#processing
if choice == 0:
	celcius = float(input('Enter Tempreture in Celcius: ')) #input
	fahrenheit = ((9/5) * celcius + 32)
	print(str('{0:.1f}'.format(fahrenheit))+'°F')#output

elif choice == 1:
	fahrenheit = float(input('Enter Tempreture in Fahrenheit: ')) #input
	celcius = ((fahrenheit-32) * (5/9))
	print(str('{0:.1f}'.format(celcius))+'°C') #output


#PROGRAM OUTPUT

# 0 : Celcius ---> Fahrenheit
# 1 : Fahrenheit ---> Celcius
# Please choose Tempreture Scale Conversion: 0
# Enter Tempreture in Celcius: 32
# 89.6°F

# C:\Users\Affan Fareed\Desktop\SchoolHomework\lab_2_feb_3rd>Lab2_tempreture.py
# 0 : Celcius ---> Fahrenheit
# 1 : Fahrenheit ---> Celcius
# Please choose Tempreture Scale Conversion: 1
# Enter Tempreture in Fahrenheit: 32
# 0.0°C
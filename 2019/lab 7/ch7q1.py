
hours = float(input('How many hours did you work this week? \n'))
while hours < 0 or hours > 40:
	print("Invalid Hours Worked Try Again\n")
	hours = float(input('How many hours did you work this week? \n'))

payRate = float(input('What is your hourly pay? \n'+'$'))
while payRate < 7.50 or payRate > 18.25:
	print("Invalid Pay Rate Try Again\n")
	payRate = float(input('What is your hourly pay? \n'+'$'))

def calc():
	grossPay = hours * payRate
	print('Gross Pay: $'+ "{:.2f}".format(grossPay))

calc()

# OUTPUT
# C:\Users\Affan Fareed\Desktop\SchoolHomework>ch7q1.py

# How many hours did you work this week?
# -1
# Invalid Hours Worked Try Again

# How many hours did you work this week?
# 41
# Invalid Hours Worked Try Again

# How many hours did you work this week?
# 40
# What is your hourly pay?
# $7.49
# Invalid Pay Rate Try Again

# What is your hourly pay?
# $18.26
# Invalid Pay Rate Try Again

# What is your hourly pay?
# $7.50
# Gross Pay: $300.00
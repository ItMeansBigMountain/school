
deposit = int(input("Enter Deposit Value: $"))
while deposit < 0 or deposit > 100000:
	print("Invalid Deposit Amount Try Again")
	deposit = int(input("Enter Deposit Value: $"))


intrest_rate = int(input("Enter Intrest Rate Percentage: "))
while intrest_rate < 0 :
	print('Intrest rate cannot be negative... try again')
	intrest_rate = int(input("Enter Intrest Rate Percentage: "))


years = int(input("How Many Years Will You Keep Your Investment?: "))
while years < 0 :
	print('Year amount cannot be negative... try again')
	years = int(input("How Many Years Will You Keep Your Investment?: "))

intrest_rate /= 100
future_value = deposit * (1+ intrest_rate) ** years
print('you will gain $'+ format(future_value, ',.2f'))
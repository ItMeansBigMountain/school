#input
weight = float(input("Please specify how much weight your shipment is (POUNDS): "))

#processing
price = 0
rate = 0
if weight <= 2:
	rate = 1.1
	price = rate * weight
elif weight >= 3 and weight <= 6 :
	rate = 2.2
	price = rate * weight
elif weight >= 7 and weight <= 10 :
	rate = 3.70
	price = rate * weight
elif weight >= 11 :
	rate = 3.8
	price = rate * weight
	
	#display
print ('TOTAL SHIPPING CHARGE: $'+ '{0:.2f}'.format(price))

#Please specify how much weight your shipment is (POUNDS): 12.2
#TOTAL SHIPPING CHARGE: $46.36

#input
quantity = int(input("Please enter how many products you have bought: "))

#processing
prior_price = quantity * 99
discount_price = 0
if quantity < 10:
	discount_rate = 0
	discount_price = 0
elif quantity >= 10 and quantity <= 19:
	discount_rate = .2
	discount_price = prior_price * discount_rate
elif quantity >= 20 and quantity <= 49:
	discount_rate = .3
	discount_price = prior_price * discount_rate
elif quantity >= 50 and quantity <= 99:
	discount_rate = .4
	discount_price = prior_price * discount_rate
elif quantity >= 100:
	discount_rate = .5
	discount_price = prior_price * discount_rate
percentage = discount_rate * 100
total = prior_price - discount_price

#display
print("BEFORE DISCOUNT TOTAL: $"+ str('{0:.2f}'.format(prior_price)))
print("DISCOUNT RATE: "+ str(percentage) +"%")
print("DISCOUNT AMOUNT: $"+ str('{0:.2f}'.format(discount_price)))
print("TOTAL COST: $" + str('{0:.2f}'.format(total)))


#Please enter how many products you have bought: 22
#BEFORE DISCOUNT TOTAL: $2178.00
#DISCOUNT RATE: 30.0%
#DISCOUNT AMOUNT: $653.40
#TOTAL COST: $1524.60

#Please enter how many products you have bought: 57
#BEFORE DISCOUNT TOTAL: $5643.00
#DISCOUNT RATE: 40.0%
#DISCOUNT AMOUNT: $2257.20
#TOTAL COST: $3385.80

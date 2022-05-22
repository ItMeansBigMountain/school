#input
foodCost = float(input('Enter The cost of your meal: $'))

#processing
tip = foodCost * .15
tax = foodCost * .07
total = foodCost + tip + tax

#output
print('\n-----RECEIPT-----\n')

print('Meal cost: $' + str('{0:.2f}'.format(foodCost)))
print('Tip (15%): $' +str('{0:.2f}'.format(tip)))
print('Local Tax (7%): $' + str('{0:.2f}'.format(tax)))
print('Total Cost: $' + str('{0:.2f}'.format(total)))
print('-----------------')

#PROGRAM OUTPUT

# -----RECEIPT-----

# Meal cost: $50.63
# Tip (15%): $7.59
# Local Tax (7%): $3.54
# Total Cost: $61.77
# -----------------
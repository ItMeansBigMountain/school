
# gb has to be between 10 50 

# 4.44 per GigaBytes added to monthly contract when over
# monthly contract = 74.99

monthly = 74.99
gbRate = 4.44

gb_used = int(input('How many GigaBytes have you used?: '))
while gb_used < 10 or gb_used > 50:
	print('ERROR: Invalid entry : 10 - 50 GB')
	gb_used = int(input('How many GigaBytes have you used?: '))

gb_allowed = int(input('How many GB does your plan allowed? :'))
while gb_allowed < 0 or gb_allowed > 50:
	print('ERROR: Invalid entry : 0 - 50 GB')
	gb_allowed = int(input('How many GB does your plan allowed? :'))


if gb_allowed < gb_used:
	difference = gb_used - gb_allowed
	monthly += (gbRate * difference)

	print('\nYou went over your limit by: ' + str(difference))
	print('You have been billed: $' + str('{0:.2f}'.format(monthly)))

	print(str(gb_used) , 'GigaBytes Used')
	print(str(difference) , 'GigaBytes Over')
	print(str(gb_allowed) , 'GigaBytes Data Limit')



else:
	print('Your monthly bill was: $' + str(monthly))
	print(str(gb_used) , 'GigaBytes Used')
	print(str(gb_allowed) , 'GigaBytes Data Limit')

def check(accountNum,account_list):
	valid = False
	for x in account_list:
		if accountNum == x:
			valid = True
	return valid

def main():
	accountNum = int(input('Please enter an account number: '))
	account_list = [
		5658845,
		8080152,
		1005231,
		4520125,
		4562555,
		6545231,
		7895122,
		5552012,
		3852085,
		8777541,
		5050552,
		7576651,
		8451277,
		7825877,
		7881200,
		1302850,
		1250255,
		4581002
	]
	validity = check(accountNum, account_list)

	while validity == False:
		print('\nAccount is NOT VALID')
		accountNum = int(input('Please enter an account number: '))
		validity = check(accountNum, account_list)
		print(validity)

	if validity == True:
		print('\nAccount is VALID')


main()

# OUTPUT

# C:\Users\Affan Fareed\Desktop\SchoolHomework\lab8>lab8q5.py
# Please enter an account number: 99999999999

# Account is NOT VALID
# Please enter an account number: 5552012
# True

# Account is VALID

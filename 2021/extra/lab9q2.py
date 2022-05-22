alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

names = []
alpha_names = []
for x in range(0,5):
	input_name = str(input('Type in a name (Make sure the first letter is capital please): '))
	while input_name[0] not in alphabet:
		print('Invalid name input!')
		input_name = str(input('Type in a name: '))
	names.append(input_name)

for x in alphabet:
	for y in names:
		if y[0] == x:
			alpha_names.append(y)

print(alpha_names)
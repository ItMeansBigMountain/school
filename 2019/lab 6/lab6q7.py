howmany = int(input('\nHow many graded scores would you like to input?: '))

score_list = []
for x in range(1,howmany+1):
	print('\n',str(x))
	input_score = input('What was the score? (PERCENTAGE): ')
	score_list.append(input_score)


def calcAverage(score_list):
	score_sum = 0
	avg_count = int(len(score_list))

	grade_list=[]
	for x in score_list:
		score_sum += int(x)
		grade_to_append = determineGrade(x)
		grade_list.append(grade_to_append)
		
	average = score_sum / avg_count

	print('GRADES --> ', str(grade_list))
	print('FINAL GRADE: ',str(average)+'% <-- '+determineGrade(average)+'\n------------------------------------\n')
	pass

def determineGrade(score):
	if int(score) <= 59:
		grade = 'F'
	elif int(score) <= 69:
		grade = 'D'
	elif int(score) <= 79:
		grade = 'C'
	elif int(score) <= 89:
		grade = 'B'
	elif int(score) <= 100:
		grade = 'A'
	else:
		print('\n***Not A Valid Score on 100 Percent Scale***\n')
	return grade

print('\n------------------------------------\nSCORES --> ', str(score_list))
calcAverage(score_list)


# OUTPUT

# How many graded scores would you like to input?: 5

#  1
# What was the score? (PERCENTAGE): 100

#  2
# What was the score? (PERCENTAGE): 80

#  3
# What was the score? (PERCENTAGE): 70

#  4
# What was the score? (PERCENTAGE): 60

#  5
# What was the score? (PERCENTAGE): 50

# ------------------------------------
# SCORES -->  ['100', '80', '70', '60', '50']
# GRADES -->  ['A', 'B', 'C', 'D', 'F']
# FINAL GRADE:  72.0% <-- C
# ------------------------------------
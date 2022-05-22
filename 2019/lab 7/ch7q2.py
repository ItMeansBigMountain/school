# GLOBAL VARIABLES
section = [20,15,10]
section_limit = [300,500,200]
section_name = ['A' , 'B' , 'C']
tickets_sold = []
for x in range(0,len(section_name)): #USER INPUT to add to tickets sold arr
	print('\nSECTION:' +  str(section_name[x]))
	tickets_sold.append(float(input('How many tickets were sold in this section? \n')))
	while tickets_sold[x] > section_limit[x]:
		print("\nERROR: Section Capacity: "+ str(section_limit[x]) + " Reached... Please Try Again\n")
		tickets_sold[x] = float(input('How many tickets were sold in this section? \n'))

# FUNCTIONS
def main():
	results = []
	for i in range(0,len(tickets_sold)):
		print('----------------------')
		print('SECTION ' + section_name[i])
		income = tickets_sold[i] * section[i]
		income = "{:.2f}".format(income)
		results.append(income)
		print('$'+ str(income))

# ________________________________Functionality_______________________________________
print('\nTICKETS SOLD INCOME')
main()


# OUTPUT
# C:\Users\Affan Fareed\Desktop\SchoolHomework>ch7q2.py

# SECTION:A
# How many tickets were sold in this section?
# 301

# ERROR: Section Capacity: 300 Reached... Please Try Again

# How many tickets were sold in this section?
# 300

# SECTION:B
# How many tickets were sold in this section?
# 501

# ERROR: Section Capacity: 500 Reached... Please Try Again

# How many tickets were sold in this section?
# 500

# SECTION:C
# How many tickets were sold in this section?
# 201

# ERROR: Section Capacity: 200 Reached... Please Try Again

# How many tickets were sold in this section?
# 200

# TICKETS SOLD INCOME
# ----------------------
# SECTION A
# $6000.00
# ----------------------
# SECTION B
# $7500.00
# ----------------------
# SECTION C
# $2000.00
grades = [ 90 , 85   , 52  , 74 , 95 , 100 , 78   ]
minimum = grades[0]
maximum = grades[0]
string = ''
for i in range(  0  , len(grades)  , 1   ):
  indivisual = float(grades[i])
  string += f'{indivisual}%, '

   
  if minimum > indivisual:
    minimum = indivisual

  if maximum < indivisual:
    maximum = indivisual



# output
print('The current test scores are:')
print(  string[:-2] , '\n'  )

print( f"Lowest Score:  {int(minimum)}  "   )
print( f"Highest Score:  {int(maximum)}  "   )




# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework\week4>stage1.py
# The current test scores are:
# 90.0%, 85.0%, 52.0%, 74.0%, 95.0%, 100.0%, 78.0%

# Lowest Score:  52.0
# Highest Score:  100.0
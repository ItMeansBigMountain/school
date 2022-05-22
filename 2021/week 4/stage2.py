def dropLowest( grades ):
  minimum = grades[0]
  maximum = grades[0]
  for i in range(  0  , len(grades)  , 1   ):
    indivisual = float(grades[i]) 
    # Find Min here
    minimum = findMin(minimum , indivisual)
    # maximum
    if maximum < indivisual:
      maximum = indivisual

  # removes minimum from array 
  grades.remove(minimum)

  # call the display scores function
  displayScores(  grades,maximum,minimum  )





# find minimum from array 
def findMin(minimum, indivisual):
  if minimum > indivisual:
    minimum = indivisual
  return minimum 

  





def displayScores(grades, maximum , minimum ):
  print( F"Lowest Score: {int(minimum)}"   )
  print( F"Heighest Score: {int(maximum)} \n"   )

  # create current grades string...
  string = ''
  for i in range(  0  , len(grades)  , 1   ):
    indivisual = float(grades[i])
    string += f'{indivisual}%, '
  string = string[:-2] 
  
  print("After droping the test score. ")
  print("The current test scores are: ")
  print( string )











def main():
  grades = [ 90 , 85   , 52  , 74 , 95 , 100 , 78   ]
  
  # create current grades string...
  string = ''
  for i in range(  0  , len(grades)  , 1   ):
    indivisual = float(grades[i])
    string += f'{indivisual}%, '


  # print current grade string
  current = string[:-2] 
  print('The current test scores are:')
  print( current , '\n'  )


  # drop lowest item
  dropLowest(grades)





# calling main here
main()




# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework\week4>stage2.py
# The current test scores are:
# 90.0%, 85.0%, 52.0%, 74.0%, 95.0%, 100.0%, 78.0%

# Lowest Score: 52
# Heighest Score: 100

# After droping the test score.
# The current test scores are:
# 90.0%, 85.0%, 74.0%, 95.0%, 100.0%, 78.0%

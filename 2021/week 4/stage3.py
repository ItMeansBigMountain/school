def dropLowest( grades , current_avg):
  minimum = grades[0]
  maximum = grades[0]
  for i in range(  0  , len(grades)  , 1   ):
    indivisual = float(grades[i]) 
    # Find Min here
    minimum = findMin(minimum , indivisual)
    # maximum
    maximum = findMx(maximum , indivisual)

  # removes minimum from array 
  grades.remove(minimum)

  # gets final average 
  final_avg = getMean(grades)

  # call the display scores function
  displayScores(  grades,maximum,minimum ,final_avg  , current_avg)




def findMin(minimum, indivisual):
  if minimum > indivisual:
    minimum = indivisual
  return minimum 

def findMx(maximum, indivisual):
  if maximum < indivisual:
    maximum = indivisual
  return maximum 

def getMean(grades):
  total = 0
  for i in range(0,len(grades) , 1):
    total+= grades[i]
  return total / len(grades)





def displayScores(grades, maximum , minimum  ,  final_avg  , previous_avg):
  print( F"Lowest Score: {int(minimum)}"   )
  print( F"Heighest Score: {int(maximum)} \n{'Average: ' + previous_avg }\n"   )

  # create current grades string...
  string = ''
  for i in range(  0  , len(grades)  , 1   ):
    indivisual = float(grades[i])
    string += f'{indivisual}%, '
  string = string[:-2] 
  
  print("After droping the test score. ")
  print("The current test scores are: ")
  print( string )
  print( "Average: " + str(float(final_avg))    )
  

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
  # displays previous average 
  current_avg = str(float(getMean(grades))) 


  # drop lowest item && display final scores after dropping lowest
  dropLowest(grades , current_avg)





# calling main here
main()




# OUTPUT
# C:\Users\affan\Desktop\SchoolHomework\week4>stage3.py
# The current test scores are:
# 90.0%, 85.0%, 52.0%, 74.0%, 95.0%, 100.0%, 78.0%

# Lowest Score: 52
# Heighest Score: 100
# Average: 82.0

# After droping the test score.
# The current test scores are:
# 90.0%, 85.0%, 74.0%, 95.0%, 100.0%, 78.0%
# Average: 87.0
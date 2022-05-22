import pandas as pd
import numpy as np
import string
import random


"""
TODO 
    ask user for logic statment
        EX: (a and b) --> ~( c or b )

        



"""






# INIT variables  
alphabet = string.ascii_letters
alphabet = alphabet[:(len(alphabet)//2)]

variables_list = []


# USER INPUT & GENERATE VARIABLES
amount_of_variables = int(input("please enter how many variables you would like to work with: "))
counter = 0
multi_var = 1
for x in range(0, amount_of_variables ,1):
    if counter >= len(alphabet):
        counter = 0
        multi_var += 1
    variables_list.append( alphabet[counter] * multi_var  )
    counter += 1


# cardinal number calculation
number_of_rows = 2 ** len(variables_list)
widest_number = len(str(bin(number_of_rows - 1 )[2:]))


# getting binary representation of each true false outcome
truth_table = []
for i in range(number_of_rows):
    each_digit_bin = bin(i)[2:].zfill(widest_number)
    truth = list(map( lambda x : True if int(x) == 1 else False   , str(each_digit_bin)))
    truth_table.append( truth )



# PANDAS DataFrame
data_model = {}
for x in range(0 , widest_number , 1):
    data_model[variables_list[x]] = [value[x] for value in truth_table ]
df = pd.DataFrame(data_model)
print(df)




# # debug
# for x in truth_table:
#     print(x)


print("\n")
print(f"Cardinal Number: {number_of_rows}")

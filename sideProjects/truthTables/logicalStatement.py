import pandas as pd
import numpy as np
import string
import random


"""
TODO 
        WORKING
            EX: (a and b) > ~( c or b )
            EX: (a and b) and ( c or b )
            EX: (a or b) or (c)

        ERROR
            EX: (a or b) or c
            EX: ( (a and b) > ~( c or b ) ) or c

"""



# checking pairs
open_list = ["[","{","("]
close_list = ["]","}",")"]
brackets = None


# checking conjectives
and_symbols = ["and" , "&"]
or_symbols = ["or" , "|"]
negation_symbols = ["~" , "-"]
conditional_symbols = [">" , "-->" , "->"]
biconditional_symbols = [">" , "-->" , "->"]

logic_symbols = and_symbols + or_symbols + negation_symbols + conditional_symbols + biconditional_symbols


# truth table
variables_list = []





def check_pairs_identify_elements(myStr):
    elements = []
    between_brackets_start = None
    between_brackets_end = None
    # returns true & elements if even bracket pairs
    stack = []
    start = None
    end = None
    continued_str_index = len(myStr) -1
    for i in range(0,len(myStr),1):
        # start bracket
        if myStr[i] in open_list:
            start = i+1
            stack.append(myStr[i])
            # mark between brackets 
            if i > 0: between_brackets_end = i
        # end bracket
        elif myStr[i] in close_list:
            pos = close_list.index(myStr[i])
            if ((len(stack) > 0) and (open_list[pos] == stack[-1])):
                stack.pop()
                end = i
                between_brackets_start = i
            else:
                return False
        # identify elements
        if start and end:
            elements.append( myStr[start:end]  )
            start = None
            end = None
            continued_str_index = i
        if between_brackets_start and between_brackets_end:
            elements.append( myStr[between_brackets_start+1:between_brackets_end]  )
            between_brackets_start = None
            between_brackets_end = None
    
    # add rest of statement if more logic after last bracket
    if len(myStr[continued_str_index+1:]):
        elements.append(myStr[continued_str_index+1:])

    # validate accurate input
    if len(stack) == 0:
        if len(elements) > 0:
            brackets = True
            return elements
        else:
            brackets = False
            logic_statement = myStr.split()                
            return logic_statement
    else:
        return False



def solve( logic_statement , validated_elements , variables_list , df_index ):

    variable_truths = [ df.loc[df_index,value] for value in variables_list  ]
    # print(logic_statement)
    # print(variable_truths)
    # print(validated_elements)
    # print(variables_list)
    # print()




    elements = []
    start = None
    end = None
    between_brackets_start = None
    between_brackets_end = None
    continued_str_index = len(logic_statement) -1



    stack = []
    index_stack = []
    consolidated_statement = []
    for i in range(0,len(logic_statement),1):
        # start bracket
        if logic_statement[i] in open_list:
            stack.append(logic_statement[i])
            index_stack.append(i+1)
            # consolidated_statement.append(logic_statement[i])
            start = i+1
            if i > 0: between_brackets_end = i

        # end bracket
        elif logic_statement[i] in close_list:
            pos = close_list.index(logic_statement[i])
            if  len(stack) > 0 and (open_list[pos] == stack[-1]) :
                end = i
                between_brackets_start = i

                # solve bubble
                # bubble = true/false
                # string manipulated with bubble in there
                # logic_statement[:index_stack[-1]] + str(bubble) + logic_statement[i:]
                bubble = logic_statement[index_stack[-1]:i]
                bubble_arr = bubble.split()

                # identify inner bracket truth value
                truth_statement = ""
                for element in bubble_arr:
                    if element in variables_list:
                        truth_index = variables_list.index(element)
                        truth_statement += f"{variable_truths[truth_index]}"
                        # print( element , variable_truths[truth_index]   )
                    elif element in logic_symbols:
                        truth_statement += f" {element} "
                        # print(element)

                # SOLVE SUBSTRING
                truth_value = eval(truth_statement)
                consolidated_statement.append(truth_value)
                # print(truth_statement)
                # print( bubble  , " --> " , truth_value  )

                # remove from stack once found
                stack.pop()
                index_stack.pop()
            else:
                return False
            
        # identify elements
        if start and end:
            elements.append( logic_statement[start:end]  )
            start = None
            end = None
            continued_str_index = i
        if between_brackets_start and between_brackets_end:
            consolidated_statement.append(logic_statement[between_brackets_start+1:between_brackets_end])
            elements.append( logic_statement[between_brackets_start+1:between_brackets_end]  )
            between_brackets_start = None
            between_brackets_end = None
    
    # add rest of statement if more logic after last bracket
    if len(logic_statement[continued_str_index+1:]):
        elements.append(logic_statement[continued_str_index+1:])
    
    
    # validate accurate input
    if len(stack) == 0:
        consolidated_output = ""
        for x in consolidated_statement:
            consolidated_output += f"{x} "

        # CHECK NEGATIONS
        output_arr = consolidated_output.split()
        negation_position = []
        for x in range(len(output_arr)):
            if not (output_arr[x] == True or output_arr[x] == False):
                if output_arr[x] in logic_symbols:
                    if output_arr[x] == "~" or  output_arr[x] == "-":
                        if output_arr[x + 1] == "True":
                            output_arr[x + 1] = "False"
                            negation_position.append(x)
                        elif output_arr[x + 1] == "False":
                            output_arr[x + 1] = "True"
                            negation_position.append(x)
                          
        consolidated_output = ""
        for x in range(len(output_arr)):
            consolidated_output += f"{output_arr[x]} "

        output_arr = consolidated_output.split()
        for x in negation_position:
            output_arr.pop(x)

        consolidated_output = ""
        for x in range(len(output_arr)):
            consolidated_output += f"{output_arr[x]} "

        
        return consolidated_output[:-1]
    else:
        return False














# INPUT LOGICAL STATEMENT
print("\nADD SPACES BETWEEN ELEMENTS AND SYMBOLS")
print("\tEX: (a and b) > ~( c or b )")
logic_statement = input("\nPlease enter logic statement: ").lower()


# CONDITION THE STATEMENT 
validated_elements = check_pairs_identify_elements(logic_statement)
if not validated_elements: print("ERROR: Please enter valid statement");exit()


# FIND INDIVISUAL VARIABLES
for i in validated_elements:
    if len(i.split()) > 0:
        for y in i.split():
            if y not in variables_list and y not in logic_symbols :
                variables_list.append(y)
                    



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



# calculate logical expression
if brackets:
    for x in range(0, len(df.index) , 1):
        df.loc[x , logic_statement ] = solve(
            logic_statement , validated_elements , variables_list , x
        )
else:
    for x in range(0, len(df.index) , 1):
        variable_truths = [ df.loc[x,value] for value in variables_list  ]
        truth_statement = ""
        for element in logic_statement.split():
            submited_element = False
            # check if variable or logic symbol
            if element in variables_list:
                truth_index = variables_list.index(element)
                truth_statement += f"{variable_truths[truth_index]}"
                submited_element = True
            elif element in logic_symbols:
                truth_statement += f" {element} "
                submited_element = True
            else:
                # print("else! :" , element)
                pass

            if len(element)> 1 and not submited_element:
                for e in element:
                    if (e in open_list) or (e in close_list)  :
                        truth_statement += str(e) + " "
                        submited_element = True
                    elif e in variables_list:
                        truth_index = variables_list.index(e)
                        truth_statement += f"{variable_truths[truth_index]}"
                        submited_element = True
                    
            if submited_element == False:
                if ord(element) in [ord(_) for _ in close_list]:
                    truth_statement += " " +  str(element) 
                elif ord(element) in [ord(_) for _ in open_list]:
                    truth_statement += " " +  str(element) 
                else:
                    print("rejected element:" ,  ord(element) , ord(")")  )
                    print(element)
                    print(truth_statement  )
                    exit()
        print(truth_statement)
        df.loc[x , logic_statement ] = truth_statement


print(df)
print("\n")
print(f"Truth Combinations: {number_of_rows}")

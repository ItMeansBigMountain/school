import numpy as np
import pandas as pd
import copy




# SHALLOW COPY
dictionary = {'Sophia' : [97,88]} #original
dict_copy = dictionary.copy() #shallow copy
dictionary["Sophia"].append(100) #array manipulation



# OUTPUT
print(
    """
    CODE SHALLOW COPY
        dictionary = {'Sophia' : [97,88]}
        dict_copy = dictionary.copy()
        dictionary["Sophia"].append(100)
    
    PRINT STATEMENTS
    """ 
)
print("\tORIGINAL: ", dictionary)
print("\tCOPY: \t",dict_copy)


#/////////////////////////////////////////////////////////////////////




# DEEP COPY
dict_deep_copy = copy.deepcopy(dictionary) #using original array from line 9
dictionary["Sophia"].append(0) #array manipulation

# OUTPUT
print(
    """\n-------------------------------------\n
    CODE DEEP COPY
        dict_deep_copy = copy.deepcopy(dictionary)  
        dictionary["Sophia"].append(0)
    
    PRINT STATEMENTS
    """
)
print("\tORIGINAL: ", dictionary)
print("\tDEEPCOPY: ",dict_deep_copy )
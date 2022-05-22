import numpy as np
import pandas as pd
import copy

# primative data model for tempreture readings
temp_dict = {
    "Maxine" : [93 , 97 , 92] ,
    "James" : [99, 102, 93] ,
    "Amanda" : [93 , 94 , 93] ,
}



# dictionary enduced dataframe 
tempretures = pd.DataFrame(temp_dict)
print( "\n\tA - Dictionary enduced dataframe \n\n", tempretures,end="\n_________________\n\n")




# Recreate dataframe with indicies
tempretures = pd.DataFrame(temp_dict , index = ['Morning' , 'Afternoon' , 'Evening' ])
print( "\n\tB - Recreate dataframe with indicies \n\n", tempretures,end="\n_________________\n\n")




# SELECT "maxine" FROM tempretures 
locate = tempretures.loc[: , "Maxine"]
print( "\n\tC - SELECT 'Maxine' FROM tempretures \n\n", locate,end="\n_________________\n\n")





# SELECT "Morning" FROM tempretures 
locate = tempretures.loc["Morning"]
print( "\n\tD - SELECT 'Morning' FROM tempretures \n\n", locate,end="\n_________________\n\n")





# SELECT "Morning & Evening"  FROM tempretures 
locate = tempretures.loc[  ["Morning","Evening" ]  , :    ]
print( "\n\tE - SELECT 'Morning & Evening' FROM tempretures \n\n", locate,end="\n_________________\n\n")








# SELECT "Amanda & Maxine"  FROM tempretures 
locate = tempretures.loc[  :  , ["Amanda","Maxine" ]    ]
print( "\n\tF - SELECT 'Amanda & Maxine'  FROM tempretures \n\n", locate,end="\n_________________\n\n")






# SELECT "Amanda & Maxine"  in "Morning & Afternoon" FROM tempretures 
locate = tempretures.loc[   ["Morning","Afternoon" ] ,  ["Amanda","Maxine" ]     ]
print( "\n\tG - SELECT 'Amanda & Maxine'  in 'Morning & Afternoon' FROM tempretures \n\n", locate,end="\n_________________\n\n")




# DATAFRAME.describe()
print( "\n\tH - DESCRIBE DATAFRAME \n\n",  tempretures.describe()   ,end="\n_________________\n\n")



# DATAFRAME.T
print( "\n\tI - TRANSPOSE DATAFRAME \n\n",  tempretures.T   ,end="\n_________________\n\n")



# SORT ALPHABETICALLY BY NAME
tempretures = tempretures.reindex(sorted(tempretures.columns), axis=1)
print( "\n\tJ - SORT COLUMNS ALPHABETICALLY BY NAME \n\n",  tempretures   ,end="\n_________________\n\n")
import numpy as np
"show me a different representation of the data...."
"var 100 saved and represented within np.arrays are stored as the same memory object in the backend"


# METADATA ABOUT np OBJECT
# numbers = np.array(  [  [2,3,5] , [7,11]   ]  )
# print( numbers )
# print(  type( numbers  ) )
# print( numbers.dtype  )
# print( numbers.ndim  )
# print( numbers.shape  )




# FILLING MULTI DIMENTIONAL ARRAY WITH ZEROS 
# zeros = np.zeros( (10,4) , dtype=int  )
# print(zeros)




# FILLING MULTI DIMENTIONAL ARRAY WITH 99
# n99 = np.full( (30 , 5) ,  99 )
# print( n99 )


# RANGE INTEGER ARRAY
# arr = np.arange(50, 100)
# arr = np.arange(10, 1 , -1)
# print( arr  )


# RANGE FLOAT ARRAY 
# float_arr = np.linspace( 1.0, 10.0, num=100)
# print(float_arr)



# numbers = np.array([2, 3, 5, 7, 11])
# print(  type(numbers)  )



# DISPLAYING LARGE ARRAYS .reshape() will seperate array into multi dimentions
# large = np.arange(1, 4001 ).reshape( 4 , 1000 )
# print(large)




# SIMULATE ROLLING DICE 
# rolls = np.random.randint( 1,7 , 4_000 )
# print(rolls)





# ARRAY OPERATIONS
# arr = np.arange(5, 16)

# print(arr)
# print(arr * 2)
# print(arr - 5)
# print(arr ** 2)

# print(arr <= 10 )




# NUMPY OBJECT METHODS
# arr = np.array( [5, 20 , 10 , 30 , 15 , 40] )
# rootz = np.sqrt(arr)

# print(arr)
# print(  rootz  )





# SLICING NP ARRAYS
# grades = np.array([ [67,89,97] , [99,89,100] , [100,100,100]    ])
# print( grades[0 , 2]   ) # subset inner index

# selected_rows = grades[ [0 , 2]  ]
# print(  selected_rows  ) # select row indicies for new selected arr





# # SHALLOW COPIES "views"
# numbers = np.arange(1, 7)
# numbers_2 = numbers.view()

# print("old\n" , numbers)
# print(numbers_2)


# numbers = numbers * 50
# print("\nnew\n" , numbers)
# print(numbers_2)


# # DEEP COPY
# # "new copy that does not affect original array"

# arr = np.arange(1, 7)
# copy_arr = arr.copy()
# print("old\n" , arr)
# print(copy_arr)


# arr = arr * 50
# print("\nnew\n" , arr)
# print(copy_arr)






# FLATTEN MULTI DIMENTION INTO SINGLE DIMENTION
# arr = np.arange(0, 10).reshape(5,2)
# print("old: " , arr)

# arr = arr.flatten()
# print("new: " , arr)



# TRANSPOSE! [flips the (5,2)]
# arr = np.arange(0, 10).reshape(5,2)
# print( arr )
# print( arr.T )





"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"








# PANDAS NOTES
"creating dataframes & series"

"series allows us to hold models with missing data"





import pandas as pd

# series
    #array that acts like a ditionary
# grades = pd.Series( [87 , 99 , 76] , index = ["affan" , "wally" , "peter"] )

# methods
# print("count" ,  grades.count()   )
# print("mean" ,  grades.mean()   )
# print("min" ,  grades.min()   )
# print("max" ,  grades.max()   )
# print("standard deviation" ,  grades.std()   )
# print(grades.describe())
# print(grades)





# dataframe
    # 2 dimentional array with rows and columns
# grades_dict = {
#     "affan" : [88, 70 , 100],
#     "eva" : [50,99,110],
#     "anderson" : [100,80,66],
# }

# grades = pd.DataFrame(grades_dict)
# grades.index = ['Test1' , 'Test2' , 'Test3']


# print(grades.loc["Test2"] , "\n----------------")

# print(grades.iloc[0] , "\n----------------")

# print(grades.loc["Test1" : "Test2"] , "\n----------------")



# BOOLEAN INDEXING
# grades_dict = {
#     "affan" : [88, 70 , 100],
#     "eva" : [50,99,110],
#     "anderson" : [100,80,66],
# }
# grades = pd.DataFrame(grades_dict)

# # filters using boolean as index to pull all scores above 90
# grades_90_above = grades[grades > 90]
# print(grades_90_above)









"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"
"------------------------------------------------------------------------------------"



# SET NOTATION FUNCTIONS


# union = { 1 , 3 , 5 } | {2 , 4 , 3}
# print(union)


# intersection = { 1 , 3 , 5 } & {2 , 4 , 3}
# print(intersection)


# difference = { 1 , 3 , 5 } - {2 , 4 , 3}
# print(difference)


# symetric_diff = { 1 , 3 , 5 } ^ {2 , 4 , 3}
# print(symetric_diff)


# disjoint = { 1 , 3 , 5 }.isdisjoint( {20 , 40 , 30} ) # True
# disjoint = { 1 , 3 , 5 }.isdisjoint( {2 , 4 , 3} ) # False
# print(disjoint)



# a = [1 , 2 , 3 ]
# b = [1 , 2 , 3 ]
# c = [1 , 2 , 3  , 4]



# print(a==b)
# print(a==c)
# print(a<c)
# print(a>=b)
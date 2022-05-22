'''
    (Finding the People with a Specified Last Name) Create a list of tuples containing
    first and last names. Use filter to locate the tuples containing the last name Jones.
    Ensure that several tuples in your list have that last name.
'''

people = [
    ("Gottfried" , "Leibniz" ),
    ( "Lisa" , "jones"),
    ("Affan" , "Fareed" ),
    ("Jeff" , "Musk" ),
    ( "Peter" , "jones"),
    ( "brian" , "jones"),
    ("Guido" , "Rossum" ),
]

# return a tuple version of filter object who needs 2 params: Iteration method of action & Iterable
Jones_family = tuple( filter( lambda x : x[1].upper() == "JONES"  , people   ))


print(f"{Jones_family = }")
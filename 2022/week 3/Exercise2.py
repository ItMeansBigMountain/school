tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# a) Check whether the dictionary contains the key 'Canada'.
def a(countries):
    if countries.get("Canada"):
        return True
    else:
        return False


# b) Check whether the dictionary contains the key 'France'.
def b(countries):
    if countries.get("France"):
        return True
    else:
        return False


# c) Iterate through the key–value pairs and display them in two-column format.
def c(countries):
    print("\nC\n------------")
    for key , value in countries.items():
        print(f"{key} : {value}"  )
    print("------------")


# d) Add the key–value pair 'Sweden' and 'sw' (which is incorrect).
def d():
    global tlds
    tlds.update({"Sweden" : "sw"})


# e) Update the value for the key 'Sweden' to 'se'.
def e():
    global tlds
    tlds['Sweden'] = "se"


# f) Use a dictionary comprehension to reverse the keys and values.
def f(dictionary):
    reversed_dictionary = { value : key for key, value in dictionary.items() }
    return reversed_dictionary


# g) use a dictionary comprehension to convert the country names to all uppercase letters
def g(dictionary):
    capital_Value_Dic = { key : value.upper() for key, value in dictionary.items() }
    return capital_Value_Dic






# output
A = a(tlds) ; print(f"\n{A = }")
B = b(tlds) ; print(f"\n{B = }")
c(tlds)
d() ; print(f"\nD \n {tlds = }")
e() ; print(f"\nE \n {tlds = }")
F = f(tlds); print(f"\n{F = }")
G = g(F); print(f"\n{G = }")
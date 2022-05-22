def recursive_mul(a,b):
    # print(a,b)
    if b ==1:
        return a
    else:
        debug = a + recursive_mul(a, b -1 )
        # print(f"{debug = }")
        # return debug
        return a + recursive_mul(a, b -1 )




print(recursive_mul(2, 10))
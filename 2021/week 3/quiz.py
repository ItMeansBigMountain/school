def getDistance(mph , hours):
    return mph * hours


def report(f , s , time):
    # call helper function to get my variables
    fast = getDistance(f, time)
    slow = getDistance(s, time)

    # run conditional for plural hours... also just do the math in the return's equation.
    if time > 1:
        return f'The distance between the two cars after {time} hours is { fast-slow } miles.'
    else:
        return f'The distance between the two cars after {time} hour is { fast-slow  } miles.'




# OUTPUT
meter = report(f = 75, s = 65, time = 1)
print(meter)
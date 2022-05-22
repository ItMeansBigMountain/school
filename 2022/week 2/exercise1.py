# USER INPUT
principal = float(input("Please enter how much you would like to invest: $"))
intrest_rate = 0.07
years = [10 , 20 , 30]

# DISPLAY ALGO
print("\n\n(Principal + Interest)")
for x in range(0,len(years),1):
    amount = principal * ((1 + intrest_rate) * years[x])
    print(f"{years[x]} years :" , "${:.2f}".format(amount) )
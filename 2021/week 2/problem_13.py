score = float(input("Please enter grade (-1 to end and calc averages):  "))
count = 0
total = 0



while int(score) != -1:
    total += score
    count += 1
    score = float(input("Please enter grade (-1 to end and calc averages):  "))
average = total / count



print(F"AVERAGE : {average} ")

# input
grade = int(input("Please enter a number sequence (no spaces):  "))

# convert data type as new var... iterate through str, convert single char to int and add to total
txt = str(grade)
total = 0
for x in txt:
    total += int(x)

# display
print(total)



# output
# Please enter a number sequence (no spaces):  243
# 9
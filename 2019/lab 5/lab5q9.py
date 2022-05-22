salary = .01
pay = .01
days = int(input('Please specify how many days you worked: '))
print('day: 1 --> You made: $'+ str(pay))
for x in range(2,days+1):
	pay = pay*2
	salary += pay
	print('day: '+ str(x)+ ' --> You made: $'+ str(pay))
print('Total salary: $'+ str(salary))


# OUTPUT

# Please specify how many days you worked: 22
# day: 1 --> You made: $0.01
# day: 2 --> You made: $0.02
# day: 3 --> You made: $0.04
# day: 4 --> You made: $0.08
# day: 5 --> You made: $0.16
# day: 6 --> You made: $0.32
# day: 7 --> You made: $0.64
# day: 8 --> You made: $1.28
# day: 9 --> You made: $2.56
# day: 10 --> You made: $5.12
# day: 11 --> You made: $10.24
# day: 12 --> You made: $20.48
# day: 13 --> You made: $40.96
# day: 14 --> You made: $81.92
# day: 15 --> You made: $163.84
# day: 16 --> You made: $327.68
# day: 17 --> You made: $655.36
# day: 18 --> You made: $1310.72
# day: 19 --> You made: $2621.44
# day: 20 --> You made: $5242.88
# day: 21 --> You made: $10485.76
# day: 22 --> You made: $20971.52
# Total salary: $41943.03
def fallingDistance(time):
	g = 9.8
	distance = 0.5 * (g * (time*time))
	return distance
	
def calc():
	for x in range(1,11):
		result = fallingDistance(x)
		print(x,"second(s): " + "{:.2f}".format(result) , "meters")

calc()


# OUTPUT
# 1 second(s): 4.90 meters
# 2 second(s): 19.60 meters
# 3 second(s): 44.10 meters
# 4 second(s): 78.40 meters
# 5 second(s): 122.50 meters
# 6 second(s): 176.40 meters
# 7 second(s): 240.10 meters
# 8 second(s): 313.60 meters
# 9 second(s): 396.90 meters
# 10 second(s): 490.00 meters
def sqrt(x):
	g = 2
	epsilon = 0.0000000001
	while(True):
		if g*g < x + epsilon and g*g > x - epsilon:
			break;
		g = (g + x/g)/2.0
	return g
input = raw_input("Square Root Calculator: ")
print sqrt(int(input))
dont_exit = raw_input()

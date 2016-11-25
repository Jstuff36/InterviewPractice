num1 = 5
num2 = 3

def GDC(num1, num2):
	if num1 > num2:
		smallest = num2
	else:
		smallest = num1
	for i in range(smallest, 0, -1):
		if num2 % i == 0 and num1 % i == 0:
			return(i)
print(GDC(num1, num2))

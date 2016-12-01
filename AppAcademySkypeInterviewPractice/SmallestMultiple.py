def SmallestMultiple():
	num =  2520
	flag = 0
	while True:
		print(num)
		if checker(num):
			return(num)
		num += 2520

def checker(num):
	for i in range(1,21):
		if num % i != 0:
			return(False)
	return(True)

print(SmallestMultiple())
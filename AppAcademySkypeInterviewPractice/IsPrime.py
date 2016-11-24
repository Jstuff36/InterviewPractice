num = 2

def IsPrime(num):
	#only even number that is prime is 2
	if num == 2:
		return(True)
	#0 and 1 are not prime nor are even numbers
	elif num < 2 or num % 2 == 0:
		return(False)
	#If the number is prime then it will not be divisible by any odd number less then it's square root
	for i in range(3, int(num**.5)+1, 2):
		if num % i == 0:
			return(False)
	return(True)

print(IsPrime(num))

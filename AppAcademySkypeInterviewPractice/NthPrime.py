num = 4

def IsPrime(num):
	#two is the only even prime number
	if num == 2:
		return(True)
	#Numbers < 2 are not prime nor are even numbers
	if num < 2 or num % 2 == 0:
		return(False)
	for i in range(3,int(num**.5)+1, 2):
		if num % i == 0:
			return(False)
	return(True)

def NthPrime(num):
	count = 0
	i = 0
	while count < num:
		if IsPrime(i):
			count += 1
		i += 1
	return(i-1)

print(NthPrime(num))
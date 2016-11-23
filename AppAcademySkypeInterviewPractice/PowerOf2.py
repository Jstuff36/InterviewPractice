num = 0

def PowerOf2(num):
	if num == 0:
		return('false')
	if num == 1:
		return('true')
	elif num % 2 == 1:
		return('false')
	else:
		return(PowerOf2(num/2))

print(PowerOf2(num))
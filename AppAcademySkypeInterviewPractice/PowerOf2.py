num = 18

def PowerOf2(num):
	#catch if 0 is passed in
	if num == 0:
		return('false')
	if num == 1:
		return('true')
	elif num % 2 == 1:
		return('false')
	else:
		return(PowerOf2(num/2))

print(PowerOf2(num))

#better way of doing it because recursion in python is very memory intensive
def PowerOf2NonRecursive(num):
	if num == 0:
		return('false')
	while num > 1:
		if int(num/2) != num/2:
			return('false')
		num /= 2
	return('true')

print(PowerOf2NonRecursive(num))
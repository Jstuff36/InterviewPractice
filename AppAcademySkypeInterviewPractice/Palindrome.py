def Palindrome():
	z = 0
	for i in range(100, 999):
		for j in range(100, 999):
			num = i * j
			if str(num) == str(num)[::-1] and num > z:
				z = num
	return(z)

print(Palindrome())

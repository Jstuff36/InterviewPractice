shift = 3
test_string = 'abc xyz'

def CecaeserCipher(shift, test_sting):
	ans = []
	for i in range(len(test_string)):
		temp = ord(test_string[i])
		if temp == ord(' '):
			ans.append(temp)
		elif temp + shift > ord('z'):
			ans.append(temp + shift - 26)
		else:
			ans.append(temp + shift)
	return(''.join([chr(i) for i in ans]))

print(CecaeserCipher(shift, test_string))
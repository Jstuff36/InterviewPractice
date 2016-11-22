test_str = 'hooplah'

def AlphabetSoup(test_str):
	ans = []
	for char in test_str:
		ans.append(ord(char))
	ans = sorted(ans)
	return(''.join([chr(x) for x in ans]))

print(AlphabetSoup(test_str))

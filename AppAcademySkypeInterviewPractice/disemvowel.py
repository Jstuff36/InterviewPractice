test_string = 'FoobAr'

def disemvowel(test_string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	ans = []
	for char in test_string:
		if char.lower() not in vowels:
			ans.append(char)
	return(''.join(ans))

print(disemvowel(test_string))

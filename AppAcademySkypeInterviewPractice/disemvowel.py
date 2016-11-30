test_string = 'FoobAr'

def disemvowel(test_string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	ans = []
	for char in test_string:
		if char.lower() not in vowels:
			ans.append(char)
	return(''.join(ans))

print(disemvowel(test_string))

def disemvowel2(test_string):
	Vowels = 'aeiou'
	ans = ''
	for char in test_string:
		if char.lower() not in Vowels:
			ans += char
	return(ans)

print(disemvowel2(test_string))

def listComp(test_string):
	vowels = 'aeiou'
	ans = [char for char in test_string if char.lower() not in vowels]
	return(''.join(ans))

print(listComp(test_string))
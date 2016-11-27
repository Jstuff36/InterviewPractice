test_string = 'abba'

def LongestPalindrome(test_string):
	longest = ''
	for i in range(len(test_string)):
		for j in range(i+1, len(test_string)):
			if IsPalindrome(test_string[i:j+1]) and len(test_string[i:j+1]) > len(longest):
				longest = test_string[i:j+1]
	return(longest)

def IsPalindrome(test_string):
	if test_string == test_string[::-1]:
		return(True)
	else:
		return(False)

print(LongestPalindrome(test_string))

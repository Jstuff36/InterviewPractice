test_string = 'hello world#$323'

def LetterCapitalize(test_string):
	words_cap = [word.capitalize() for word in test_string.split()]
	return(' '.join(words_cap))

print(LetterCapitalize(test_string))
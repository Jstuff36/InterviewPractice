test_string = 'hello world#$323'

def LetterCapitalize(test_string):
	return(' '.join([word.capitalize() for word in test_string.split()]))

print(LetterCapitalize(test_string))
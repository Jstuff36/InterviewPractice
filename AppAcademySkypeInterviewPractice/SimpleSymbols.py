test_string = '+f++d+'

def SimpleSymbols(test_string):
	if test_string[0].isalpha():
		return('false')
	for i in range(1,len(test_string)):
		if test_string[i].isalpha():
			if test_string[i-1] != '+' or test_string[i+1] != '+':
				return('false')
	return('true')

print(SimpleSymbols(test_string))
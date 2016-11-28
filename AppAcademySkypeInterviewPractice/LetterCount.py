test_string = 'cats are fun'

def LetterCount(test_string):
	dic = {}
	for let in test_string.replace(' ', ''): #Use replace to get rid of whitespace
		if let in dic:
			dic[let] += 1
		else:
			dic[let] = 1
	return(dic)

print(LetterCount(test_string))
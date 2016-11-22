test_string = 'Hello World'

def StringReverse(test_string):
	ans = []
	for i in range(len(test_string)-1, -1, -1):
		ans.append(test_string[i])
	return(''.join(ans))

print(StringReverse(test_string))

#with recursion
def RecursiveReverse(test_string):
	if len(test_string) == 1:
		return(test_string)
	return(RecursiveReverse(test_string[1:])+test_string[0])

print(RecursiveReverse(test_string))
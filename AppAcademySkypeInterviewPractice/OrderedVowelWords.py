test_string = 'this is a test of the vowel ordering system'

def OrderedVowelWords(test_string):
	ans = []
	words = test_string.split(' ')
	for word in words:
		if InOrder(word):
			ans.append(word)
	return(' '.join(ans))

def InOrder(word):
	vowels_present = []
	vowels = 'aeiou'
	for let in word:
		if let in vowels:
			vowels_present.append(let)
	if sorted(vowels_present) != vowels_present:
		return(False)
	#for let in range(len(vowels_present)-1):
		#if vowels_present[let] > vowels_present[let+1]:
		#	return(False)
	return(True)

print(OrderedVowelWords(test_string))
test_string = 'abc'

def MostCommonLetter(test_string):
	test_string = ''.join(sorted(test_string))
	most_common = 0
	for i in range(len(test_string)):
		j = i + 1
		count = 1
		while j < len(test_string) and test_string[i] == test_string[j]:
			count += 1
			j += 1
		if count > most_common:
			most_common = count
			let = test_string[i]
	return([let, most_common])

print(MostCommonLetter(test_string))
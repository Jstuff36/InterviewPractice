test = 'a confusing /:sentence:/[ this is not!!!!!!!~'

def longest_word(test):
	str2array = test.split(' ')
	length = ''
	for i in str2array:
		i = ''.join([j for j in i if i.isalpha() or i.isnumeric()])
		if len(i) > len(length):
			length = i
	return(length)

print(longest_word(test))
test_string = 'hello*3'

def LetterChanges(test_string):
	new_string = ''
	for i in range(len(test_string)):
		new_string += dic(test_string[i])
	return(new_string)

def dic(char):
	dictionary ={
		'a': 'b',
		'b': 'c',
		'c': 'd',
		'd': 'E',
		'e': 'f',
		'f': 'g',
		'g': 'h',
		'h': 'I',
		'i': 'j',
		'j': 'k',
		'k': 'l',
		'l': 'm',
		'm': 'n',
		'n': 'O',
		'o': 'p',
		'p': 'q',
		'q': 'r',
		'r': 's',
		's': 't',
		't': 'U',
		'u': 'v',
		'v': 'w',
		'w': 'x',
		'x': 'y',
		'y': 'z',
		'z': 'A'
		}
	if char in dictionary:
		return(dictionary[char])
	else:
		return(char)

print(LetterChanges(test_string))

#Other way
#print(chr(ord('B')+1))
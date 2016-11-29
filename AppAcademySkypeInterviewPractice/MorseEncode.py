Test_string = 'cat in hat'


def MorseEncode(Test_string):
	ans = ''
	for char in Test_string:
		ans += MorseDic(char.capitalize())
	return(ans)


def MorseDic(char):
    dic = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
   	'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' '
    }
    return(dic[char] + ' ')


print(MorseEncode(Test_string))
test_string = 'markov'
test_list = [5, 3, 1, 4, 2, 0]

def ScrambleString(test_string, test_list):
	ans = ''
	for num in test_list:
		ans += test_string[num]
	return(ans)

print(ScrambleString(test_string, test_list))
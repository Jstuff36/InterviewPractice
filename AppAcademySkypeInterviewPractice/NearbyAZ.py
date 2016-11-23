test_string = "abcz"

def NearbyAZ(test_string):
	for i in range(len(test_string)):
		if test_string[i] == 'a':
			j = i + 1
			while j < len(test_string) and j <= i + 3:
				if test_string[j] == 'z':
					return('true')
				j += 1
	return('false')

print(NearbyAZ(test_string))
test_string = 'i am checking this string to see how many times each character appears'

#First with sorted because easier
def NumRepeats(test_string):
	test_string = sorted(test_string)
	count = 0
	i = 0
	while i < len(test_string):
		flag = 0
		j = i + 1
		while j < len(test_string) and test_string[i] == test_string[j]:
			flag = 1
			j += 1
		if flag == 1:
			count += 1
		i = j

	return(count)

print(NumRepeats(test_string))

#Now without sorted incase it cannot not be used
def NumRepeatsNoSorted(test_string):
	count = 0
	i = 0
	current_chars = []
	while i < len(test_string):
		for j in range(i+1, len(test_string)):
			if test_string[j] == test_string[i] and test_string[i] not in current_chars:
				count += 1
				current_chars.append(test_string[i])
		i += 1
	return(count)

print(NumRepeatsNoSorted(test_string))

#More elegent solution modified from stackoverflow
#wow dictionaries are cool
def NumRepeatSOF(test_string):
	count = {}
	for char in test_string:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	return(sum([1 for keys in count if count[keys] > 1]))

print(NumRepeatSOF(test_string))




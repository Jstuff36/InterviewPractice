test_list = [2, 3, 7, 4]

#This way is kind of cheating because of sorted
def ThirdGreatest(test_list):
	test_list = sorted(test_list)
	return(test_list[-3])

print(ThirdGreatest(test_list))

#Another Way
def ThirdGreatestReal(test_list):
	first = 0
	second = 0
	third = 0
	for num in test_list:
		if num >= first:
			third = second
			second = first
			first = num
		elif num >= second:
			third = second
			second = num
		elif num >= third:
			third = num
	return(third)

print(ThirdGreatestReal(test_list))
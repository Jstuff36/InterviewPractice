test_list = [1, 3, 5, -2, 6, -1]

def TwoSum(test_list):
	for i in range(len(test_list)):
		for j in range(i+1, len(test_list)):
			if test_list[i] + test_list[j] == 0:
				return([i,j])
	return('nil')

print(TwoSum(test_list))
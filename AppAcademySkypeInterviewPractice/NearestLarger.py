test_list = [2, 6, 9, 4, 8]
index = 3

def NearestLarger(test_list, index):
	diff = 1
	while True:
		LeftIndex = index - diff
		RightIndex = index + diff
		if LeftIndex >= 0 and test_list[LeftIndex] > test_list[index]:
			return(LeftIndex)
		elif RightIndex < len(test_list) and test_list[RightIndex] > test_list[index]:
			return(RightIndex)
		elif LeftIndex == 0 and RightIndex >= len(test_list):
			return(None)
		diff += 1

print(NearestLarger(test_list, index))

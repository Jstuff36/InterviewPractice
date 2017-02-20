test_list = [5,4,1,2,3]

def bubble_sort(test_list):
	for i in range(len(test_list)):
		for j in range(i+1,len(test_list)):
			if test_list[i] > test_list[j]:
				temp = test_list[i]
				test_list[i] = test_list[j]
				test_list[j] = temp
		print(test_list)
	return(test_list)

print(bubble_sort(test_list))

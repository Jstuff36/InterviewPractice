test_list = [2, 3, 5, 2]

def crazy_sum(test_list):
	return(sum([num * index for num,index in enumerate(test_list)]))

print(crazy_sum(test_list))

num = 37
def square_nums(num):
	count = 0
	for i in range(1,num):
		if i*i < num:
			count += 1
		elif i*i >= num:
			break
	return(count)

print(square_nums(num))

num = 20
def crazy_nums(num):
	ans = []
	for i in range(num):
		if i % 3 == 0 and i % 5 == 0:
			continue
		elif i % 3 == 0:
			ans.append(i)
		elif i % 5 == 0:
			ans.append(i)
	return(ans)

print(crazy_nums(num))




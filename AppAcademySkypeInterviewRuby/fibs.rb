def fibs(num)
	return 1 if num < 2
	arr = [0, 1]
	(1..num-2).each { |i| arr << arr[-1] + arr[-2] }
	arr
end

p fibs(100)

def fibs_rec(num, arr = [0, 1])
	return 1 if num < 2
	return arr if num == 2
	arr << arr[-1] + arr[-2]
	fibs_rec(num-1, arr)

end

p fibs_rec(100)
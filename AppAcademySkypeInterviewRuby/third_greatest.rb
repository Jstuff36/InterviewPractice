def third_greatest(arr)
	first = 0
	second = 0
	third = 0
	arr.each do |i|
		if i >= first
			temp = first
			third = second
			second = temp
			first = i
		elsif i >= second
			third = second
			second = i
		elsif i >= third
			third = i
		end
	end
	third
end

p third_greatest([2, 3, 7, 4, 8, 9, 10])
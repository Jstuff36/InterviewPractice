def third_greatest(arr)
	first = nil
	second = nil
	third = nil
	arr.each do |i|
		if first.nil? || i >= first
			temp = first
			third = second
			second = temp
			first = i
		elsif second.nil? || i >= second
			third = second
			second = i
		elsif third.nil? || i >= third
			third = i
		end
	end
	third
end

p third_greatest([2, 3, 7, 4, 8, 9, 10])
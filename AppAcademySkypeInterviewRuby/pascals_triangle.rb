def pascals_triangle(levels, arr = [[1], [1,1]])

	return arr[0] if levels == 1
	return arr[1] if levels == 2
	n = 1
	while n < levels
		(0...arr[n].length-1).each do |i|
			arr[n+1] ||= [1]
			arr[n+1] << arr[n][i] + arr[n][i+1]
		end
		arr[n+1] << 1
		n += 1
	end
	arr
end

p pascals_triangle(10)
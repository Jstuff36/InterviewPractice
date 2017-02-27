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

p pascals_triangle(5)

def pascals_triangle_rec(levels)
	return [[1]] if levels == 0
	return [[1],[1,1]] if levels == 1

	result = pascals_triangle_rec(levels - 1)
	new_row = [1]

	last_row = result[-1]
	(0...last_row.length-1).each do |i|
		new_row << last_row[i] + last_row[i+1]
	end
	new_row << 1
	result << new_row
	result
end

p pascals_triangle_rec(5)
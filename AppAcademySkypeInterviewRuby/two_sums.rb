def two_sums(arr)
	arr.each_index do |i|
		j = i + 1
		while j < arr.length
			return [i,j] if arr[i] + arr[j] == 0
			j += 1
		end
	end
	nil
end

p two_sums([1, 3, 5])
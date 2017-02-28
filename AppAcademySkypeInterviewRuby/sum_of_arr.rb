def sum_of_arr(arr, target)
	arr.each_with_index do |val, i|
		(i+1...arr.length).each do |j|
			return [i,j] if arr[i] + arr[j] == target
		end
	end
	false
end

p sum_of_arr([2,3,7,9,10], 10)


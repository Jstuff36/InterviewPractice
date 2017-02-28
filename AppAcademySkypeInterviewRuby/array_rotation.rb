def array_rotation(arr, steps)
	shifted_array = []
	i = arr.length
	while true

		if i - steps < arr.length
			shifted_array << arr[i - steps]
			i += 1
		else
			shifted_array << arr[i - steps - arr.length]
			i += 1
		end

		return shifted_array if arr.length == shifted_array.length
	end
end

p array_rotation([1, 2, 3, 4, 5], 3)
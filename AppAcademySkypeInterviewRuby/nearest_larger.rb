def nearest_larger(arr, idx)

	count = 1

	while true
		if idx + count * -1 >= 0 and arr[idx + count * -1 ] > arr[idx]
			return idx + count *-1
		elsif idx + count < arr.length and arr[idx + count]  > arr[idx]
			return idx + count
		end

		count += 1

		if  count + idx >= arr.length and (count + idx * -1) < 0
			return nil
		end

	end
end

p nearest_larger([2, 6, 9, 4, 8], 3)
def is_power_of_two?(num)
	return false if num < 1 #edge case

	while num > 1
		return false if num % 2 == 1
		num /= 2
	end
	true
end

p is_power_of_two?(0)

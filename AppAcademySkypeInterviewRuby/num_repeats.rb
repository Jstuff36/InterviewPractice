def num_repeats(str)
	counter = 0
	repeats = []
	str_split = str.split("")
	str_split.each_with_index do |val, i|
		((i + 1)..str_split.length).each do |j|
			if val == str_split[j] and not repeats.include? val
				counter += 1
				repeats << val
				next
			end
		end
	end

	counter

end

p num_repeats("abcde")
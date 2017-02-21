def most_common_letter(str)
	counter = 0
	num_times = 1
	most_common = 0
	let = nil
	str.split("").each_with_index do |val, i|
		counter = i + 1
		while counter < str.length
			num_times += 1 if val == str[counter]
			counter += 1
		end

		if num_times > most_common
			most_common = num_times
			let = val
		end
		num_times = 1
	end
	[let, most_common]
end

p most_common_letter("abbabcccccc")
def dasherize(num)
	num_split = num.to_s.split("")
	nums_to_pars = num_split[1..-2]
	dasherized = nums_to_pars.map do |i|
		if Integer(i) % 2 == 1
			"-" << i << "-"
		else
			i
		end
	end
	if num_split[0].to_i % 2 == 1
		dasherized.unshift(num_split[0] << "-")
	else
		dasherized.unshift(num_split[0])
	end

	if num_split[-1].to_i % 2 == 1
		dasherized << "-" << num_split[-1]
	else
		dasherized << num_split[-1]
	end


	normalized = dasherized.join("").split("")
	ans = []

	normalized.each_index do |i|
		if normalized[i] != "-"
			ans << normalized[i]
		elsif normalized[i] == "-" and normalized[i+1] == "-"
			next
		else
			ans << normalized[i]
		end
	end
	ans.join("")
end

p dasherize(3223)
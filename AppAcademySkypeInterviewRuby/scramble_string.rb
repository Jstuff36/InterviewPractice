def scramble_string(str, pos)
	str_split = str.split("")
	scrambled = pos.map do |i|
		str_split[i]
	end
	scrambled.join("")
end

p scramble_string("markov", [5, 3, 1, 4, 2, 0])
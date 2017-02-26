def word_unscrambler(str, arr)
	matches = []
	arr.each do |val|
		matches << val if val.chars.sort == str.chars.sort
	end
	matches
end

p word_unscrambler("turn", ["numb", "turn", "runt", "nurt"])
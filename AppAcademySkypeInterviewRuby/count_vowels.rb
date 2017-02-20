def count_vowels(str)
	vowels = %w[a e i o u]
	counter = 0
	str.split("").each do |let|
		counter += 1 if vowels.include? let
	end
	counter
end

puts count_vowels("colour")
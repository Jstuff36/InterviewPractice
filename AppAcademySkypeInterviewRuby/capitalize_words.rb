def capitalize_words(str)
	str_split = str.split(" ")
	capitalized = str_split.map { |i| i.capitalize }
	capitalized.join(" ")
end

def capitalize_words_diff(str)
	str_split = str.split(" ")
	capitalized = str_split.map do |word|
		word[0] = word[0].upcase
		word
	end
	capitalized.join(" ")
end

p capitalize_words("this is a sentence")
p capitalize_words_diff("this is a sentence")
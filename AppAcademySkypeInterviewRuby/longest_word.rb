def longest_word(sentence)
	words = sentence.split(" ")
	longest = ""
	words.each do |word|
		longest = word if word.length > longest.length
	end
	longest
end

test_str = "abc def abcde"
puts longest_word(test_str)
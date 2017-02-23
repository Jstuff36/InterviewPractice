def ordered_vowel_words(str)
	words = str.split(" ")
	good_words = []
	words.each do |word|
		good_words << word if ordered_vowel_word?(word)
	end
	good_words.join(" ")
end

def ordered_vowel_word?(str)
	vowels = %w[a e i o u]
	str_split = str.split("")
	vow = []
	str_split.each do |let|
		vow << let.ord if vowels.include? let
	end

	return true if vow == vow.sort

end

p ordered_vowel_words("this is a test of the vowel ordering system")
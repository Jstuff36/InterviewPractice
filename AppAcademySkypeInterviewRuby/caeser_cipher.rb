def caeser_cipher(offset, str)

	str_split = str.split("")
	str_translated = ""

	str_split.each do |char|
		if char == " "
			str_translated << char
		elsif char.ord + offset > 122
			str_translated << (char.ord + offset - 26).chr
		else
			str_translated << (char.ord + offset).chr
		end
	end

	str_translated

end

p caeser_cipher(3, "abc xyz")
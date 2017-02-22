def palindrome?(str)
	counter = str.length - 1
	reversed_str = ""
	while counter >= 0
		reversed_str << str[counter]
		counter -= 1
	end
	return true if reversed_str == str
	false
end

def longest_palindrome(str)
	str_split = str.split("")
	longest = ""
	str_split.each_with_index do |val1, i|
		(i...str.length).each do |j|
			longest = str[i..j] if palindrome?(str[i..j]) and str[i..j].length > longest.length
		end
	end
	longest
end

p longest_palindrome("abcbd")
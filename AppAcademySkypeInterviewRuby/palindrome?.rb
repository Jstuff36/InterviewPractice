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

puts palindrome?("racecar")
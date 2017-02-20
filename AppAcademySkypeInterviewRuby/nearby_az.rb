def nearby_az(str)
	str.split("").each_with_index do |val, index|
		if val == "a"
			return true if str[index + 1] == "z" || str[index + 2] == "z" || str[index + 3] == "z"
		end
	end
	false
end

puts nearby_az("fza")
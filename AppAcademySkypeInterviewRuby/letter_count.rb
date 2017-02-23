def letter_count(str)
	str_split = str.split("")
	dic = {}
	str_split.each do |val|
		if val == " "
			next
		elsif dic.keys.include? val
			dic[val] += 1
		else
			dic[val] = 1
		end
	end
	dic
end

p letter_count("cats are fun")
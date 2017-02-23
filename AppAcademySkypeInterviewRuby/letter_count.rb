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

def letter_count_w_Hash(str)
	str_split = str.split("")
	dic = Hash.new(0) #Hash.new() set a value for any key created equal to what's in parenthesis
	str_split.each do |val|
		dic[val] += 1 unless val == " "
	end
	dic
end

p letter_count_w_Hash("cats are fun")

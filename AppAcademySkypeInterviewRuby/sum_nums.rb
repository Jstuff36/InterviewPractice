def sum_nums(num)
	total = 0
	(1..num).each do |i|
		total += i
	end
	total
end

puts sum_nums(5)
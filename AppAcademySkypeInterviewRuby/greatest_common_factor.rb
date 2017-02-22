def greatest_common_factor(num1, num2)

	factors = []
	(1..num1).each do |i|
		factors << i if num1 % i == 0
	end

	common_factors = []
	(1..num2).each do |i|
		common_factors << i if num2 % i == 0 and factors.include? i
	end

	common_factors.last
end

p greatest_common_factor(3, 5)
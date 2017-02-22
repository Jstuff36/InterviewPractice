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

def AA_greatest_common_factor(num1, num2)

	if num1 > num2
		i = num1
	else
		i = num2
	end

	while true
		return i if num1 % i == 0 and num2 % i == 0
		i -= 1
	end
end

p AA_greatest_common_factor(18, 24)
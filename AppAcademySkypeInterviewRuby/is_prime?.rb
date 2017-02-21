def is_prime?(num)
	return false if num < 2 #only numbers greater than 1 can be prime
	return true if num == 2 #only even prime
	(2...num).each do |i|
		return false if num % i == 0
	end
	true
end

p is_prime?(4)
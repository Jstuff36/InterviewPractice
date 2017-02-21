def is_prime?(num)
	return false if num < 2 #only numbers greater than 1 can be prime
	return true if num == 2 #only even prime
	(2...num).each do |i|
		return false if num % i == 0
	end
	true
end

def nth_prime(n)
	counter = 0
	num_test = 2
	while counter < n
		counter += 1 if is_prime?(num_test)
		num_test += 1
	end
	num_test - 1
end

p nth_prime(125)
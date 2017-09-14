def find_prime(limit)
	num = 3
	primes = 1
	while true
		primes += 1 if is_prime?(num)
		return num if primes == limit
		num += 1
	end
end

def is_prime?(num)
	(2...num).each do |i|
		return false if num % i == 0
	end
	true
end

p find_prime(10001)
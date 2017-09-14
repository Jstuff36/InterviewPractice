def pytagorean_triplet
	(1..1000).each do |a|
		(1..1000).each do |b|
			(1..1000).each do |c|
				return [a,b,c] if a**2 + b**2 == c**2 and a + b + c == 1000
			end
		end
	end
end

p pytagorean_triplet
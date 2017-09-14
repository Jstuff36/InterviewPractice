def money_comb(total, denom)

	combinations = 0

	denom.each_with_index do |val,i|
		(i..denom.length).each do |j|
			amount = 0
			while amount < total
				amount += denom[j]
				combinations += 1 if amount == total
			end
	end

	combinations
end

p money_comb(4, [1,2,3])
def get_max_profit(stock_prices)
	largest_dif = nil
	stock_prices.each_with_index do |val, i|
		(i..stock_prices.length).each do |j|
			dif = stock_prices[i] - stock_prices[j]
			largest_dif = dif if dif > largest_dif
		end
	end
	largest_dif
end

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

p get_max_profit(stock_prices_yesterday)
def wonky_coins(num)
	return 1 if num == 0
	total = wonky_coins(num / 2) + wonky_coins(num / 3) + wonky_coins(num / 4)
	total
end

p wonky_coins(0)
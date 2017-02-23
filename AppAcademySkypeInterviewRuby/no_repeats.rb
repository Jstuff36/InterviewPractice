def no_repeats(year_start, year_end)
	good_years = []
	(year_start..year_end).each do |year|
		good_years << year if no_repeats_elegant?(year)
	end
	good_years
end

def no_repeats?(year)
	years_seen = []
	year_s_split = year.to_s.split("")
	year_s_split.each do |num|
		return false if years_seen.include? num
		years_seen << num
	end
	true
end

def no_repeats_elegant?(year)
	return false if year.to_s.split("").uniq.length < 4
	true
end

p no_repeats(1980, 1987)
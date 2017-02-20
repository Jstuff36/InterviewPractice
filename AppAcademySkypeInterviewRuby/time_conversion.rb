def time_conversion(minutes)
	#to convert something to an integer such as when one needs to round down
	#do Integer(thing)
	hours = Integer(minutes/60)
	minutes_left = minutes % 60
	if minutes_left > 10
		"#{hours}:#{minutes_left}"
	else
		"#{hours}:0#{minutes_left}"
	end
end

puts time_conversion(360)
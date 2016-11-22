num = 45

def TimeConvert(num):
	hours = num / 60
	minutes = num - 60 * int(hours)
	return(str(int(hours))+':'+str(minutes))

print(TimeConvert(num))
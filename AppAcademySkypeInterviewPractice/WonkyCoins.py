num = 1

def WonkyCoins(num):
	num = int(num)
	if num == 0:
		return(1)
	else:
		return(WonkyCoins(num/3) + WonkyCoins(num/2) + WonkyCoins(num/4))

print(WonkyCoins(num))
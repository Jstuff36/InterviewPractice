num = 3223

def DasherizeNumber(num):
	num = str(num)
	ans = ''
	for i in range(1, len(str(num))):
		if int(num[i-1]) % 2 == 1 or int(num[i]) % 2 == 1:
			ans += '-'
		ans += num[i]
	return(num[0] + ans)

print(DasherizeNumber(num))


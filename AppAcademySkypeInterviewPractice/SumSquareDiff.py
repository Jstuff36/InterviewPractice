def SumSquareDiff():
	SquareSum = 0
	SumSquared = 0
	for i in range(1, 101):
		SquareSum += i*i
		SumSquared += i
	return(SumSquared**2 - SquareSum)

print(SumSquareDiff())
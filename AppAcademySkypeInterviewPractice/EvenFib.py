def fib_series():
	terms = [0,1]
	while(terms[-1] + terms[-2] < 4000000):
		terms.append(terms[-1]+terms[-2])
	return(sum(i for i in terms if i%2 == 0))

print(fib_series())
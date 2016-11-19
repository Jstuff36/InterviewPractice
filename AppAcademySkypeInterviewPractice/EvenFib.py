def fib_series():
	terms = [0,1]
	num = 4000000 #change this term to change the upper limit of the sequence
	while(terms[-1] + terms[-2] < num):
		terms.append(terms[-1]+terms[-2])
	return(sum(i for i in terms if i%2 == 0))

print(fib_series())
#Project Euler first problem
num = 1000

def multiplies(num):
	total = 0
	for i in range(num):
		if i%3 == 0 or i%5 == 0:
			total += i
	return(total)

print(multiplies(num))

#or could do
#total = [i for i in range(num) if i%3 == 0 or i%5 == 0]
#return(sum(total))
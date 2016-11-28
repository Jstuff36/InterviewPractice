years = [1980, 1987]

def NoRepeats(years):
	ans = []
	for year in range(years[0], years[1]+1):
		if Repeat(str(year)):
			ans.append(year)
	return(ans)

def Repeat(year):
	for num in range(len(year)):
		for index in range(num+1,len(year)):
			if year[num] == year[index]:
				return(False)
	return(True)

print(NoRepeats(years))

#Better way found online using set

def NoRepeatsSet(years):
	return([i for i in range(years[0], years[1]+1) if len(set(str(i))) == 4])

print(NoRepeatsSet(years))
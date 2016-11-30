word = 'turn'
dic = {
1: 'turn',
2: 'numb',
3: 'runt',
4: 'nurt'
}

def WordUnscrambler(word, dic):
	ans = []
	for key in dic:
			if sorted(dic[key]) == sorted(word):
				ans.append(dic[key])
	return(ans)


print(WordUnscrambler(word, dic))
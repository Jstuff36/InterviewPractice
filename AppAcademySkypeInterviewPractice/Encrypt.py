test_string = 'aaabbbcccddd'

def encrypt(test_string):
    ans = []
    index = 0
    length = len(test_string)
    i = 0
    while i < length:
        count = 0
        j = i
        while j < len(test_string) and test_string[i] == test_string[j]:
            count += 1
            j += 1
        ans.append([])
        ans[index].append(test_string[i])
        ans[index].append(count)
        index += 1
        i = j
    return(ans)
print(encrypt(test_string))

def EncryptBetter(test_string):
    dic = {}
    for char in test_string:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return(sorted(dic.items()))
print(EncryptBetter(test_string))
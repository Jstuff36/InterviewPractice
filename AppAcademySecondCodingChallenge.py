test_string = 'abcdef'

def ordered_word(test_string):
    for i in range(len(test_string)-1):
        if test_string[i] > test_string[i+1]:
            return('false')
    return('true')

print(ordered_word(test_string))

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

words = ["door", "moot", "boot", "boots"]
test_word = 'moor'

def one_off_words(test_word, words):
    ans = []
    for word in words:
        #make sure words are same length
        if len(word) != len(test_word):
            continue
        count = 0
        for i in range(len(test_word)):
            if word[i] != test_word[i]:
                count += 1
                #Break loop if more than 1 letter is different in string
                if count > 1:
                    break
        if count < 2:
            ans.append(word)
    return(ans)

print(one_off_words(test_word, words))





test_list = [2,1,4,3,0]
def lucky_sevens(test_list):
    if len(test_list) < 3:
        return('Less than 3 elements in list')
    length = len(test_list)
    i = 2
    while i < length:
        if test_list[i] + test_list[i-1] + test_list[i-2] == 7:
            return('true')
        i += 1
    return('false')

print(lucky_sevens(test_list))
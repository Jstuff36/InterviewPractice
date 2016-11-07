# If the order of the operations did not matter I considered doing a check to see if R was even then do not do anything of only do S if it was greater than one. Because it was not specified I decided to do each operation as it was given.
import re
string = '(AB) C((DE)F) /S'

def exp_proccess(string):
    if string == '':
        return(string)
    regex = r"/[SR]+"
    matches = re.search(regex, string, re.IGNORECASE)
    string = string.replace(matches.group(0), '')
    flag = 0
    for i in matches.group(0):
        if i == 'R':
            new_string = []
            index = len(string)
            while index:
                index -= 1
                if string[index] == ')':
                    new_string.append('(')
                elif string[index] == '(':
                    new_string.append(')')
                else:
                    new_string.append(string[index])
            string = ''.join(new_string)
            flag = 0

        elif i == 'S':
            if flag == 1:
                continue
            length = len(string)
            i = 0
            counter = 0
            index = []
            while i < length:
                if string[i] == '(':
                    counter += 1
                    if counter > 1:
                        index.append(i)
                if string[i] == ')' and counter > 1:
                    index.append(i)
                    counter -= 1
                elif string[i] == ')' and counter == 1:
                    counter  -= 1
                i += 1
            i = 0
            for j in index:
                string = string[:j-i] + string[j+1-i:]
                i += 1
            for i in length
            flag = 1

    return(string)

print(exp_proccess(string))

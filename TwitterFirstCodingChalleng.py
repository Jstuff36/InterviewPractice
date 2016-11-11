# If the order of the operations did not matter I considered doing a check to see if R was even then do not do anything of only do S if it was greater than one. Because it was not specified I decided to do each operation as it was given.
import re
string = '((34)3)(((5)67)8) /RS'

def exp_process(string):
    if string == '':
        return('Input is empty') #If string is empty inform the user

    regex = r'/([RS]+)?'
    #Using regex capture the text that conatins the commands the program will do
    matches = re.search(regex, string, re.IGNORECASE)
    string = string.replace(matches.group(0), '').strip()
    flag = 0

    for operation in matches.group(0):
        #if an R is found reverse the string
        if operation == 'R' or operation == 'r':
            string = reverse_sting(string)
             #if a S is found simply the string
        elif operation == 'S'or operation == 's':
            if flag == 1:
                continue
            string = simplify_string(string)
            flag = 1
    return(string)

def reverse_sting(string):
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
    #Initialized string as list so I would not have to create a new string everytime because Python strings are immutiable
    #Now turn list into a string
    return(''.join(new_string))

def simplify_string(string):
    counter = 1
    first_paren = []
    length_string = len(string)
    i = 0
    #First remove parenthesis around the very first element if it exist
    if string[0] == '(':
        while i < length_string - 1:
            if string[i+1] == '(':
                counter += 1
            elif string[i+1] == ')':
                counter -= 1
                if counter == 0 and len(first_paren) == 0:
                    first_paren.append(i+1)
            i += 1
        #Remove first parenthesis by string splices
        string = string[1:first_paren[0]] + string[first_paren[0]+1:]

    length_substring = len(string)
    i = 0
    counter = 0
    index = []
    #now remove all subparenthesis by saving their indices when a counter > 1
    while i < length_substring:
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
    #Remove all subparenthesis by string splices
    for j in index:
        string = string[:j-i] + string[j+1-i:]
        i += 1
    return(string)

print(exp_process(string))

#This function removes sub parenthesis from first expression ex) (A(BC))(D(EF)) -> ABC(DEF)
'''def simplify_string(string):
    counter = 0
    first_paren = []
    length_string = len(string)
    i = 0
    stack = []
    #Remove parenthesis around first character if it is present
    inner_flag = 0
    if string[0] == '(':
        while i < length_string:
            if string[i] == '(':
                stack.append(i)
                counter += 1
            elif string[i] == ')':
                stack.append(i)
                counter -= 1
                if counter == 0:
                    inner_flag = 1
            if inner_flag == 1:
                break
            i += 1
    j = 0
    for i in stack:
        string = string[:i-j] + string[i+1-j:]
        j += 1
    length_substring = len(string)
    i = 0
    counter = 0
    index = []
    #remove parenthesis around sub expressions
    while i < length_substring:
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
    return(string)'''
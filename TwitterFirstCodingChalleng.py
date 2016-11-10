# If the order of the operations did not matter I considered doing a check to see if R was even then do not do anything of only do S if it was greater than one. Because it was not specified I decided to do each operation as it was given.
import re
string = '343(((5)67)8) /RS'

def exp_process(string):
    if string == '':
        return('Input is empty') #If string is empty inform the user
    regex = r'/([RSrs]+)?'
    #Using regex capture the text that conatins the commands the program will do
    matches = re.search(regex, string, re.IGNORECASE)
    string = string.replace(matches.group(0), '').strip()
    flag = 0
    for operation in matches.group(0):
        #if an R is found reverse the string
        if operation == 'R' or operation == 'r':
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


        elif operation == 'S'or operation == 's':
            #if a S is found simply the string
            if flag == 1:
                continue
            #remove first parenthesis
            counter = 1
            first_paren = []
            length_string = len(string)
            i = 0
            if string[0] == '(':
                while i < length_string - 1:
                    if string[i+1] == '(':
                        counter += 1
                    elif string[i+1] == ')':
                        counter -= 1
                        if counter == 0 and len(first_paren) == 0:
                            first_paren.append(i+1)
                    i += 1
                string = string[1:first_paren[0]] + string[first_paren[0]+1:]

            length_substring = len(string)
            i = 0
            counter = 0
            index = []
            if string[0] == '(':
                flag_first_paren = 1
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
            flag = 1
    return(string)

print(exp_process(string))

'''counter = 1
            first_paren = [0]
            length_string = len(string)
            i = 0
            if string[0] == '(':
                while i < length_string - 1:
                    if string[i+1] == '(':
                        first_paren.append(i+1)
                        counter += 1
                    elif string[i+1] == ')':
                        first_paren.append(i+1)
                        counter -= 1
                        if counter == 0:
                            break
                    i += 1
                i = 0
                for j in first_paren:
                    string = string[:j-i] + string[j+1-i:]
                    i+=1'''

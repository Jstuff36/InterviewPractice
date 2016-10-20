# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:04:12 2016

@author: Justin
"""
#problem 1
def num_printer(num):
    if len(str(num)) > 3:
        return(-1) 
    #Exit if number is greater than 3 digits
    remainders = []
    temp = num
    for i in range(len(str(temp))):
        remainders.append(temp % 10)
        temp = int(temp / 10)
    remainders = remainders[::-1]
    
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen']
    tens = ['', '', 'twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']
    
    word_num = []
    
    if len(remainders) == 1:
        word_num.append(ones[remainders[0]])
    elif len(remainders) == 2 and num > 19:
        word_num.append(tens[remainders[0]])
        word_num.append(ones[remainders[1]])
    elif len(remainders) == 2 and num < 20:
        word_num.append(teens[remainders[1]])
    elif len(remainders) == 3:
        word_num.append(ones[remainders[0]])
        word_num.append('hundred')
        word_num.append(tens[remainders[1]])
        word_num.append(ones[remainders[2]])
    
    word_num = ' '.join(word_num)
    return(word_num)



#problem 2
def num_finder(array):
    #parameter checks
    for i in range(len(array) - 1):
        if array[i+1] - array[i] != 1:
            return(i + 1)
    return(-1)

array = [0, 1, 2, 3, 5]

num_finder(array)
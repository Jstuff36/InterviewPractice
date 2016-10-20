# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 06:59:51 2016

@author: Justin
"""

#Return largest second most frequent number
array = [3, 5, 3, 10, 5, 2, 9, 3, 2, 10]
#Check for edge cases
array.sort()
largest = [0,0]
second_largest = [0,0]

for i in range(len(array)-1):
    j = i
    counter = 0
    while array[i] == array[j]:       
        j += 1
        counter += 1
        if j == len(array):
            break
    if counter > largest[1]:
        second_largest = largest
        largest = [array[i], counter]
    elif counter == largest[1]:
        largest = [array[i], counter]
    elif counter == second_largest[1]:
        second_largest = [array[i], counter]
    elif counter > second_largest[1] and counter < largest[1]:
        second_largest = [array[i], counter]
    i = j
    
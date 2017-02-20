#### Winning Streak ####
# You are a professional chess player. Your competitive record is stored as a
# string of 'W's and 'L's, signifying matches you've won and lost. Write a
# function that determines your longest winning streak from a given record.
#
# Examples:
# winning_streak("LW") # => 1
# winning_streak("LL") # => 0
# winning_streak("WWW") # => 3
# winning_streak("WLLWWWLW") # => 3

def winning_streak(test_string):
    longest_steak = 0
    i = 0
    while i < len(test_string):
        counter = 0
        if test_string[i] == 'W':
            counter = 1
            j = i + 1
            while j < len(test_string) and test_string[i] == test_string[j]:
                counter += 1
                j += 1
            i = j
        else:
            i += 1
        if counter > longest_streak:
            longest_steak = counter

    return(longest_steak)






#### Aliquot Sequence ####
# A number's aliquot sum is the sum of all of its factors excluding itself.
#
# For example, the aliquot sum of 10 is: 1 + 2 + 5 = 8
#
# We can use the aliquot sum to define a special sequence, called the
# aliquot sequence. The aliquot sequence of a number begins with the
# number itself. The second number in the sequence is the first number's
# aliquot sum, the third number is the second number's aliquot sum, and
# so on.
#
# For example, the first 4 numbers in the aliquot sequence of 10 are: 10, 8, 7, 1
#
# Write a function that takes in two numbers, base and n, and returns the
# aliquot sequence of length n starting with base.
#
# Examples:
# aliquot_sequence(10, 4) # => [10, 8, 7, 1]
# aliquot_sequence(10, 2) # => [10, 8]
# aliquot_sequence(7, 4) # => [7, 1, 0, 0]

def aliqot_sequence(base, n):
    ans = []
    ans.append(base)
    while len(ans) < n
        temp = []
        for i in range(1, base):
            if int(base / i) == base / i:
                temp.append(i)
        ans.append(sum(temp))
        base = sum(temp)
    return(ans)









#### Pascal's Triangle ####
# This is an example of Pascal's Triangle:
#
#  depth
#    0   |      1
#    1   |     1 1
#    2   |    1 2 1
#    3   |   1 3 3 1
#    4   |  1 4 6 4 1
#
#
# Pascal's Triangle is a mathematical construct that follows a simple
# rule: each number in the triangle is the sum of the two numbers
# directly above-and-to-the-left and above-and-to-the-right of it.
#
# For example, to find the next row after [1,2,1]:
#
#         1       2       1
#
#     1       3       3       1
#     |       |       |       |
#  (0 + 1) (1 + 2) (2 + 1) (1 + 0)
#
#
# Write a function that will return Pascal's Triangle at the given
# depth. The triangle should be represented as an array of rows.
#
# pascals_triangle(0) => [[1]]
# pascals_triangle(2) => [[1], [1,1], [1,2,1]]
# pascals_triangle(4) => [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]



def pascals_triangle(depth):
    if depth == 0:
        return [[1]]
    if depth == 1:
        return [[1], [1,1]]
    previous = pascale_triangle(depth - 1)
    return previous.append(pascals_helper(previous[-1]))

def pascals_helper(lower_depth):
    temp = [1]
    for i in range(len(lower_depth)):
        temp.append(lower_depth[i] + lower_depth[i+ 1])
    return temp.append(1)
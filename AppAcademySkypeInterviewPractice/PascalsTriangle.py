def pascals_triangle(depth):
    if depth == 0:
        return [[1]]
    if depth == 1:
        return [[1], [1,1]]
    previous = pascals_triangle(depth - 1)
    return previous.append(pascals_helper(previous[-1]))

def pascals_helper(lower_depth):
    temp = [1]
    for i in range(len(lower_depth)-1):
        temp.append(lower_depth[i] + lower_depth[i + 1])
    return temp.append(1)

print(pascals_triangle(2))
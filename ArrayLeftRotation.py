def array_left_rotation(arr, NumElements, NumTimes):
    for i in range(NumTimes):
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)
    return(arr)

arr = list(range(20))
NumElements = len(arr)
NumTimes = 5
print(array_left_rotation(arr, NumElements, NumTimes))

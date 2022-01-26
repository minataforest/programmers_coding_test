def solution(arr, divisor):

    temp = []

    for i in arr:
        if i % divisor == 0:
            temp.append(i)

    temp.sort()

    if len(temp) > 0:
        return temp
    else:
        return [-1]
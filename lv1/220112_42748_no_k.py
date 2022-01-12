def solution(array, commands):
    answer = []
    for i in commands:
        new = array[i[0]-1 : i[1]]
        new.sort()
        no = i[2] -1
        answer.append(new[no])

    return answer

# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# [5, 6, 3]

# list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
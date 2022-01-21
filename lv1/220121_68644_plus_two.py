import itertools

def solution(numbers):

    result = itertools.combinations(numbers, 2)
    temp_result = set()

    for i in result:
        temp_result.add(sum(i)) 

    answer = sorted(list(temp_result))

    return answer
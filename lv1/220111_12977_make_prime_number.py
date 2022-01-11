import itertools

nums = [1, 2, 7, 6, 4]

def solution(nums):
    answer = 0
    prime = []

    temp = itertools.combinations(nums, 3)

    for i in temp:
        prime.append(sum(i))

    for i in prime:
        for j in range(2, i):
            if i % j == 0:
                break

            answer += 1 if i == j+1 else 0

    return answer
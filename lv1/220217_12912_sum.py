def solution(a, b):
    min_no = min(a, b)
    max_no = max(a, b)

    return sum([i for i in range(min_no, max_no+1)])
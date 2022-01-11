def solution(numbers):
    all_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0

    for i in all_number:
        if i not in numbers:
            answer += i


# def solution(numbers):
#     return 45 - sum(numbers)
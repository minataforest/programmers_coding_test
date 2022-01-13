def solution(answers):
    fst = [1, 2, 3, 4, 5]
    scd = [2, 1, 2, 3, 2, 4, 2, 5]
    thd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    if len(fst) < len(answers):
        fst *= (len(answers) // len(fst)) + 1

    if len(scd) < len(answers):
        scd *= (len(answers) // len(scd)) + 1

    if len(thd) < len(answers):
        thd *= (len(answers) // len(thd)) + 1

    a = {1: 0, 2: 0, 3: 0}

    for i in range(0, len(answers)):
        a[1] += 1 if answers[i] == fst[i] else 0
        a[2] += 1 if answers[i] == scd[i] else 0
        a[3] += 1 if answers[i] == thd[i] else 0

    answer = []
    answer_max = max(a.values())

    for key, value in a.items():
        if value == answer_max:
            answer.append(key)

    return answer


solution([1, 2, 3, 4, 5])

# pattern1 = [1, 2, 3, 4, 5]
# pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
# pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# score = [0, 0, 0]
# result = []
#
# for idx, answer in enumerate(answers):
#     if answer == pattern1[idx % len(pattern1)]:
#         score[0] += 1
#     if answer == pattern2[idx % len(pattern2)]:
#         score[1] += 1
#     if answer == pattern3[idx % len(pattern3)]:
#         score[2] += 1
#
# for idx, s in enumerate(score):
#     if s == max(score):
#         result.append(idx + 1)
#
# return result
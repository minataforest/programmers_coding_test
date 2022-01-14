# n=5
# lost = [2, 4]
# reserve = [1, 3, 5]

n=9
lost = [5,6,8,1,2]
reserve = [2,3,4,8,9 ]


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 도난 당한 학생과 여벌 있는 학생이 같은지
    for i in lost[:]:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)

    # 도난 당한 학생 앞뒤로 여벌 있는 학생이 있는지
    for i in lost[:]:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
            continue

        if i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)
            continue

    answer = n - len(lost)

    return answer



solution(n, lost, reserve)
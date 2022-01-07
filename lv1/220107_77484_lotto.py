lottos=[0, 0, 0, 0, 0, 0]
win_nums=[38, 19, 20, 40, 15, 25]

# lottos=[45, 4, 35, 20, 3, 9]
# win_nums=[20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):

    # set 교집합
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]

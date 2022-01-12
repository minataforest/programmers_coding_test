def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1

    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]

    return list(d.keys())[0]


# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]


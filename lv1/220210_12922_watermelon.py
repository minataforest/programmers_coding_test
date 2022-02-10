def solution(n):

    i, mod = divmod(n, 2)

    return '수박'*i if mod ==0 else '수박'*i + '수'
def solution(n):
    
    ternary = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        ternary += str(mod)
    
    answer = int(ternary, 3)
    return answer
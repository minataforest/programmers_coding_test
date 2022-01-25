def solution(s):    
    result = divmod(len(s), 2)

    return s[result[0]-1: result[0]+1] if result[1] == 0 else s[result[0]]
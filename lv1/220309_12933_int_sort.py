def solution(n):
    
    temp = sorted((str(int(n))), reverse=True)
    answer = "".join(temp)
    
    return int(answer)
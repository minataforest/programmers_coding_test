def solution(left, right):
    
    answer = 0
    
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            cnt += 1 if i%j == 0 else 0
            if j == i:
                answer += i if cnt%2==0 else -i
    
    return answer
def solution(d, budget):
    d.sort()
    total_money = 0 # 부서 예산 합
    
    for i in range(len(d)):
        total_money += d[i]
        
        if total_money < budget: # 예산 합이 예산보다 적은 경우
            continue
            
        elif total_money == budget: # 예산 합이 예산과 같은 경우
            return i+1
        
        else: # 총합이 예산보다 많은 경우
            return i
        
    # 부서가 1개인 경우. 혹은 모든 부서 예산합이 총예산보다 적은 경우
    return len(d)
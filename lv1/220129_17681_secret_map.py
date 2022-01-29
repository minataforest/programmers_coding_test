def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        one = bin(arr1[i])[2:]
        two = bin(arr2[i])[2:]
        
        one = one.zfill(n)
        two = two.zfill(n)
        
        string = ''
        
        for j in range(n):
            string += "#" if max(one[j], two[j]) == "1" else " "

        answer.append(string)
        

    return answer
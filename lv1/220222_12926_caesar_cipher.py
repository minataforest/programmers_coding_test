def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += ' '
        else:          
            if i.isupper(): # 대문자인 경우  65 ~ 90
                if (ord(i)+n) > 90:
                    answer += chr(ord(i)+n-26) 
                else:
                    answer += chr(ord(i)+n)

            else: # 소문자인 경우 97 ~ 122
                if (ord(i)+n) > 122:
                    answer += chr(ord(i)+n-26) 
                else:
                    answer += chr(ord(i)+n)

    return answer

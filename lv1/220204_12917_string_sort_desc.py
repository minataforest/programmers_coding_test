def solution(s):

    upper=[]
    lower=[]

    for i in s:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)

    upper.sort(reverse=True)
    lower.sort(reverse=True)

    temp1 = ''.join(lower)
    temp2 = ''.join(upper)

    return temp1+temp2

# def solution(s):
#    return ''.join(sorted(s, reverse=True))
import re

def solution(s):
    x = re.search("[^0-9]", s)

    if x:
        return False
    else:
        if len(s)==4 or len(s)==6:
            return True
        else:
            return False


# def alpha_string46(s):
#    return s.isdigit() and len(s) in (4, 6)

# def alpha_string46(s):
#    import re
#    return bool(re.match("^(\d{4}|\d{6})$", s))
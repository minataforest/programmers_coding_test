def solution(s):
    return int(s) if s[0] != '-' else (0 - int(s[1:]))
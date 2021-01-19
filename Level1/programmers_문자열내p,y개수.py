def solution(s):
    if s.count('p')+s.count('P') == s.count('y')+s.count('Y'):
        return TRUE
    elif s.count('p')+s.count('P') == 0 and s.count('y')+s.count('Y') == 0:
        return TRUE
    else:
        return FALSE

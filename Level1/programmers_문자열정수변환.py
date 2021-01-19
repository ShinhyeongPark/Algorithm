def solution(s):
    answer = 0
    
    if 1 <= len(s) <= 5:
        if s.count('-') != 0:
            answer = int(s.replace('-', '')) * (-1)
        elif s.count('+') == 1:
            answer = int(s.replace('-', ''))
        else:
            answer = int(s)
        
    return answer

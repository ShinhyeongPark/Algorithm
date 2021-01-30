import re

def solution(new_id):
    expr= re.compile('[a-z0-9\-\_\.]')
    new_id = new_id.lower() #문자열 소문자 변환
    m = expr.findall(new_id) #정규표현식에 따른 특수문자 제거

    #연속된 . 축약
    stack = []
    i = 0

    while i < len(m):
        if m[i] == '.':
            if not stack:
                stack.append(m[i])
                i+= 1
            else:
                del m[i]
        else:
            if stack:
                del stack[:]
                i += 1
            else:
                i+= 1
    if m:
        if m[0] == '.':
            del m[0]
    if m:
        if m[-1] == '.':
            del m[-1]
    if not m:
        m.append('a')

    if len(m) >=16:
        m = m[:15]
        if m[-1] == '.':
            del m[-1]

    if len(m) <= 2:
        while len(m) < 3:
            m.append(m[-1])

    return ''.join(m)

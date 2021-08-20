# 올바른 괄호인지 판단하는 함수
def f(strr):
    # return False: 올바른 문자열 X
    stack = []
    for s in strr:
        if s == '[':
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == '{':
            stack.append(s)
        else:
            if not stack:  # 스택이 비어있다면, 비교할 대상이 없으므로
                return False
            else:
                if s == ']' and stack.pop() != '[':
                    return False
                elif s == '}' and stack.pop() != '{':
                    return False
                elif s == ')' and stack.pop() != '(':
                    return False
    return True


def solution(s):
    answer = 0
    # 문자열의 길이가 홀수일 경우 애초에 올바른 문자열이 될 수 없다.
    if len(s) % 2 != 0:
        return answer

    #문자열 길이만큼 반복
    for i in range(len(s)):
        if f(s) == True: #올바른 문자열일 경우
            answer += 1
        s = s[1:] + s[0] #맨앞의 문자열만 맨뒤로

    return answer

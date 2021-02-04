#효율성 통과
#STACK을 사용해, 현재 원소와 스택의 마지막값을 비교하는 방식으로 변경했다.
def solution(s):
    strlst = list(s) #String to List 
    stack = []

    for v in strlst: #리스트 원소만큼 반복
        if not stack: #스택이 비었을 경우
            stack.append(v) #비교를 하지 못하므로, 단순히 삽입
        else: #스택이 있을 경우, 비교
            if stack[-1] == v: #스택의 마지막 값과 비교했을 때 같을 경우 = 연속된 문자
                stack.pop() #스택 제거
            else: #다른 문자일 경우
                stack.append(v) #삽입

    if not stack: #비교가 끝난 후, 스택이 비었을 경우 짝지어 제거하기 성공
        return 1
    else:
        return 0
        
 /*시간초과 코드*/
 //단순히 인덱스를 갖고 비교한 후 제거한 뒤, 반복문을 처음부터 다시 시작해서
 //시간 초과가 발생했다.
 def solution(s):
    strlst = list(s)

    while strlst: #문자열이 모두 제거될때까지
        count = 0
        for i in range(len(strlst)-1):
            if strlst[i] == strlst[i+1]:
                del strlst[i]
                del strlst[i]
                break
            else:
                count += 1
        
        if count == len(strlst)-1:
            return 0

    return 1


M, N = map(int, input().split()) #M: 자리수, N: 삭제할 갯수

num = list(map(int, list(input()))) #숫자를 각 자리별로 분리

stack = []
delNum = N 

for i in range(M):
    while delNum > 0 and stack: #스택에 값이 존재하고, 아직 삭제할 숫자가 남아 있을 경우
        if stack[-1] < num[i]: #스택에 마지막 값과 비교
            stack.pop() #제거
            delNum -= 1 #삭제할 갯수 감소
        else:
            break
    stack.append(num[i]) 

print(''.join(map(str,stack)))

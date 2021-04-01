#입력마다 합 계산
N = int(input())

stack = []
SUM= 0
for i in range(N):
    n = int(input())
    if n == 0:
        SUM -= stack.pop()
    else:
        stack.append(n)
        SUM += n

print(SUM)

#입력이 다 끝나고 스택으 총합 계산
N = int(input())

stack = []
for i in range(N):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))

#결론:매 입력시 총합을 계산(덧셈,뺄셈)을 하는 것이 리스트의 총합을 구하는 것 보다 처리속도 빠름

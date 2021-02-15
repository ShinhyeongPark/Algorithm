n = int(input())
stack = []
for i in range(n+1): #0~n까지 제곱
    stack.append(str(2**i))

print(' '.join(stack))

n = int(input())
stack = []
for i in range(n+1):
    stack.append(str(n-i))

print(' '.join(stack))

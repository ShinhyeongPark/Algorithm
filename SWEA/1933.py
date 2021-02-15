n = int(input())
stack = []
for i in range(1,n+1):
    if n%i == 0:
        stack.append(str(i))

print(' '.join(stack))

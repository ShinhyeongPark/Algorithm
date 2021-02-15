n = int(input())
stack = []

for i in range(1, n+1):
    count = 0
    if '3' in list(str(i)) or '6' in list(str(i)) or '9' in list(str(i)):
        count += list(str(i)).count('3')
        count += list(str(i)).count('6')
        count += list(str(i)).count('9')
        stack.append('-'*count)
    else:
        stack.append(str(i))

print(' '.join(stack))

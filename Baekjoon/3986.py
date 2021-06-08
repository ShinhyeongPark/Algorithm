T = int(input())

count = 0
for t in range(T):
    word = input()
    stack = []

    for w in word:
        if len(stack) != 0 and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    if not stack:
        count += 1

    
print(count)

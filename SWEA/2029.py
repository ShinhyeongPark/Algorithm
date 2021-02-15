T = int(input())
for i in range(T):
    nums = map(int, input().split())
    stack = []

    for num in nums:
        stack.append(num)

    print('#' + str(i+1),str(int(stack[0]/stack[1])),str(stack[0]%stack[1]))

nums = map(int, input().split())
stack = []

for num in nums:
    stack.append(num)

print(stack[0]+stack[1])  
print(stack[0]-stack[1])  
print(int(stack[0]/stack[1]))
print(stack[0]%stack[1])

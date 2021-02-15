nums = map(int, input().split())
stack = []

for num in nums:
    stack.append(str(num))
#1:가위 2:바위 3:보
if stack[0] == '1' and stack[1] == '2':
    print('B')
elif stack[0] == '1' and stack[1] == '3':
    print('A')
elif stack[0] == '2' and stack[1] == '1':
    print('A')
elif stack[0] == '2' and stack[1] == '3':
    print('B')
elif stack[0] == '3' and stack[1] == '1':
    print('B')
elif stack[0] == '3' and stack[1] == '2':
    print('A')

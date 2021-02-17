T = int(input()) #테스트 케이스 수

for t in range(T):
    n = int(input())
    stack = []
    for i in range(n):
        nums = list(input().split()) #H,M,H,M

        for j in range(int(nums[1])):
            stack.append(nums[0])

    print("#"+str(t+1))
    while stack:
        if len(stack) <= 10:
            print(''.join(stack))
            del stack[:len(stack)]
        else:
            print(''.join(stack[:10]))
            del stack[:10]

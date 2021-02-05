T = int(input())
for i in range(T):
    nums = map(int, input().split())
    stack = []
    answer = 0
    for num in nums:
        if num % 2 != 0:
            stack.append(num)

    print("#"+ str(i+1), str(sum(stack)))
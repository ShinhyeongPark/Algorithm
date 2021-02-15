T = int(input())

for i in range(T):
    nums = map(int, input().split())
    stack = []
    count = 0
    for num in nums:
        count += 1
        stack.append(num)
    #리스트의 최소,최대값 제거
    stack.remove(min(stack)) 
    stack.remove(max(stack))
    #리스트의 갯수로 나눈다 -> 평균
    print("#"+str(i), int(round(sum(stack)/(count-2))))

T = int(input())

for n in range(T):
    answer = 0
    sum_stack = []
    nums = list(map(int, input().split()))

    str1 = list(map(int, input().split()))
    str2 = list(map(int, input().split()))

    if nums[0] > nums[1]: #str1이 더 길때
        for i in range(0, nums[0]-nums[1]+1): #긴문자열에 시작 위치: i
            answer = 0
            for j in range(0, nums[1]): #짧은문자열
                answer = answer + str1[i+j] * str2[j]
            sum_stack.append(answer)
    else:
        for i in range(0, nums[1]-nums[0]+1): #
            answer = 0
            for j in range(0, nums[0]):
                answer = answer + str1[j] * str2[i+j]
            sum_stack.append(answer)

    print("#"+str(n+1), max(sum_stack))

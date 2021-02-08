T = int(input())
for i in range(T):
    nums = map(int, input().split())
    answer = 0

    for num in nums:
        if num > answer:
            answer = num

    print("#" + str(i+1), str(answer))
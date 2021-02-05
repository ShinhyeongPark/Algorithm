import math

T = int(input()) #Case 수
for i in range(T): #Case만큼 반복
    nums = map(int, input().split())
    answer = 0
    for num in nums:
        answer += num

    print("#"+ str(i+1), str(round(answer/10)))
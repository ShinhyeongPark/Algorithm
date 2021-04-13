#알고리즘
#3을 넘어가면 간격이 커지는 것을 보고
#일정한 값이 증가하는 것은 아니라고 판단했다.

T = int(input()) #테스트 케이스 수

for i in range(T):
    N = int(input())

    dp = [1, 2, 4]
    for i in range(3, N): #3 ~ N-1
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    print(dp[N-1])

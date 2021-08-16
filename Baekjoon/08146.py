def solution(numOfStairs):
    dp = [0] * 71
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, numOfStairs+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[numOfStairs]

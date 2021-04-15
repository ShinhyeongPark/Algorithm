N = int(input())

dp = [0] * (N+1)
dp[0] = 1
# print(dp)
for i in range(1, N+1): #N번 반복
    for j in range(0,i):
        dp[i] += dp[j] * dp[i-j-1]
# print(dp)
print(dp[N])

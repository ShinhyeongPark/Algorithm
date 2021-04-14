#알고리즘
#길이 N마다 가질 수 있는 경우의 수를 나열하고
#규칙을 찾았다.
#점화식 : dp[i] = dp[i-1] + dp[i-2]

N = int(input())

dp = [0,1,2]

for i in range(3, N+1):
    dp.append((dp[i-1] + dp[i-2])%10007)

print(dp[N])

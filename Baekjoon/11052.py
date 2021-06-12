N = int(input())
card = [0]
card += list(map(int, input().split())) #[0,1,5,6,7]

dp = [0] * (N+1)
dp[1] = card[1]

for i in range(2,N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + card[j]:
            dp[i] = dp[i-j] + card[j]

print(dp[-1])

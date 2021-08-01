import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [[""] * (len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + A[i-1]
        else:
            left = dp[i][j-1]
            up = dp[i-1][j]
            if len(left) < len(up):
                dp[i][j] = up
            else:
                dp[i][j] = left

print(dp)
answer = dp[-1][-1]
print(len(answer))
if len(answer) != 0:
    print(answer)

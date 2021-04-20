#간단한 DP문제이다
#1칸 또는 2칸으로 N만큼 간다는 의미는
#1과 2를 사용해 N을 만드는 경우의 수를 의미한다.
#1부터 경우의 수를 구하면
#피보나치 수열을 이루는것을 알 수 있다.

def solution(n):
    if n < 3:
        return n
    dp = [0,1,2]
    
    for i in range(3,n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n] % 1234567

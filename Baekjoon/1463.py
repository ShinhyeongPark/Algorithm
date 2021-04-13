#이전 값들의 최소 횟수를 저장함으로써
#재귀적인 연산을 없애고 저장된 값을 사용해 현재 값의 최소횟수를 구한다.

N = int(input())

dp = [0,0,1,1]

for i in range(4,N+1):
    x = i
    result = []
    if x % 3 == 0: 
        result.append(dp[int(x/3)])
    if x % 2 == 0:
        result.append(dp[int(x/2)])
    result.append(dp[x-1])

    #10을 예로 들면 10 -> 9, 10 -> 5로 가는 두가지 경우가 있는데
    #만약 10 -> 9 로 가면 dp[9]인 2회이지만 5로 가면 dp[5]인 3이다.
    #비교대상 중 최소 값을 가져와 연산 1회를 더해준 결과를 리턴한다.
    dp.append(min(result) + 1)

print(dp[N])

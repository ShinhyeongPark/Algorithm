N = int(input())

date = [] #상담일수
cost = [] #상담 비용
dp = [] #해당 날짜의 최대 비용

for i in range(N):
    x,y = map(int, input().split())
    date.append(x)
    cost.append(y)
    dp.append(y)
dp.append(0)

for i in range(N-1, -1, -1): #뒤에서부터 비교
    if i + date[i] > N: #시작시점에서 상담기간을 더한 값이 퇴사일을 넘어갈 경우
        dp[i] = dp[i+1] #첫번째 예시로 9일 10일 같은 경우는 넘어간다.
    else:
        dp[i] = max(dp[i+1], cost[i]+dp[i + date[i]]) #현재 상담을 하지 않고 넘아갔을 때와
                                                        #현재 상담을 하고 다음 상담을 할때의 이윤을 비교

print(dp[0])

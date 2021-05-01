#순서는 반드시 지켜야한다.
N = int(input())

block = list(map(int,list(input().split())))
blockSize = len(block)
dp = [1] * blockSize #초기값: 각자 자기 자신을 포함하므로 1

for i in range(1,blockSize): #이전 상자의 최대로 들어갈 수 있는 상자의 갯수 비교
    for j in range(i): #자기보다 이전
        if block[i] > block[j]: #현재 상자가 이전 상자보다 크기가 클 경우
            dp[i] = max(dp[i], dp[j]+1) #자기가 더 많이 포함하거나, 아니면 자기보다 작은 상자가 더 많이 포함하거나

print(max(dp))

    
